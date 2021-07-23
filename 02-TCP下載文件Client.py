import socket

def main():
    # 創建TCP套接字
    TCP_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 連接Server
    TCP_socket.connect(("172.20.10.3", 8888))

    # dest_ip = input("輸入對方ip: ")
    # dest_port = int(input("輸入對方port: "))
    # send_data = input("請輸入資料: ")
    file_name = input("請輸入下載檔案名稱：")
    send_data = file_name.encode("utf-8")
    TCP_socket.send(send_data)
    # TCP_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))
    while True:
        recv_data = TCP_socket.recv(1024*1024)
        if recv_data:
            try:
                with open("[new]"+file_name, "ab+") as f:
                    f.write(recv_data)
            except Exception:
                print("BBBBBBBBB")
        else:
            break        

    TCP_socket.close()

if __name__ == "__main__":
    main()