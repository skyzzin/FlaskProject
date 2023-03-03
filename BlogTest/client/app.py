from flask import Flask, request, render_template, url_for, redirect,session,jsonify
from DataBase.Banco import *
from Mylib.Socket import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<nome>')
def user(nome):
    if nome not in session['nome']:
        return redirect(url_for('login'))
    elif session['nome'] == nome:
        return render_template('usuario.html', nome=nome)
    else:
        return render_template('login.html')

@app.route('/user/nome',methods=["GET"])
def get_user_name():
    session['nome']
    return jsonify(session['nome'])

@app.route('/user/msg',methods=["GET"])
def GetMsg():
    msg = SearchMsg()
    return jsonify(msg)
    

@app.route('/user/chat',methods=["POST","GET"])
def chat():
    if 'nome' not in session:
        return redirect(url_for('login'))
    try:
        msg = request.form.get('msg')
        id = session['nome']
        if msg is not None:
            msg = request.form.get('msg')
            id = session['nome']
            Connect(id,msg)
            
        
    except AttributeError:
        print('AttributeError')
    return render_template('chat.html',nome=id)

@app.route('/user/horarios')
def horarios():
    if 'nome' not in session:
        return redirect(url_for('login'))
    return render_template('horarios.html')

@app.route('/user/fofocas')
def fofocas():
    if 'nome' not in session:
        return redirect(url_for('login'))
    return render_template('fofocas.html')

@app.route('/user/<nome>/config',methods=['POST',"GET"])
def config(nome):
    if 'nome' not in session:
        return redirect(url_for('login'))
    else:
     
     return render_template('config.html')
    
    
        

@app.route('/login', methods=["POST", "GET"])
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
   
    busca = Search(nome, senha)
    if busca:
        session['nome'] = nome
        return redirect(url_for('user', nome=nome))
    else:
        return render_template('login.html')

@app.route('/cadastrar', methods=["POST", "GET"])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email') 
    senha = request.form.get('senha2')
    if nome is not None:
        if len(nome) >= 5:
            if email is not None:
                if len(email) >=5:
                    if senha is not None:
                        if len(senha) >=5:
                            InsertInto(nome, email, senha)
                            return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/resete',methods=['POST',"GET"])
def resete():
    email = request.form.get('email')
    senha = request.form.get('senha')
    nsenha = request.form.get('nsenha')

    if email is not None:
        if len(email) >= 10:
            if senha is not None:
                if len(senha) >= 5:
                    if nsenha is not None:
                        if len(nsenha) >=5:
                            Update(nsenha,email,senha)
                            return redirect(url_for('login'))

    return render_template('resete.html')

if __name__ == '__main__':
    app.run(debug=True)