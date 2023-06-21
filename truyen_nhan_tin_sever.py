
# tham số đầu tiên là Address Family: kiểu thiết lập kết nối. Python hỗ trợ 3 dạng:
#         AF_INET: Ipv4
#         AF_INET6: Ipv6
#         AF_UNIX
# tham số thứ hai là Socket Type: cách thiết lập giao thức
#         SOCK_STREAM: TCP
#         SOCK_DGRAM: UDP
# s.bind((HOST, PORT))          Đăng ký tên cho socket, ràng buộc địa chỉ vào socket
# s.listen(2)                   Cho socket đang lắng nghe tới tối đa 2 kết nối
# client, addr = s.accept()     Khi một client gõ cửa, server chấp nhận kết nối và 1 socket mới được tạo ra.
#                                    Client và server bây giờ đã có thể truyền và nhận dữ liệu với nhau
# data = client.recv(1024)           Nhận gói dữ liệu
# str_data = data.decode("utf8")     Phân tích gói dữ liệu vừa nhận
# s.sendall(bytes(msg, "utf8"))      Gửi dữ liệu thông qua giao thức TCP
# s.close()	                       Đóng một kết nối







import socket
HOST = '192.168.43.139'

PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
while True:
    client, addr = s.accept()
    try:
        print('Connected by', addr)
        while True:
            data = client.recv(1024)
            str_data = data.decode("utf8")
            if str_data == "quit":
                break
            print("Client: " + str_data)
            msg = str(input("Server: "))
            #s.sendall(bytes(msg,"utf8"))
            client.send(bytes(msg,"utf8"))
    finally:
        client.close()
s.close()












# import socket

# HOST = '127.0.0.1'
# PORT = 65432

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     print('Start listening...')
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)


# """Server for multithreaded (asynchronous) chat application."""
# from socket import AF_INET, socket, SOCK_STREAM
# from threading import Thread


# def accept_incoming_connections():
#     while True:
#         client, client_address = SERVER.accept()
#         print("%s:%s has connected." % client_address)
#         client.send(bytes("Nhập tên của bạn rồi bắt đầu chat!", "utf8"))
#         addresses[client] = client_address
#         Thread(target=handle_client, args=(client,)).start()


# def handle_client(client):  # Takes client socket as argument.
#     name = client.recv(BUFSIZ).decode("utf8")
#     welcome = 'Xin chào %s! Nếu bạn muốn thoát gõ, {quit} để thoát.' % name
#     client.send(bytes(welcome, "utf8"))
#     msg = "%s đã tham gia phòng chat!" % name
#     broadcast(bytes(msg, "utf8"))
#     clients[client] = name

#     while True:
#         msg = client.recv(BUFSIZ)
#         if msg != bytes("{quit}", "utf8"):
#             broadcast(msg, name + ": ")
#         else:
#             client.send(bytes("{quit}", "utf8"))
#             client.close()
#             del clients[client]
#             broadcast(bytes("%s đã thoát phòng chat." % name, "utf8"))
#             break


# def broadcast(msg, prefix=""):  # prefix is for name identification.
#     for sock in clients:
#         sock.send(bytes(prefix, "utf8") + msg)


# clients = {}
# addresses = {}

# HOST = '127.0.0.1'
# PORT = 33000
# BUFSIZ = 1024
# ADDR = (HOST, PORT)

# SERVER = socket(AF_INET, SOCK_STREAM)
# SERVER.bind(ADDR)

# if __name__ == "__main__":
#     SERVER.listen(5)
#     print("Chờ kết nối từ các client...")
#     ACCEPT_THREAD = Thread(target=accept_incoming_connections)
#     ACCEPT_THREAD.start()
#     ACCEPT_THREAD.join()
#     SERVER.close()

