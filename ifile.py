﻿import codecs
import datetime
import json
import os
import pickle
import socket
import subprocess
import time
from urllib import parse

import requests

# file=open("data.txt", mode="w")
# file.write("25172新北市淡水區新市二路三段172巷17號8F")
# file.write("\n25172新北市淡水區新市二路三段172巷17號8F")
# file.write("\n25172新北市淡水區新市二路三段172巷17號8F")
# file.write("\n25172新北市淡水區新市二路三段172巷17號8F")
# file.close()

# 寫入讀取檔案內容
# with open("data.txt", mode="w") as file:
#     file.write("屏東縣恆春鎮恆公路970巷3弄15號\n")
#     file.write("台北市北投區立德路150號（分機31113）\n")
#     file.write("林宏斌\n")
# with open("data.txt", mode="r") as file:
#         data=file.read()
# print(data)

# 讀取檔案內容作總和
# sum=0
# with open("data.txt", mode='r') as file:
#     for line in file:
#         sum+=int(line)
# print(sum)

# JSON格式讀取
# with open("edison.json", mode="w") as file:
#     file.write("{\n")
#     file.write("    \"name\":\"Edison Lin\",\n")
#     file.write("    \"id\":\"T122228027\",\n")
#     file.write("    \"work\":\"2222\"\n")
#     file.write("}\n")
# import json
# with open("edison.json", mode="r") as file:
#     data=json.load(file)
# print(data,"\n")
# print("\n姓名  ： ", data["name"])
# print("\n證件號： ", data["id"])
# print("\n公司名： ", data["work"])

# 隨機選取
# import random
# data1 = random.choice([1,2,3,4,5,6,7,8,9])
# data2 = random.sample([1,2,3,4,5,6,7,8,9], 4)
# data3 = [1,2,3,4,5,6,7,8,9]
# random.shuffle(data3)
# print(data1,"\n", data2,"\n",data3,"\n")
# data1 = random.random()
# data2 = random.normalvariate(80, 5)
# data3 = random.uniform(100,110)
# print(data1,"\n", data2,"\n",data3,"\n")

# 網路連線
# import urllib.request as request
# import json
# src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=c32998fa-c9b2-4324-9016-e19fbe0815f1"
# with request.urlopen(src) as response:
#     data = json.load(response)
# data1 = data["result"]["results"]
# # print(data1)
# with open("mrt.txt", mode="w") as file:
#     for data2 in data1:
#         file.write(data2["stationA"]+" - "+data2["stationB"]+"\n")

# 定義class
# class IO:
#     Support = ["console", "file"]
#     def read(src):
#         if src not in IO.Support:
#             print(src,"Not support")
#         else:
#             print("read from", src)
# IO.read("file")
# IO.read("xxx")

# 定義實體物件
# class Point:
#     def __init__(self, x, y, z):
#         self.x = x * 2
#         self.y = y * 3
#         self.z = z + ' Edison'
# p =  Point(1, 5, "lin" )
# print(p.x, p.y, p.z)

# FullName 實體物件設計：  分開記錄
# class FullName:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = " " + last
# name1 = FullName("Edison", "Lin")
# name2 = FullName("Grace", "Lin")
# name3 = FullName("K.K", "Peng")
# name4 = FullName("Allen", "Tu")
# print(name1.first + name1.last)
# print(name2.first + name1.last)
# print(name3.first + name1.last)
# print(name4.first + name1.last)

# Point 實體物件設計：  Instance Methods
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(self.x, self.y)
#     def distance(self, xx, yy):
#         self.x = xx
#         self.y = yy
#         return(self.x**2 + self.y**2)

# P = Point(3, 4)
# r = P.distance(10, 20)
# print(type(P))
# P.show()

# File 實體物件設計：  包裝檔案讀取
# class File:
#     def __init__(self, name):
#         self.name = name
#         self.file = None #空的檔案
#     def open(self):
#         self.file = open(self.name, mode="r", encoding="utf-8")
#     def read(self):
#         return self.file.read()
# f1 = File("mrt.txt")
# f1.open()
# data = f1.read()
# print(data)

