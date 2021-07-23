import os
import socket
from urllib import parse
import pickle
import json
import subprocess
import time
import requests
import codecs
import iFactory.iDB as DB
import iFactory.i2_send as MQ_send
import pika, sys
import iFactory.email as email

status1 = ['alive', 'stop'] 
status2 = ['alive', 'disconnect', 'send fail', 'queue fail'] 
type3 = ['collector', 'wsgi', 'monitor'] 
status4 = ['data path change', 'device stop'] 
status5 = ['alive', 'disconnect', 'send fail', 'queue fail'] 
ret_list1 = []
ret_list2 = []
ret_list3 = []
ret_list4 = []
ret_list5 = []
ret_list6 = []
ret_list7 = []
email_group = { 'G1':['edison3.lin@gmail.com','edisonlin.hojac@gmail.com'],
                'G2':'b82506001@gmail.com',
                'G3':['edisonlin.hojac@gmail.com','b82506001@gmail.com'],
                'G4':['pega.edison@gmail.com','edisonlin.hojac@gmail.com']
             }

# i7_test = [
#     {"start_time": "2020-4-15 16:00:00", "end_time": "2020-4-15 23:59:59", "devices":[{"dev_id": "123456","vendor":"dek", "dev_type": "mounter"}]},
#     ['collector', 'wsgi', 'monitor'],
#     {'1':'a'},
#     {'1':'a', '2':'b'}
# ]
i7_URLs = [
    "http://127.0.0.1:8888/production_time",
    "http://127.0.0.1:8888/production_abnormal_time",
    "http://127.0.0.1:8888/down_time",
    "http://127.0.0.1:8888/error_report",
    "http://127.0.0.1:8888/spi_cpk",
    "http://127.0.0.1:8888/get_defect_info",
    "http://127.0.0.1:8888/get_yield_rate",
    "http://127.0.0.1:8888/get_cycle_time",
]
i7_inputs = [
    {"start_time": "2020-4-15 16:00:00", "end_time": "2020-4-15 23:59:59", "devices":[{"dev_id": "123456","vendor":"dek", "dev_type": "PRINTER"}]},
    
    {"start_time": "2020-4-15 16:00:00", "end_time": "2020-4-15 23:59:59", "devices":[{"dev_id": "123456","vendor":"dek", "dev_type": "mounter"}]},    
    
    {"start_time": "2020-4-15 16:00:00", "end_time": "2020-4-15 23:59:59", "devices":[{"dev_id": "123456","vendor":"dek", "dev_type": "PRINTER"}, {"dev_id": "56789","vendor":"Heller", "dev_type": "reflow"}]},

    {"vendor": "JT", "dev_id": "ABCED", "start_time": "2020-4-15 16:00:00", "error_code": ["JT_A01", "err_msg", "掉板"]},

    {"devlist":[{ "dev_id": "tri_abc","vendor":"tri"}, { "dev_id": "ky_qaz", "vendor":"ky"}]},    
    
    {"pcb_id": "194141300006169", "brd_idx": "1", "comp": "D5"},
    
    {"dev_id": "J092120317", "vendor": "JUTZE", "start_time": "20200101000000"},
    
    {"printer_vendor": "Dek", "printer_dev_id": "851641", "spi_vendor": "KY", "spi_dev_id": "SPI-83L381", "aoi_vendor": "JUTZE", "aoi_dev_id": " J092120317", "counter": 10}    
]


def ping_ip(dev_ip):
    is_up = subprocess.run("ping -n 1 -w 1 -c 1 %s" % dev_ip, shell=True, stdout=subprocess.PIPE) 
    return False if is_up.returncode else True


def send_cmd(dev_ip, command):
    ## return 從server收到的資料
    port = 4321
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((dev_ip, port))
        client.settimeout(5)
        client.sendall(parse.quote(command).encode('utf-8'))
        while True:
            recv_data = pickle.loads(client.recv(4096))
            if recv_data:
                client.close()
                return recv_data            
    except Exception as e:
        return ['no service']
    finally:
        client.close()
        
        
def ip_alive(iDB):
    i = 0
    for item in iDB:
        dev_ip = item['dev_ip']
        if ping_ip(dev_ip):
            iDB[i]['line'] = 'alive'
        else:
            iDB[i]['line'] = 'stop'
        i += 1 
    return iDB
 
        
