from app import db #// "De 'app' importa o objeto que vai se conectar com o banco de dados"

from datetime import datetime

class Agendamento (db.Model):  #// Cada agendamento da academia vai ser guardado aqui 

    id = db.column(db.Integer, primary_key=True) #// Um numero unico para cada agendamento (o 'primaryKey' Garante que nunca vai repetir )

    nome_cliente = db.column(db.String(100), nullable=False) #// O nome de quem marcou (o 'nullabe' significa que esse campo é obrigaorio )

    
    nome_barber = db.column(db.String(100), nullable=False)  #// ( Nome do barbeiro escolhido )

    data_hora = db.Column (db.DateTime, nullable=False)  #// Dia e horarioo do agendamento 

    status = db.Column(db.String(20), default="Pendente") #// pendente, aceito ou recusado

    criado_em = db.column(db.DateTime, default=datetime.utcnown) #// #A data do agendamento - (preenchido Automaticamente)

