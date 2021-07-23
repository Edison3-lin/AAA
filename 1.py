import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 5555))
    while True:
        # dest_ip = input("輸入對方ip: ")
        # dest_port = int(input("輸入對方port: "))
        # send_data = input("請輸入資料: ")
        send_data = "請輸入資料: "
        udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1", 8080))
        # udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

        recv_data, addr = udp_socket.recvfrom(100)
        if recv_data == b'exit':
            break

        print("%s %s" % (recv_data.decode(encoding='utf-8'), addr))



    udp_socket.close()

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