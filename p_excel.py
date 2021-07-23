# import os
# import sys
# import win32com.client
# from PIL import ImageGrab

# try:
#     win32com.client.DispatchEx('Excel.Application')
# except:
#     raise OSError('xxxx')    

# # 导入模块
# import win32com
# from win32com.client import *
# # 新建一个基于COM对象的应用
# xlApp = win32com.client.Dispatch("Outlook.Application")
# # 设置应用可见
# # xlApp.Visible = True
# # # 新增一个工作簿
# # xlBook = xlApp.Workbooks.Add()
# # # 保存并关闭工作簿
# # xlBook.SaveAs("E:\\text.xls")
# # xlBook.Close()
# # # 打开已有的应用
# # xlBook = xlApp.Workbooks.Open("E:\\text.xls")
# # 不保存，直接退出
# # xlBook.Close(SaveChanges=0)
# # # 关闭应用
# # xlApp.Quit()


from win32com.client import gencache
shell = gencache.EnsureDispatch('Excel.Application')
print(shell)


