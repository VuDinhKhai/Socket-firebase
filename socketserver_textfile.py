import socket

host_name=socket.gethostname()
HOST=socket.gethostbyname(host_name)
PORT=8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
while True:
    client, addr = s.accept()
    try:
        print('Connected by', addr)
        with open("D:/vscode/code Python/truyen_nhan_tin/VDK.txt",'rb') as f:
            #im=Image.open()
            #im.show()
            client.send(f.read())
            f.close
    finally:
        client.close()
s.close()