# 抓取PTT電影版網頁原始碼
# import urllib.request as req
# url = "https://www.ptt.cc/bbs/movie/index.html"
# request = req.Request(url, headers={
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")
# # print(data)
# import bs4
# root = bs4.BeautifulSoup(data, "html.parser")
# titles = root.find_all("div", class_="title")
# for t in titles:
#     if t.a != None:
#         print(t.a.string)

# Cookie 操作實務
# 抓取PTT八卦版網頁原始碼
# import urllib.request as req
# def GetUrl(url):
#     # url = "https://www.ptt.cc/bbs/Gossiping/index.html"
#     request = req.Request(url, headers={
#         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122     Safari/537.36",
#         "cookie":"over18=1"
#     })
#     with req.urlopen(request) as response:
#         data = response.read().decode("utf-8")
#     # print(data)
#     import bs4
#     root = bs4.BeautifulSoup(data, "html.parser")
#     titles = root.find_all("div", class_="title")
#     for t in titles:
#         if t.a != None:
#             print(t.a.string)
#     nextlink = root.find("a", string = "‹ 上頁")    #上頁的網址
#     return nextlink["href"]

# Page = 0
# UrlPage = "https://www.ptt.cc/bbs/MobileComm/index.html"
# while (Page < 3):
#     UrlPage = "https://www.ptt.cc/" + GetUrl(UrlPage)
#     Page += 1

# Edison
# import os
# import sys
# sys.path.append("d://VPL//xxx//libs")

# import time
# import socket
# import subprocess
# from sysutils import ConfigParse, MongodbOperator, FileOperator

# SupportFunc = [
#     'powerdc', 'speed2000', 'allegro', "sipi_allegro", "orcad", "ddr",
#     "powersi", "opi"
# ]
# scriptPath = os.path.dirname(os.path.abspath(__file__))
# POWERSHELL = "%SystemRoot%\system32\WindowsPowerShell\\v1.0\\powershell.exe"
# mainPsPath = os.path.abspath(os.path.join(scriptPath, "test.ps1"))
# main1PsPath = os.path.abspath(os.path.join(scriptPath, "test1.ps1"))
# UPDATE_INTERVAL = 600
# UPDATE_STATUS_COLLECTION = "app_server_info"


# class appServer(MongodbOperator):

#     def __init__(self):
#         MongodbOperator.__init__(self)

#     def check_other_servers(self, job_type):
#         print("check_other_servers")
#         return self.db_check_other_servers(UPDATE_STATUS_COLLECTION, socket.gethostname(), job_type)

#     def update_staus(self, job_type):
#         print("update_staus")
#         self.db_update_server_status(UPDATE_STATUS_COLLECTION, socket.gethostname(), job_type)
#         return

# # a = sys.argv
# # b = len(sys.argv)
# # c = len(sys.argv[2:])

# if(len(sys.argv[1:]) < 1):
#     print("You need input function. ex: powerdc, speed2000, allegro, sipi_allegro, orcad, ddr, powersi,opi")
#     sys.exit(0)
# for arg in sys.argv[1:]:
#     unsupportFunc = True
#     # print("AAAA")
#     for func in SupportFunc:
#         # print("bbbb")
#         if arg == func:
#             # print("CCC")
#             unsupportFunc = False
#     if unsupportFunc == True:
#         print("Function", arg, "is unsupported.")
#         sys.exit(0)
#     # print(arg)