def Exec_cmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return p.communicate()

        
""" 1. Chcek Dev alive
    1. Chcek Dev alive
    1. Chcek Dev alive
""" 
def i1(iDB):
    ping_list = list()
    for item in iDB:
        if item['line'] == 'alive':
            ping_list.append({'dev_id':item['dev_id'], 'status':'alive'})
        else:
            ping_list.append({'dev_id':item['dev_id'], 'status':'disconnect'})
    return ping_list
    
""" 2. Check AMQP alive 
    3. Check AMQP alive 
    4. Check AMQP alive 
"""
def i2():
    if MQ_send.MQ_send('PegatronMQ'):
        time.sleep(1)
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()
            r = channel.basic_get(queue='Edison', auto_ack=False)
            if r[2].decode() == 'PegatronMQ':
                channel.queue_delete(queue='Edison')
                connection.close()
                return True
            else:
                connection.close()
                return False
        except Exception as e:
            print("Error message: ", e)
            # wait()
        # except: 
            return False
    else:
        # wait()
        return False

""" 3. Chcek Dev process
    3. Chcek Dev process
    3. Chcek Dev process
""" 
def i3(iDB):
    process_list = list()
    for item in iDB:
        dev_ip = item['dev_ip']
        dev_id = item['dev_id'] 
        if item['line'] == 'alive':
            msg = b'"Process_Operate"'
            P_type = send_cmd(dev_ip, msg)
            if not P_type:
                email.send(email_group['G3'])
            process_list.append({'dev_id':dev_id, 'type':P_type})
        else:
            process_list.append({'dev_id':dev_id, 'type':'No_connected'})
    return process_list

""" 4. Check Dev Operate
    4. Check Dev Operate
    4. Check Dev Operate
"""    
def i4(iDB):
    log_list = list()
    for item in iDB:
        dev_ip = item['dev_ip']
        dev_id = item['dev_id'] 
        if item['line'] == 'alive':
            if item['equip_type'] == 'AOI':
                msg = b'"AOI_Operate"'
            elif item['equip_type'] == 'SPI':
                msg = b'"SPI_Operate"'
            elif item['equip_type'] == 'Printer':
                msg = b'"Printer_Operate"'
            elif item['equip_type'] == 'Reflow':
                msg = b'"Reflow_Operate"'
            elif item['equip_type'] == 'Mounter':
                msg = b'"Mounter_Operate"'
            else:
                msg = b'"cancel"'
            # msg = b'"quit"'
            log = send_cmd(dev_ip, msg)
            log_list.append({'dev_id':dev_id, 'status':log[0]})
            if log[0] == 'device stop':
                email.send(email_group['G4'])
        else:
            log_list.append({'dev_id':dev_id, 'status':'No_connected'})
    return log_list

""" 5. Check Raspberry Operate
    5. Check Raspberry Operate
    5. Check Raspberry Operate
"""   
def i5(iDB):
    Ras_list = list()
    for item in iDB:
        if ((item['line'] == 'alive') and ((item['equip_type'] == 'Printer') or (item['equip_type'] == 'Reflow'))):
            dev_ip = item['dev_ip']
            dev_id = item['dev_id'] 
            msg = b'"Raspberry"'
            Ras = send_cmd(dev_ip, msg)
            Ras_list.append({dev_id:Ras[0]})
    return Ras_list            

