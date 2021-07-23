import subprocess

def Exec_cmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return p.communicate()

_out, _err = Exec_cmd("dir {url}.{input}".format(url="1", input="py"))

is_up = subprocess.Popen("dir 1.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
# a = is_up.stdout.replace('\xef\xbb\xbf', '')
# a = is_up.stdout
# a.pop(0)
print(is_up.communicate()[0])