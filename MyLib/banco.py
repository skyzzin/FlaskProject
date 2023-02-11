import sqlite3

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()

def CreateTable():
    banco = sqlite3.connect('banco.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(30), senha VARCHAR(30))')

def InsertDB(nome,senha):
    banco = sqlite3.connect('banco.db')
    cursor = banco.cursor()
    cursor.execute('INSERT INTO user(nome,senha) VALUES(?,?)',(nome,senha))
    banco.commit()

def Search(nome,senha):
    banco = sqlite3.connect('banco.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM user WHERE nome=? AND senha=?',(nome,senha))

    result = cursor.fetchone()
    return result
        


CreateTable()