""" 6. Check DB Update
    6. Check DB Update
    6. Check DB Update
"""   
def i6():
    with open('os.txt', 'r') as f1:
        a = f1.readlines()
        t_str = ''
        for d in a:
            if 'start_time' in d:
                b = d.strip('\n')        
                e = b.split(' ')
                i = 0
                for f in e:
                    if f == 'start_time':
                        t_str = e[i+1]+' '+e[i+2]    
                    i += 1    
                file_stamp = time.mktime(time.strptime(t_str,"%Y-%m-%d %H:%M:%S"))
                now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
                now_stamp = time.time()
                t = now_stamp - file_stamp
                Sday = 60*60*24
                Shour = 60*60
                Smin = 60
                Dday = (t // Sday)
                t1 = t % Sday
                Dhour = (t1 // Shour)
                t2 = t1 % Shour
                Dmin = (t2 // Smin)
                Dsec = t2 % Smin
                # print("%d %d %d %d"%(Dday, Dhour, Dmin, Dsec))                
                with open('d.txt','w') as f2:
                    f2.write('%s to %s\n' % (t_str, now_time))
                    if Dday == 0:
                        if Dhour != 0:
                            f2.write("檔案未更新的時間： %d小時 %d分鐘 %d秒" %(Dhour, Dmin, Dsec))
                        elif Dmin != 0:  
                            f2.write("檔案未更新的時間： %d分鐘 %d秒" %(Dmin, Dsec))
                        else:  
                            f2.write("檔案未更新的時間： %d秒" %(Dsec))
                    else:        
                        f2.write("檔案未更新的時間：%d天 %d小時 %d分鐘 %d秒" %(Dday, Dhour, Dmin, Dsec))
        if not t_str:
            with open('d.txt','w') as f2:
                f2.write("cant find start_time")  
                
                
""" X. Run remote xServer.py
    X. Run remote xServer.py
    X. Run remote xServer.py
""" 
def i7():
    ret_list = list()
    index = 0
    for x in i7_URLs:
        # print("curl -X POST {url} {input}\n".format(url=x, input=i7_inputs[index]))
        _out, _err = Exec_cmd("curl -X POST {url} {input}".format(url=x, input=i7_inputs[index]))
        # wait()
        index += 1
        try:
            json.loads(_out)
            ret_list.append({'API':index, 'result':'true'})
        except:
            ret_list.append({'API':index, 'result':'false'})
    return ret_list
# Wait for ESC key
import msvcrt
def wait():
    while True:
        print('\npress \'ESC\' to continue....\n')
        a_key = msvcrt.getch()
        if a_key == b'\x1b':
            break
   
def main():
    iDB = DB.Get_DB()   #DB objects
    # iDB = ip_alive(iDB)
    while True:
        os.system('cls')
        ret_list1 = []
        ret_list2 = []
        ret_list3 = []
        ret_list4 = []
        ret_list5 = []
        ret_list7 = []
        ## function 0
        iDB = ip_alive(iDB)                                  
        with codecs.open("fun0.json", "w", "utf-8") as fout:
            json.dump(iDB, fout, indent=4, sort_keys=True)                
        ## function 1
        print('(1) Check Device alive\n')
        ret_list1 = i1(iDB)
        with codecs.open("_Check_Dev_Alive.json", "w", "utf-8") as fout:
            json.dump(ret_list1, fout, indent=4, sort_keys=True)
            
        ## function 2
        print('(2) Check Amqp alive\n')
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        if i2():
            ret_list2.append({'amqp_ip':local_ip, 'status':'alive'})
        else:
            ret_list2.append({'amqp_ip':local_ip, 'status':'disconnect'})
            email.send(email_group['G2'])
            
        with codecs.open("_Check_Amqp_Alive.json", "w", "utf-8") as fout:
            json.dump(ret_list2, fout, indent=4, sort_keys=True)
        
        ## function 3
        print('(3) Check Process operate\n')
        ret_list3 = i3(iDB)
        # print(ret_list3)
        with codecs.open("_Check_Process_Operate.json", "w", "utf-8") as fout:
            json.dump(ret_list3, fout, indent=4, sort_keys=True)
        
        ## function 4
        print('(4) Check Device operate\n')
        ret_list4 = i4(iDB)
        # print(ret_list4)
        with codecs.open("_Check_Dev_Operate.json", "w", "utf-8") as fout:
            json.dump(ret_list4, fout, indent=4, sort_keys=True)
            
        ## function 5
        print('(5) Check Raspberry operate\n')
        ret_list5 = i5(iDB)
        # print(ret_list5)
        with codecs.open("_Check_Raspberry_Operate.json", "w", "utf-8") as fout:
            json.dump(ret_list5, fout, indent=4, sort_keys=True)

        ## function 6
        print('(6) Check DB update\n')
        i6()
        with codecs.open("_Check_DB_Update.json", "w", "utf-8") as fout:
            json.dump(ret_list6, fout, indent=4, sort_keys=True)
        
        ## function 7
        print('(7) Check API interface\n')
        ret_list7 = i7()  
        with codecs.open("_Check_API_iFactory.json", "w", "utf-8") as fout:
            json.dump(ret_list7, fout, indent=4, sort_keys=True)
    #     sys.exit(0)
    
    
if __name__ == '__main__':
    main()
        
