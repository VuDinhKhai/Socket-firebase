import socket
import threading


def server(client,addr):
    print('Connected by', addr)
    while True:
        data = client.recv(1024)
        str_data = data.decode("utf8")
        if str_data == "quit":
            break
        print(addr, " : " + str_data)
        # msg = str(input("Server: "))
        #     client.send(bytes(msg,"utf8"))
    print(client," : finished")
    #print(" count: ",threading.active_count( ) )
    client.close()

host_name=socket.gethostname()
HOST=socket.gethostbyname(host_name)
PORT=8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)


while True:
    try:
        client, addr = s.accept()
        thr=threading.Thread(target=server,args=(client,addr))
        thr.daemon = False
        thr.start()
        #thr.join()
        #print(" count: ",threading.active_count( ) )
        #print("threading.enumerate( ) : ",threading.enumerate())
    
    except:
        print("Error")
    
print("End")
s.close()