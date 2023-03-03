import pymysql


def CreateTable():
    db = pymysql.connect(host='localhost',user='root',passwd='',database='banco')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
        id INT(1) AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(20),
        email VARCHAR(20),
        senha VARCHAR(20))''')
    db.close()

def CreateTableMsg():
    db = pymysql.connect(host='localhost',user='root',passwd='',database='banco')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS comentarios(
          id INT(100) AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(20),
        msg VARCHAR(100))''')
    db.close()
    
    
    
def InsertInto(nome,email,senha):
    db = pymysql.connect(host='localhost',user='root',passwd='',database='banco')
    cursor = db.cursor()
    cursor.execute('INSERT INTO usuarios(nome,email,senha) VALUES(%s,%s,%s)',(nome,email,senha))
    db.commit()
    db.close()

def InsertIntoMsg(nome,msg):
    db = pymysql.connect(host='localhost',user='root',passwd='',database='banco')
    cursor = db.cursor()
    cursor.execute('INSERT INTO comentarios(nome,msg) VALUES(%s,%s)',(nome,msg))
    db.commit()
    db.close()

def Search(nome,senha):
    db = pymysql.connect(host='localhost',user='root',passwd='',database='banco')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE nome=%s AND senha=%s',(nome,senha))
    res = cursor.fetchone()
    return res

def SearchMsg():
    db = pymysql.connect(host='localhost',user='root',passwd='',database='banco')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM comentarios')
    res = cursor.fetchall()
    return res

def Update(nsenha,email,senha):
    db = pymysql.connect(host='localhost',user='root',passwd='',database='banco')
    cursor = db.cursor()
    cursor.execute('UPDATE usuarios SET senha=%s WHERE email=%s AND senha=%s',(nsenha,email,senha))
    db.commit()
    db.close()












CreateTable()
CreateTableMsg()