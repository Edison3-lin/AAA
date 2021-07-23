import socket

def main():
    # 1.買個手機（創建TCP套接字 socket）
    TCP_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入SIM卡（綁定本地信息 bind）
    TCP_server_socket.bind(("172.20.10.3", 8888))
    print("===Server binding...===\n")

    while True:
        # 3.將手機設置為正常響鈴模式（讓默認的套接字由主動變為被動 listen）
        TCP_server_socket.listen(128)
        print("===Server listen...===\n")

        # 4.等待別人的電話打來（等待客戶端的連接 accept）
        new_client_socket, client_addr = TCP_server_socket.accept()
        print("===Server accept...===\n")


        # 服務這個客戶端
        print("請輸入下載檔案名稱：")
        recv_data = new_client_socket.recv(100)
        print("%s\n" % (recv_data.decode(encoding='utf-8')))
        try:
            with open(recv_data.decode(encoding='utf-8'), 'rb') as f1:
                new_client_socket.send(f1.read())
        except Exception:
            print('file doesn"t exist')
        # 結束這個客戶端    
        new_client_socket.close()

    # 結束通訊服務
    TCP_server_socket.close()


if __name__ == "__main__":
    main()