# arguments = ' '.join(sys.argv[1:])
# print(sys.path)
# pro = subprocess.Popen([POWERSHELL, "-File", mainPsPath, "None", arguments], shell=True)
# while True:
#     appServer().update_staus(arguments)
#     backServer, type = appServer().check_other_servers(arguments)
#     if backServer != "None":
#         subprocess.Popen(
#             [POWERSHELL, "-File", main1PsPath, "Error", backServer, type],
#             shell=True)
#         if type == "speed2000":
#             continue
#         print("start to backup")
#         print(backServer, type)
#         subprocess.Popen([POWERSHELL, "-File", mainPsPath, backServer, type], shell=True)
#     time.sleep(UPDATE_INTERVAL)

# import win32com
# import win32gui
# import win32con
# import win32api
# win32api.MessageBox(0, "xxxx", 'Desktop creation failed')

# a=3
# b=2

# try:
#     if a<b :
#         print(n)
# except:
#     print("except")
# else:
#     print("esle")

#!/usr/bin/python
# -*- coding: UTF-8 -*-
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Ediosn test
# import os
# import sys
# FILE_INFO           = 'kobosetup.exe'
# class EstimateTime:
#     def __init__(self, brd_info="d://backup//.info"):
#         self.FILE_INPUT = brd_info
#         self.prefix_file = os.path.dirname(os.path.abspath(self.FILE_INPUT))
#         self.FILEPATH_INFO = os.path.join(self.prefix_file, FILE_INFO)
#         spd_file = os.path.join(self.prefix_file, FILE_INFO)
#         self.spd_size = os.path.getsize(spd_file)

# f = EstimateTime()
# print(f.prefix_file, end='')
# print(f.FILEPATH_INFO)
# print(f.spd_size)
# print('%s%s Edison Address: ' % (f.spd_size, f.FILEPATH_INFO))

# try:
#     a = 1/1
#     raise BaseException("111")
# except ZeroDivisionError:
#     print("Dived by zero")
# except:
#     print("Lin")

# for i in print.__doc__.split("\n"):
#     print(i)

# import csv
# import os
# import sys
# import json
# FILE_INPUT_SIM_CSV = 'sim_item.csv'

# def parse_file(f, l=True):
#     if os.path.exists(f):
#         with open(f) as fin:
#             if l == True:
#                 return fin.read().splitlines()
#             elif l == 'json':
#                 return json.load(fin)
#             else:
#                 return fin.read()
#     else:
#         return None

# # 開啟 CSV 檔案
# # with open(FILE_INPUT_SIM_CSV, newline='') as fin:
# #     x = csv.reader(fin)
# #     for y in x:
# #         z = y.split('\t')
# #         print(z)


# type_info = parse_file(FILE_INPUT_SIM_CSV)
# # print(len(type_info))
# for x in type_info:
#     for y in x.split('\t'):
#         print(y)
# print(type_info[0].split('\t')[1])

# for x in range(0, len(type_info)):
#     tmp_type = type_info[x].split('\t')
#     print(tmp_type)

# with open('sim_item.csv', newline='') as csvfile:
#   # 讀取 CSV 檔案內容
#   rows = csv.reader(csvfile)

#   # 以迴圈輸出每一列
#   for row in rows:
#     print(row)


# import os
# import sys

# iplist = list()
# ip = '12.0.0.2'
# # ip = '172.24.186.191'
# # ip = 'www.baidu.com'
# backinfo = os.system('ping -c 1 -w 1 %s'%ip) # 實現pingIP地址的功能，-c1指傳送報文一次，-w1指等待1秒
# if backinfo:
#  print('no')
# else:
#  iplist.append(ip)
# print(iplist)


# a = "2020-10-10 23:40:00"
# #將其轉換為時間數組
# import time

# timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
# # 轉換為時間戳:
# timeStamp = int(time.mktime(timeArray))
# print(timeStamp)

# 修改JSON檔的資料
# import json
# import codecs
# with open("edison.json", mode="r") as file:
#     data=json.load(file)
# data["name"] = "Edison"
# data["id"] = "T12222xxx"
# print(data)

# with codecs.open("edison.json", "w", "utf-8") as fout:
#     json.dump(data, fout, indent=4, sort_keys=True)


