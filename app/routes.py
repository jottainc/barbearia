# //   Criação das rotas  // #

from flask import Blueprint # Busca uma ferramenta do Flask chamada Blueprint. Pensa nela como uma "gaveta" onde guardamos rotas relacionadas.

main = Blueprint ("Main", __name__) #  Cria essa gaveta e dá o nome de main pra ela.

@main.route ("/")  #// ("Quando alguem acessar o endereço "/" execute a função abaixo" ) - sso vai servir como a entrada inicial 

def index():  #// Função que vai ser usada quando alguem acessar a pagina inicial 
    return "Seja bem vindo a barbearia !! Fique a vontade"
