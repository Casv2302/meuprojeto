from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', titulo = 'Pagina Inicial')

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo = 'Contato')

@app.route('/artigos')
def artigo():
    return render_template('artigos.html', titulo = 'artigos')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo = 'sobre')        