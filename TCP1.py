import socket

def main():
    # 1.買個手機（創建TCP套接字 socket）
    TCP_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入SIM卡（綁定本地信息 bind）
    TCP_server_socket.bind(("172.20.10.3", 8888))
    print("===1===")

    while True:
        # 3.將手機設置為正常響鈴模式（讓默認的套接字由主動變為被動 listen）
        TCP_server_socket.listen(128)
        print("===listen...===")

        # 4.等待別人的電話打來（等待客戶端的連接 accept）
        new_client_socket, client_addr = TCP_server_socket.accept()
        print("===accept...===")

        # 服務這個客戶端
        while True:
            recv_data = new_client_socket.recv(100)
            if recv_data:
                print("%s %s" % (recv_data.decode(encoding='utf-8'), client_addr))
                new_client_socket.send("Received...".encode('utf-8'))                
            else:    
                break
        # 結束這個客戶端    
        new_client_socket.close()

        # 結束通訊服務
        if recv_data == b'exit':
            TCP_server_socket.close()


if __name__ == "__main__":
    main()