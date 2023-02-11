from flask import Flask,render_template,request
from MyLib.banco import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    nome = request.form.get('lnome')
    senha = request.form.get('lsenha')
    res = Search(nome=nome,senha=senha)
    if res:
        return render_template('PVDCX-FUNCIONARIO.html')
    else:
        return f'Invalido'

@app.route('/cadastrar')
def pdv():
    return render_template('cadastrar.html')

if __name__ == '__main__':
    app.run(debug=True)