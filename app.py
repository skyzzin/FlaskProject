from flask import Flask,render_template,request
from MyLib.SimpleCrud import *

app = Flask(__name__)



@app.route('/')
def Start():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    return render_template('HomePage.html')

@app.route('/cad', methods=["POST"])
def Cad():
    nome = request.form.get('nome')
    senha = request.form.get('senha1')
    print(f'{nome},{senha}')
    InsertDB(nome=nome,senha=senha)
    return render_template('index.html') 

@app.route('/login/<nome>',methods=["POST"])
def Login(nome):
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    print(nome)
    if  SearchDB(nome=nome,senha=senha) == 'erro':
            return f'Dados Não Econtrados'
    else:
        
        return render_template('HomePage.html',nome=nome)

@app.route('/redefinir',methods=['POST'])
def redefinir():
    newpasswd = request.form.get('rsenha')
    nome = request.form.get('rnome')
    UpdateDB(newpasswd,nome)
    return f'Senha Alterada Com Sucesso'

@app.route('/delete', methods=["POST"])
def delete():
    nome = request.form.get('dnome')
    senha = request.form.get('dsenha')
    DeleteDB(nome,senha)
    return f"Conta deletada"
    
@app.route('/perfil')
def pefil():
    return render_template('perfil.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/addproduto', methods=["POST"])
def addproduto():

    return render_template('addproduto.html')


    
        
        
   
   
    
    
    

    

if __name__ =='__main__' :
    app.run(debug=True)