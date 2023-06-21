


import socket
#HOST = '192.168.1.9'

HOST = '192.168.7.151'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('connecting to %s port ' + str(server_address))
s.connect(server_address)
try:
    while True:
        msg = input('Client: ')
        s.sendall(bytes(msg, "utf8"))
        if msg == "quit":
            break
        data = s.recv(1024)
        print('Server: ', data.decode("utf8"))
finally:
    s.close()

















# import socket

# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)

# print('Received', repr(data))

# from socket import AF_INET, socket, SOCK_STREAM
# from threading import Thread
# import tkinter


# def receive():
#     while True:
#         try:
#             msg = client_socket.recv(BUFSIZ).decode("utf8")
#             msg_list.insert(tkinter.END, msg)
#         except OSError:  # Possibly client has left the chat.
#             break


# def send(event=None):  # event is passed by binders.
#     msg = my_msg.get()
#     my_msg.set("")  # Clears input field.
#     client_socket.send(bytes(msg, "utf8"))
#     if msg == "{quit}":
#         client_socket.close()
#         top.quit()


# def on_closing(event=None):
#     my_msg.set("{quit}")
#     send()

# top = tkinter.Tk()
# top.title("Chatter")

# messages_frame = tkinter.Frame(top)
# my_msg = tkinter.StringVar()  # For the messages to be sent.
# my_msg.set("Nhập tên của bạn!.")
# scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# # Following will contain the messages.
# msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
# scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
# msg_list.pack()
# messages_frame.pack()

# entry_field = tkinter.Entry(top, textvariable=my_msg)
# entry_field.bind("<Return>", send)
# entry_field.pack()
# send_button = tkinter.Button(top, text="Gửi", command=send)
# send_button.pack()

# top.protocol("WM_DELETE_WINDOW", on_closing)

# #Ket noi toi server
# HOST = '127.0.0.1'
# PORT = 33000
# if not PORT:
#     PORT = 33000
# else:
#     PORT = int(PORT)

# BUFSIZ = 1024
# ADDR = (HOST, PORT)

# client_socket = socket(AF_INET, SOCK_STREAM)
# client_socket.connect(ADDR)

# receive_thread = Thread(target=receive)
# receive_thread.start()
# tkinter.mainloop()  # Starts GUI execution.

