import socket

def main():
    # 創建TCP套接字
    TCP_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 連接Server
    TCP_socket.connect(("172.20.10.3", 8080))
    while True:
        # dest_ip = input("輸入對方ip: ")
        # dest_port = int(input("輸入對方port: "))
        # send_data = input("請輸入資料: ")
        send_data = "EDISON: "
        TCP_socket.send(send_data.encode("utf-8"))
        # TCP_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

        recv_data, addr = TCP_socket.recvfrom(100)
        if recv_data == b'exit':
            break

        print("%s" % (recv_data.decode(encoding='utf-8')))



    TCP_socket.close()

    # HOST = '172.20.10.3'
    # PORT = 8080

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((HOST, PORT))

    # while True:
    #     cmd = raw_input("Please input msg:")
    #     s.send(cmd)
    #     data = s.recv(1024)
    #     print("server send : %s " % (data))


if __name__ == "__main__":
    main()