# with open('os.txt', 'r') as f:
#     a = f.readlines()
#     for d in a:
#         if 'start time' in d:
#             b = d.strip('\n')
#             e = b.split(' ')
#             i = 0
#             for f in e:
#                 if f == 'time':
#                     t_str = e[i+1]+' '+e[i+2]
#                 i += 1
#             print(t_str)

# # t_str="2020-09-10 12:01:20"
# a = time.strptime(t_str, "%Y-%m-%d %H:%M:%S")
# c = time.mktime(a)
# d = datetime.datetime.fromtimestamp(c)
# print(d)


# import optparse, time
# from qpid.messaging import *
# from qpid.util import URL
# from qpid.log import enable, DEBUG, WARN
# def nameval(st):
# idx = st.find("=")
# if idx >= 0:
# name = st[0:idx]
# value = st[idx+1:]
# else:
# name = st
# value = None
# return name, value
# parser = optparse.OptionParser(usage="usage: %prog [options] ADDRESS [ CONTENT ... ]",
# description="Send messages to the supplied address.")
# parser.add_option("-b", "--broker", default="localhost",
# help="connect to specified BROKER (default %default)")
# parser.add_option("-r", "--reconnect", action="store_true",
# help="enable auto reconnect")
# parser.add_option("-i", "--reconnect-interval", type="float", default=3,
# help="interval between reconnect attempts")
# parser.add_option("-l", "--reconnect-limit", type="int",
# help="maximum number of reconnect attempts")
# parser.add_option("-c", "--count", type="int", default=1,
# help="stop after count messages have been sent, zero disables (default %default)")
# parser.add_option("-t", "--timeout", type="float", default=None,
# help="exit after the specified time")
# parser.add_option("-I", "--id", help="use the supplied id instead of generating one")
# parser.add_option("-S", "--subject", help="specify a subject")
# parser.add_option("-R", "--reply-to", help="specify reply-to address")
# parser.add_option("-P", "--property", dest="properties", action="append", default=[],
# metavar="NAME=VALUE", help="specify message property")
# parser.add_option("-M", "--map", dest="entries", action="append", default=[],
# metavar="KEY=VALUE",
# help="specify map entry for message body")
# parser.add_option("-v", dest="verbose", action="store_true",
# help="enable logging")
# opts, args = parser.parse_args()
# if opts.verbose:
# enable("qpid", DEBUG)
# else:
# enable("qpid", WARN)
# if opts.id is None:
# spout_id = str(uuid4())
# else:
# spout_id = opts.id
# if args:
# addr = args.pop(0)
# else:
# parser.error("address is required")
# content = None
# if args:
# text = " ".join(args)
# else:
# text = None
# if opts.entries:
# content = {}
# if text:
# content["text"] = text
# for e in opts.entries:
# name, val = nameval(e)
# content[name] = val
# else:
# content = text
# conn = Connection(opts.broker,
# reconnect=opts.reconnect,
# reconnect_interval=opts.reconnect_interval,
# reconnect_limit=opts.reconnect_limit)
# try:
# conn.open()
# ssn = conn.session()
# snd = ssn.sender(addr)
# count = 0
# start = time.time()
# while (opts.count == 0 or count < opts.count) and \
# (opts.timeout is None or time.time() - start < opts.timeout):
# msg = Message(subject=opts.subject,
# reply_to=opts.reply_to,
# content=content)
# msg.properties["spout-id"] = "%s:%s" % (spout_id, count)
# for p in opts.properties:
# name, val = nameval(p)
# msg.properties[name] = val
# snd.send(msg)
# count += 1
# print msg
# except SendError, e:
# print e
# except KeyboardInterrupt:
# pass
# conn.close()


# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# email_list = {  '1122':['edison3.lin@gmail.com','edisonlin.hojac@gmail.com'],
#                 '1133':'b82506001@gmail.com',
#                 '1144':['edisonlin.hojac@gmail.com','b82506001@gmail.com'],
#                 '1155':['pega.edison@gmail.com','edisonlin.hojac@gmail.com']
#              }

