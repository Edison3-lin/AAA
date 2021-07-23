import socket

def main():
    # 創建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定本地信息
    udp_socket.bind(("", 7890))
    
    while True:
        # 從鍵盤輸入資料
        udp_data = input("輸入資料：")
        
        if udp_data == "exit":
            break
        
        # 發送
        udp_socket.sendto(udp_data.encode("utf-8"),('172.20.10.4', 8080))
        
    # 傳送結束
    udp_socket.close()

if __name__ == "__main__":
    main()
