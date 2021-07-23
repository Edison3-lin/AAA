import os
import sys
# import winrm
import subprocess
import win32con
import wmi
import json
import codecs
import pymongo
from mongoengine import *



###第一种方式
# from mongoengine import connect
#     connect('project1')  #project1为你要连接的数据库的名称

###第二种方式
#如果mongo服务是在其他地方运行，可以使用这种方法
    # from mongoengine import connect
    # connect （'project1' ， host = '192.168.1.35' ， port = 12345 ）

###第三种方式
#如果数据库需要身份验证，username并password 应提供的参数
    # from mongoengine import connect
    # connect （'project1' ， username = 'webapp' ， password = 'pwd123' ）


###第四种方式（推荐）
#URI样式连接也被支持 - 只需提供URI作为host：
    # from mongoengine import connect
    # connect （'project1' ， host = 'mongodb：// localhost / database_name' ）


# def eq_insert_one(user_data):



def ping_ip(dev_ip):
    is_up = subprocess.run("ping -n 1 -w 1 -c 1 %s" % dev_ip, shell=True, stdout=subprocess.PIPE) 
    return False if is_up.returncode else True

      
class User(Document):
      uid = SequenceField(primary_key=True)
      vendor = StringField(max_length=20)
      equip_type = StringField(max_length=20)
      dev_id = StringField(max_length=50)
      dev_ip = StringField(max_length=45)
      dev_mac = StringField(max_length=17)
      factory = StringField(max_length=20)
      line = StringField(max_length=20)

      
# myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# my = connect('Edison') 
# connect('DB1', host='127.0.0.1', port=27017)
connect('DB1', host='mongodb://localhost')

# dblist = myclient.list_database_names()
equip_info = (
  { 'vendor':'8086','equip_type':'Print','dev_id':'1122','dev_ip':'127.0.0.1','dev_mac':'0C-9D-92-32-DC-9A','factory':'aaa','line':'alive'},
  { 'vendor':'8186','equip_type':'SPI','dev_id':'1321','dev_ip':'17.0.110.2','dev_mac':'CE-08-8D-4C-4F-E6','factory':'ccc','line':'alive'},
  { 'vendor':'8186','equip_type':'Reflow','dev_id':'1622','dev_ip':'17.0.110.2','dev_mac':'CE-08-8D-4C-4F-E6','factory':'ccc','line':'alive'},
  { 'vendor':'8186','equip_type':'Mounter','dev_id':'1822','dev_ip':'17.0.110.2','dev_mac':'CE-08-8D-4C-4F-E6','factory':'ccc','line':'alive'},
  { 'vendor':'8286','equip_type':'Mounter','dev_id':'1529','dev_ip':'127.0.0.1','dev_mac':'CE-08-8D-42-4F-E6','factory':'aaa','line':'alive'},
  { 'vendor':'8185','equip_type':'AOI','dev_id':'1328','dev_ip':'17.0.110.2','dev_mac':'CE-08-8D-4C-4F-E6','factory':'ccc','line':'alive'},
  { 'vendor':'8185','equip_type':'SPI','dev_id':'1322','dev_ip':'17.0.110.2','dev_mac':'CE-08-8D-4C-4F-E6','factory':'ccc','line':'alive'},
  { 'vendor':'8185','equip_type':'Print','dev_id':'1552','dev_ip':'17.0.110.2','dev_mac':'CE-08-8D-4C-4F-E6','factory':'ccc','line':'alive'},
  { 'vendor':'8185','equip_type':'Reflow','dev_id':'1442','dev_ip':'17.0.110.2','dev_mac':'CE-08-8D-4C-4F-E6','factory':'ccc','line':'alive'}
)

ep_insert = [
  { 'vendor':'8086','equip_type':'555','dev_id':'9122','dev_ip':'127.0.0.1','dev_mac':'0C-9D-92-32-DC-9A','factory':'aaa','line':'alive'},
  { 'vendor':'8186','equip_type':'666','dev_id':'9322','dev_ip':'17.0.110.2','dev_mac':'CE-08-8D-4C-4F-E6','factory':'ccc','line':'alive'},
  { 'vendor':'8286','equip_type':'777','dev_id':'9512','dev_ip':'127.0.0.1','dev_mac':'CE-08-8D-42-4F-E6','factory':'aaa','line':'alive'},
]


# if(equip_info):
#   for user_data in equip_info:
#     User(**user_data).save()

# if(ep_insert):
#   for a in ep_insert:
#     if(User.objects(dev_id__exact=a['dev_id'])):
#       User.objects()
#     else:
#       User(**a).save()  
i = 0
for u in User.objects:
    i += 1  
    if u.dev_id == '9999':
      u.update(line = 'eee'  )
      v = u
      print(i)
v.reload()      
print(v.line)      
# u.update()
# print(u)
# print(u.vendor)
# intel = User.objects(vendor='8086')
# for i in intel:
#       print(i.dev_id)
      
# w = wmi.WMI()
# cpu_list = w.Win32_Processor()
# for cpu in cpu_list:
#     print("cpu核心數",cpu.NumberOfCores)
#     print("cpu型號",cpu.Name)

# import platform 
# import time 
# for sys in w.Win32_OperatingSystem(): 
#   print("Version:%s" % sys.Caption.encode("UTF-8"))
#   print(sys.OSArchitecture.encode("UTF-8")) #系統是位還是位的 
#   print(sys.NumberOfProcesses) #當前系統執行的程序總數
      
# iplist = list()
# epstatuslist = list()

# with codecs.open("ep.json", "r", "utf-8") as file:
#   data=json.load(file)
# d = {
#     "dev_id": "",
#     "status": ""
# }  
# with codecs.open("ep.json", "a", "utf-8") as s:
#   # json.dump(iplist, s, indent=4, sort_keys=True)
#   for i in User.objects:
#     d["dev_id"] = i.dev_id
#     # 實現pingIP地址的功能，-c1指傳送報文一次，-w1指等待1秒 
#     ip = i.dev_ip  
#     backinfo = os.system('ping -c 1 -w 1 -n 1 %s' % ip)
#     if backinfo:
#       d['status'] = '_Stop_'
#     else:
#       d['status'] = '_Line_'
    
#     epstatuslist.append({d['dev_id'],d['status']})
#     print(epstatuslist)
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


