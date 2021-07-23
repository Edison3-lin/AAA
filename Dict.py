### 字典轉換成list再寫入檔案
import os
data = os.environ
# with open('os.txt',mode='w') as f:
    # for key, value in list(data.items()):
    #     f.write(key+': '+value+'\n')
for i in data.items():
   print(i)