import pymysql

banco = pymysql.connect(host='localhost', user='root', password='', database='banco')
cursor = banco.cursor()

def CreateTable():
    banco = pymysql.connect(host='localhost', user='root', password='', database='banco')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS produtos(id INT(10) PRIMARY KEY AUTO_INCREMENT,nome VARCHAR(20),codigo BIGINT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS user (id INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(30), senha VARCHAR(30),acesso VARCHAR(10))')

def InsertDB(nome,senha,acesso):
    banco = pymysql.connect(host='localhost', user='root', password='', database='banco')
    cursor = banco.cursor()
    cursor.execute('INSERT INTO user(nome,senha,acesso) VALUES(%s,%s,%s)',(nome,senha,acesso))
    banco.commit()

def Search(nome,senha):
    banco = pymysql.connect(host='localhost', user='root', password='', database='banco')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM user WHERE nome=%s AND senha=%s',(nome,senha))

    result = cursor.fetchone()
    return result
        


CreateTable()
