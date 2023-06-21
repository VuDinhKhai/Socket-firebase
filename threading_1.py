from os import name
import socket
import threading

def f_client(c, a, p):

    while True:
        msg=c.recv(1024)
        if msg[0]== "#":
            break
        c.sendall(msg)
    c.close()
    return

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',7777))
s.listen(5)

while True:
    client,(nameaddr,ipaddr)=s.accept()
    print("Name addr : ",nameaddr)
    print("IP addr : ",ipaddr)
    t=threading.Thread(target=f_client,args=(client,nameaddr,ipaddr))
    t.start()