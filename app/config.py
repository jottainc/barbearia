import os  #// importa uma ferramenta do Python que permite conversar com o sistema operacional. Vou precisar dela mais pra frente.

class Config: #// Estou criando uma caixinha para guardar todas as informações do projeto 

    SECRET_KEY = "barbearia-secret-123"  #// Senha secreta que o Flask usa para guardar informações

    SQLALCHEMY_DATABASE_URI = "sqlite:///barbearia.db"  #//  O endereço do nosso banco de dadsos chamado: barbearia.db".

    SQLALCHEMY_TRACK_MODIFICATIONS = False #// Desliga a porra de um aviso chato 
