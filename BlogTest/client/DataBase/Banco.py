import sqlite3

def CreateTable():
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        senha TEXT)''')
    db.close()

def CreateTableMsg():
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS comentarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        msg TEXT)''')
    db.close()

def InsertInto(nome,email,senha):
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()
    cursor.execute('INSERT INTO usuarios(nome,email,senha) VALUES(?,?,?)',(nome,email,senha))
    db.commit()
    db.close()

def InsertIntoMsg(nome,msg):
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()
    cursor.execute('INSERT INTO comentarios(nome,msg) VALUES(?,?)',(nome,msg))
    db.commit()
    db.close()

def Search(nome,senha):
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE nome=? AND senha=?',(nome,senha))
    res = cursor.fetchone()
    return res

def SearchMsg():
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM comentarios')
    res = cursor.fetchall()
    return res

def Update(nsenha,email,senha):
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()
    cursor.execute('UPDATE usuarios SET senha=? WHERE email=? AND senha=?',(nsenha,email,senha))
    db.commit()
    db.close()

CreateTable()
CreateTableMsg()
