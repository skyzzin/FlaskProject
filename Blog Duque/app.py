import os,threading

def client():
    os.system('python ./client/app.py')
def Servidor():
    os.system('python ./servidor/servidor.py')


s = threading.Thread(target=Servidor).start()
c = threading.Thread(target=client).start()




