import socket

def Connect(id,msg):
    skt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    skt.connect(('localhost',9822))
    skt.sendall(id.encode())
    skt.sendall('-'.encode())
    skt.sendall(msg.encode())
    skt.close()
        

        
        