import wmi
import os
import subprocess

### os - 擷取系統環境變數
s = subprocess.Popen("python", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
s.stdin.write(b"import os\n")
s.stdin.write(b"print(os.environ)")
s.stdin.close()

out = s.stdout.read().decode("utf-8")
s.stdout.close()
print(out)

### wmi - 察看正在運行的process
c = wmi.WMI()    
wql = "SELECT * FROM Win32_Service WHERE State = 'Running'"
for x in c.query(wql):
    print(x.ProcessId)
    print(x.DisplayName)


### subprocess - 執行powershell檔案
POWERSHELL = "%SystemRoot%\system32\WindowsPowerShell\\v1.0\\powershell.exe"

p = subprocess.Popen([POWERSHELL,"-File","1.ps1"], shell=True) 
# p=subprocess.run([POWERSHELL,"-File","1.ps1"], shell=True) 
# p=subprocess.run("dir d:\\", shell=True, stdout=subprocess.PIPE) 
# p=subprocess.Popen("dir /w d:\\", shell=True) 
a = p.wait() 
if(p.stdout):
    print(p.stdout)
else:
    print('ttt')    