from flask import Flask
from markupsafe import escape # adciona variaveis <variavel> que passa para a função como uma palavra-chave
from flask import url_for
from flask import render_template

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

#              '/hello/' ou '/hello/<name> 

# A funcao 'hello' que pertence a essas rotas retorna um render_template com 
# a página que será renderizada mais as variaveis que vieram pela rota (ou nenhuma name=None ex.)
# ao renderizar a página o Jinja entra em ação, ele já vai estar esperando o retorno com a página
# e as variáveis, e lá ele irá tratár isso 


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# Como ele apenas renderiza o html, ele não trata o if aqui, apenas diretamente no html com o jinja


if __name__=='__main__':
    app.run(debug=True)

