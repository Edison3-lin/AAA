#-*- coding: utf-8 -*-

import socket
from urllib import parse
import pickle

# # 创建tcp socket
# tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # 目的信息
# server_ip = input("请输入服务器ip:")
# server_port = int(input("请输入服务器port:"))

# # 链接服务器
# tcp_client_socket.connect((server_ip, server_port))

# # 提示用户输入数据
# send_data = input("请输入要发送的数据：")

# tcp_client_socket.send(send_data.encode("gbk"))

# # 接收对方发送过来的数据，最大接收1024个字节
# recvData = tcp_client_socket.recv(1024)
# print('接收到的数据为:', recvData.decode('gbk'))

# # 关闭套接字
# tcp_client_socket.close()


def send_cmd(instr):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('172.20.10.3', 8388))
        client.settimeout(5)
        client.sendall(parse.quote(instr).encode('utf-8'))
        while True:
            recv_data = pickle.loads(client.recv(4096))
            # recv_data = client.recv(1024)
            if recv_data:
                print(recv_data)
                break
        
    except Exception as e:
        print(e)
    finally:
        client.close()


msg = b'"quit"'
# msg = b"d:\\x.bat"
send_cmd(msg)



