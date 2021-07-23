import codecs
import datetime
import json
import os
import pickle
import socket
import subprocess
import time
from urllib import parse

import requests
import sys

# y = time.strftime("%Y", time.localtime())
# m = time.strftime("%m", time.localtime())
# d = time.strftime("%d", time.localtime())
# b = time.strftime("%b", time.localtime())
# print('%s  %s   %s   %s'%(y,m,d,b))    
# print(time.strftime("%Y %m %d %H %M %S", time.localtime()))

# from win32com import *
# import pythoncom
# import win32com.client as win32
# def execute_excel(input_excel):
#     '''execute_excel Edison

#     Arguments:
#         input_excel {stfing} -- Edison
#     '''
#     if input_excel is not None:
#         pythoncom.CoInitialize()
#         excel = win32.DispatchEx('Excel.Application')
#         excel.Visible = 1
#         excel.DisplayAlerts = 1
#         wb1 = excel.Workbooks.Open(input_excel)
#         ws1 = excel.ActiveSheet
#         # ws1.EnableCalculation = True
#         # ws1.Calculate()
#         # wb1.Save()
#         # wb1.Close(True)
#         # if excel:
#         excel.Quit()
# execute_excel('d:\\Job\\1.xlsx')
# print(execute_excel.__get__)

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
# P.show()

# r = P.distance(10, 20)
# # print(type(P))
# print(r)
# P.show()



# class Animal:
#     def __init__(self, x, y):
#         self.name = x
#         self.nickname = y

#     def eat(self):
#         print("吃")
        
#     def drink(self):
#         print("喝")
        
#     def sleep(self):
#         print("睡")                
        
#     def __str__(self):
#         return "%s %s 是動物的名字" % (self.name, self.nickname)
        
# class dog(Animal):
#     def bark(self):
#         print("汪汪")        
        
# class sdog(dog):
#     def bark(self):
#         super().sleep()
#         print("神一樣的汪汪")            
        
        
        
# edison = Animal("林宏斌", "帥哥")
# print(edison)
# a = dog("grace", "lin")        
# a.eat()
# a.drink()   
# a.sleep()
# a.bark()

# b = sdog("edison", "xxx")
# b.eat()
# b.drink()   
# b.sleep()
# b.bark()     
        
        
POWERSHELL = "%SystemRoot%\system32\WindowsPowerShell\\v1.0\\powershell.exe"
monitor = subprocess.Popen([POWERSHELL, "-File", ".\\1.ps1"], shell=True)
# print(monitor.returncode)
# monitor.wait()




