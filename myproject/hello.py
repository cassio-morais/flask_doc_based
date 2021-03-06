from flask import Flask
from markupsafe import escape # adciona variaveis <variavel> que passa para a função como uma palavra-chave
from flask import url_for
from flask import render_template
from flask import request

app= Flask(__name__)


# VARIABLE RULES

@app.route('/user/<username>') # rota 
def show_user_profile(username): # variavel que vem na url
    # show the user profile for that user
    return 'User %s' % escape(username) 
    
    # http://127.0.0.1:5000/user/cassio
    # User cassio


@app.route('/post/<int:post_id>') # convertendo em int na chamada
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

    # http://127.0.0.1:5000/post/12
    # Post 12


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

    # http://127.0.0.1:5000/path/teste
    # Subpath teste




# UNIQUE URLS / REDIRECTION BEHAVIOR


@app.route('/projects/') # ele volta para a url canônica /project/ se for passado a barra depois do fim. 
def projects():
    return 'The project page'

@app.route('/about') # sem a barra no final, a rota quebra se for digitado a url /about/ assim
def about():
    return 'The about page'




# URL BUILDING

# with app.test_request_context(): # só test_request_context pra mostrar no shell como fica
    
#     # facilitar a apresentação de URLs dentro do código
#     print(url_for('hello'))
#     # /hello
#     print(url_for('hello', next='/')) 
#     # /hello?next=/
#     print(url_for('show_user_profile',username='cassio morais'))
#     # /user/cassio%20morais




# HTTP METHODS

# por padrão, se vc não passar método nenhum, o decorator app.route interpreta que é um get

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()





# STATIC FILES

# criei a pasta static pra colocar arquivos estaticos: js, css, imgs etc
# posso usar o url_for() pra gerar um endpoint estatico pra minha pasta

# url_for('static', filename='style.css')




# RENDERING TEMPLATES 

# O Flask vem com o Jinja que lida com templates html

# quando a url é chamada no exemplo abaixo, ela virá por duas rota possiveis:

#              conceito de rotas dinâmicas   
#             '/hello/' ou '/hello/<name>'

# A funcao 'hello' que pertence a essas rotas retorna um render_template com 
# a página que será renderizada mais as variaveis que vieram pela rota (ou nenhuma name=None ex.)
# ao renderizar a página o Jinja entra em ação, ele já vai estar esperando o retorno com a página
# e as variáveis, e lá ele irá tratar isso (hello.html)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# Como ele apenas renderiza o html, ele não trata o if aqui, apenas diretamente no html com o jinja


#MARKUP


# Here is a basic introduction to how the Markup class works:

# Ele implementa uma segurança ao código https://github.com/pallets/markupsafe

# Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
#       Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
# Markup.escape('<blink>hacker</blink>')
#       Markup('&lt;blink&gt;hacker&lt;/blink&gt;')
# Markup('<em>Marked up</em> &raquo; HTML').striptags()
#       'Marked up » HTML'


# THE REQUEST OBJECT

# abaixo um teste de requisica para validar os dados passados usando o atributo 'method'
# que vem na requisicao. Se ela for 'POST' e se os dados sao validos, retorna a o resultado da funcao 'log_the_user_in'
# senão, ele sobe um erro, sai do if e renderiza o template de login com o error.

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)


# FILE UPLOADS

#  Just make sure not to forget to set the enctype="multipart/form-data" attribute on your HTML form, 
#  otherwise the browser will not transmit your files at all.


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...


if __name__=='__main__':
    app.run(debug=True)

