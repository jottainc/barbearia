from flask import Flask  #Busca a ferramenta Flask que eu instalei pelo terminal 

def create_app(): #Receita
    app = Flask (__name__)

    from app.routes import main      #Busca as rotas (OS "endereços" DO SISTEMA)
    app.register_blueprint (main)   #Registra essas rotas na aplicação (É COMO COLOCAR PLACAS NA CIDADE)

    return app  #DEVOLVE A APLICAÇÃO PRONTA PARA QUEM CHAMOU A FUNÇÃO 

