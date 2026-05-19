from flask import Flask  #// Busca a ferramenta Flask que eu instalei pelo terminal 

from flask_sqlalchemy import SQLAlchemy #// importa o tradutor do sql 

from app.config import Config #// Importa a configuração ("Config")

db = SQLAlchemy() #// Estou criando um objeto que vai trocar ideia com o banco de dados 

def create_app(): #Receita
    app = Flask (__name__)

    app.config.from_object(Config) #//  Aqui eu apliquei as configurações da aplicação 

    db.init_app(app) #// Conectando o banco de dados a aplicação 


    from app.routes import main      #Busca as rotas (OS "endereços" DO SISTEMA)
    app.register_blueprint (main)   #Registra essas rotas na aplicação (É COMO COLOCAR PLACAS NA CIDADE)

    return app  #DEVOLVE A APLICAÇÃO PRONTA PARA QUEM CHAMOU A FUNÇÃO 

