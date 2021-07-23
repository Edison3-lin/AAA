# file=open("data.txt", mode="w")
# file.write("25172新北市淡水區新市二路三段172巷17號8F")
# file.write("\n25172新北市淡水區新市二路三段172巷17號8F")
# file.write("\n25172新北市淡水區新市二路三段172巷17號8F")
# file.write("\n25172新北市淡水區新市二路三段172巷17號8F")
# file.close()

#寫入讀取檔案內容
# with open("data.txt", mode="w") as file:
#     file.write("屏東縣恆春鎮恆公路970巷3弄15號\n")
#     file.write("台北市北投區立德路150號（分機31113）\n")
#     file.write("林宏斌\n")
# with open("data.txt", mode="r") as file:
#         data=file.read()
# print(data)

#讀取檔案內容作總和
# sum=0
# with open("data.txt", mode='r') as file:
#     for line in file:
#         sum+=int(line)
# print(sum)

#JSON格式讀取
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

#修改JSON檔的資料
# import json
# import codecs
# with open("edison.json", mode="r") as file:
#     data=json.load(file)
# data["name"] = "Edison"
# data["id"] = "T12222xxx"
# print(data)

# with codecs.open("edison.json", "w", "utf-8") as fout:
#     json.dump(data, fout, indent=4, sort_keys=True)

# with open("edison.json", mode="w") as file:
#     json.dump(data, file)

#隨機選取
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

#網路連線
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

#定義class
# class IO:
#     Support = ["console", "file"]
#     def read(src):
#         if src not in IO.Support:
#             print(src,"Not support")
#         else:
#             print("read from", src)
# IO.read("file")
# IO.read("xxx")

#定義實體物件
# class Point:
#     def __init__(self, x, y, z):
#         self.x = x * 2
#         self.y = y * 3
#         self.z = z + ' Edison'
# p =  Point(1, 5, "lin" )
# print(p.x, p.y, p.z)

#FullName 實體物件設計：  分開記錄
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

#Point 實體物件設計：  Instance Methods
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

#File 實體物件設計：  包裝檔案讀取
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

#抓取PTT電影版網頁原始碼
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

#Cookie 操作實務
#抓取PTT八卦版網頁原始碼
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

#Edison
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

#Ediosn test
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


import os
import time
import datetime
#獲取檔案的建立時間
file ="d:\smt\exe\pre.txt"
timestamp = os.path.getmtime(file)
t2 = 1599644999.2996607
print(timestamp)
print(time.localtime(timestamp))
print(time.time())
# print(datetime.datetime.fromtimestamp(timestamp))
# print(datetime.date.fromtimestamp(timestamp))
# print(time.gmtime(os.path.getmtime(file)))
