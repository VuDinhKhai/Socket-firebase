import socket
from PIL import Image

host_name=socket.gethostname()
HOST=socket.gethostbyname(host_name)
PORT=8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('connecting to %s port ' + str(server_address))
s.connect(server_address)
#D:\vscode\code Python\truyen_nhan_tin\The.jpg
with open("D:/anhthe/anhthe.jpg",'wb') as f:
    print("file opened")
    data=s.recv(1024)
    while data:
        f.write(data)
        data=s.recv(1024)
        print(data)
    #f.write(data)
    f.close()
with open("D:/anhthe/anhthe.jpg", 'rb') as f:
    im = Image.open(f)
    im.show()
s.close()