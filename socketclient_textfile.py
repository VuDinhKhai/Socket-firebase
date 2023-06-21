import socket

host_name=socket.gethostname()
HOST=socket.gethostbyname(host_name)
PORT=8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('connecting to %s port ' + str(server_address))
s.connect(server_address)

with open("D:/anhthe/khai.txt",'wb') as f: #‘wb’	Mở file để ghi cho dạng nhị phân. 
    #Nếu file không tồn tại thì sẽ tạo mới file và ghi nội dung,
    # nếu file đã tồn tại thì sẽ bị cắt bớt (truncate) và ghi đè lên nội dung cũ
    print("file opened")
    data=s.recv(1000000)
    f.write(data)
    print(data)
    f.close()
with open("D:/anhthe/khai.txt", 'r', encoding = 'utf-8') as f:
    #‘rb’	Mở file chế độ đọc cho định dạng nhị phân
    c=f.read()
    print(c)
s.close()

