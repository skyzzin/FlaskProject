import socket
from Banco import *

skt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind(('127.0.0.1',9822))
skt.listen()
print('Servidor Online')
while True:
    conn,adress = skt.accept()
    print('Cliente Connectado',adress)
    while True:
        data = conn.recv(1024)
        if not data:
            print('Cliente desconectado:', adress)
            break
        dados = data.decode()
        _dados = dados.split('-')
        id = _dados[0]
        msg = _dados[1]
        print("Id: ",id,"Mensagem: ",msg)
        InsertIntoMsg(nome=id,msg=msg)