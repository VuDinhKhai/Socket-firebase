import socket

Host_name=socket.gethostname()
print("HOST_Name: ",Host_name)
addr=socket.gethostbyname(Host_name)
print("IP: ",addr)

'''
s.rev(buflen[,flags])   nhận dữ liệu
s.send(data[,flags])    gửi dữ liệu
'''