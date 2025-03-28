from flask import Flask, render_template # Importando a biblioteca Flask
#biblioteca para segurança no login
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__) # Criando um objeto do Flask chamado app 

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True) 