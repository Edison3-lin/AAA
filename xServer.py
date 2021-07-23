# -*- coding: utf-8 -*-
import socket
import os
import threading

import urllib.parse
import ctypes
import datetime
import subprocess
import json
import pickle
import time
from pathlib import Path

local_port = 4321                           # 配置socket server繫結的本地埠
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)   # 配置socket server繫結的本地IP
# local_ip = '168.95.0.2'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((local_ip, local_port))

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("172.0.0.1",local_port))
server.listen(5)

# 只響應白名單中的計算機發來的任務
# admin_filter的key()
admin_filter = list()
admin_filter.append('127.0.0.1')
admin_filter.append('172.20.10.3')
admin_filter.append('172.20.10.4')
admin_filter.append('168.95.0.1')
admin_filter.append('168.95.0.2')


# print('White list:' + str(admin_filter))
print('Server bind on %s:%s' % (local_ip, str(local_port)))
print('-----------------Server starting success-----------------')

""" 機台類型     路徑                           判斷檔案
    Printer	    E:/Config	                  EVENT.DAT
    SPI	        D:/Tester_Data_bk/料號/日期	   日期+時間.dat (例：20181018140229_355045.dat)
    Mounter	    無機台原生LOG可以判斷
    AOI	        X:\年\月 (X為網路磁碟機)        日期.log (例: 20191120.log)
    Reflow	    C:\oven\Journal File          日期 data.txt (例: Aug 07 2018 data.txt)
"""


def Doperate(conn, command):
    ret = list()
    y = time.strftime("%Y", time.localtime())
    m = time.strftime("%m", time.localtime())
    d = time.strftime("%d", time.localtime())
    b = time.strftime("%b", time.localtime())
    
    t = time.strftime("%H%M%S", time.localtime())
    if command == '"AOI_Operate"':
        my_file = os.path.join('x:\\', y, m, y+m+'.log')
    elif command == '"SPI_Operate"':
        my_file = os.path.join('D:\\Tester_Data_bk\\',
                               'data', y+m+d+'_'+t+'.dat')
    elif command == '"Printer_Operate"':
        my_file = os.path.join('e:/config/EVENT.DAT')
    elif command == '"Reflow_Operate"':
        my_file = os.path.join('d:\\oven\\Journal File', b+' '+d+' '+y+' data.txt')
    else:
        my_file = os.path.join('d:\\oven\\Journal File', y+m+d+'data.txt')

    try:
        file = open(my_file, 'r')
        ret.append('data path change')
        conn.send(pickle.dumps(ret))
        return True
    except FileNotFoundError:
        ret.append('device stop')
        conn.send(pickle.dumps(ret))
        return False


""" Check Process Operate
    Check Process Operate
    Check Process Operate
"""
def Check_Process(conn):
    ### subprocess - 執行powershell檔案
    ret = list()
    POWERSHELL = "%SystemRoot%\system32\WindowsPowerShell\\v1.0\\powershell.exe"
    monitor = subprocess.run('POWERSHELL "get-process -name *monitor | Format-Wide"',
                          shell=True, stdout=subprocess.PIPE)
    if monitor.stdout != b'':
        ret.append('monitor')
    collector = subprocess.run(
        'POWERSHELL "get-process -name *collector | Format-Wide"', shell=True, stdout=subprocess.PIPE)
    if collector.stdout != b'':
        ret.append('collector')
    wsgi = subprocess.run(
        'POWERSHELL "get-process -name *wsgi | Format-Wide"', shell=True, stdout=subprocess.PIPE)
    if wsgi.stdout != b'':
        ret.append('wsgi')
    print(ret)
    if ret == []:
        ret = ['No process']
    conn.send(pickle.dumps(ret))


def Check_Raspberry(conn):
    ret = list()
    my_file = os.path.join('d:/smt/exe/pre.txt')
    try:
        file = open(my_file, 'r')
        file_stamp = os.path.getmtime(my_file)
        current = time.time()
        if (current - file_stamp) < 3600:
            ret.append('work')
        else:
            ret.append('stop')
        conn.send(pickle.dumps(ret))
        return True
    except FileNotFoundError:
        ret.append('pre.txt not found')
        conn.send(pickle.dumps(ret))
        return False


def main():
    while True:
        conn, addr = server.accept()
        command = urllib.parse.unquote(conn.recv(1024).decode('utf-8'))

        peer_name = conn.getpeername()
        sock_name = conn.getsockname()

        # peer_name是個tuple，peer_name[0]是ip，peer_name[1]是埠號
        now_dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(u'%s, From %s:%s' %
              (now_dt, peer_name[0], peer_name[1]))  # , sock_name
        # 白名單，管理員許可權驗證
        # print(peer_name[0])
        # if peer_name[0] in admin_filter:
        if True:
            print(command)

            if command == '"cancel"':
                conn.send(pickle.dumps(['None']))
            elif command == '"Process_Operate"':
                Check_Process(conn)
            elif command in ['"AOI_Operate"', '"SPI_Operate"', '"Printer_Operate"', '"Reflow_Operate"', '"Mounter_Operate"']:
                Doperate(conn, command)
            elif command == '"Raspberry"':
                Check_Raspberry(conn)
            else:
                command == '"quit"'
                conn.send(pickle.dumps(['Quit']))
                conn.close()
                exit(0)

            # if command == '"start server"'
            #     t = threading.Thread(target=exe_prog,args=(command,))
            #     t.start()

        #conn.send('server: I received '+command)


if __name__ == '__main__':
    main()