# content = MIMEMultipart()  #建立MIMEMultipart物件
# content["subject"] = "tttt"  #郵件標題
# content["from"] = "edison3.lin@gmail.com"  #寄件者
# # content["to"] = "b82506001@gmail.com".join(',pega.edison@gmail.com') #收件者
# a = []
# for i,j in email_list.items():
#     if i == '1166':
#         if type(j) != list:
#             a.append(j)
#         else:
#             a = j
# print(a)
# b = ",".join(a)
# print(b)
# content["to"] = b
# content.attach(MIMEText("seems unworkable"))  #郵件內容
# import smtplib
# with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
#     try:
#         smtp.ehlo()  # 驗證SMTP伺服器
#         smtp.starttls()  # 建立加密傳輸
#         smtp.login("edison3.lin@gmail.com", "nhgw qgvw aszm fdmd")  # 登入寄件者gmail
#         smtp.send_message(content)  # 寄送郵件
#         print("Complete!")
#     except Exception as e:
#         print("Error message: ", e)


# 用途：操作oracle数据库demo
# import cx_Oracle
# # user = "smtuser"
# # passwd = "pega#1234"
# # listener = '10.255.70.36:1521'
# user = "SYSDBA"
# passwd = "2goixdxi"
# listener = "localhost:1521/XEPDB1"

# # Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
# db = cx_Oracle.connect("system/2goixdxi@//localhost:1521/XEPDB1")
# cur = db.cursor()

# # SQL 插入语句
# # cur.execute("grant create view to sys")
# # cur.execute("INSERT INTO SYS.EQUIP_INFO$ VALUES (:VENDOR, \
# #        :EQUIP_TYPE, :DEV_ID, :DEV_IP, :DEV_MAC, :FACTORY, :LINE)", \
# #        ['9999','PRINT','5556','168.95.0.3','0C-9D-93-32-DC-9A','LD3','alive'])

# cur.execute("SELECT * FROM SYS.EQUIP_INFO$")
# res = cur.fetchall()
# print(res)

# # # 关闭数据库连接
# db.close()

# import iFactory.email as email

# email_list = {  '1122':['edison3.lin@gmail.com','edisonlin.hojac@gmail.com','b82506001@yahoo.com.tw','edison3.lin@hotmail.com.tw'],
#                 '1133':'b82506001@gmail.com',
#                 '1144':['edisonlin.hojac@gmail.com','b82506001@gmail.com'],
#                 '1155':['pega.edison@gmail.com','edisonlin.hojac@gmail.com']
#              }

# email.send(email_list['1122'])

# y = time.strftime("%Y", time.localtime())
# m = time.strftime("%m", time.localtime())
# d = time.strftime("%d", time.localtime())
# t = time.strftime("%H%M%S", time.localtime())
# # my_file = os.path.join('x:\\',y,m,y+m+'.log')
# my_file = os.path.join('d:\\oven\\Journal File', y+m+d+'data.txt')
# try:
#     file = open(my_file, 'r')
# except:
#     print('xxx')
# t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# a = "2020-09-19 12:00:00"
# b = time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S"))
# c = time.time()
# t = c-b
# Sday = 60*60*24
# Shour = 60*60
# Smin = 60

# Dday = int(t // Sday)
# t1 = t % Sday
# Dhour = (t1 // Shour)
# t2 = t1 % Shour
# Dmin = (t2 // Smin)
# Dsec = t2 % Smin


# print("%d %d %d %d" % (Dday, Dhour, Dmin, Dsec))

LINE = subprocess.run('"POWERSHELL "get-process -name *LINE | Format-Wide"',
                          shell=True, stdout=subprocess.PIPE)
if LINE.returncode == 0:
    print('xxxx')    
else:    
    print('ttt')    
    
    
    
    
