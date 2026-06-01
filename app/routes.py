# //   Criação das rotas  // #


from flask import Blueprint, request, jsonify   #// " Requets = recepcionista. jsoniFY = tradutor "

from app import db   

from datetime import datetime

from app.models import Agendamento

main = Blueprint ("Main", __name__) #  Cria essa gaveta e dá o nome de main pra ela.

@main.route("/agendamento", methods=["POST"])
def criar_agendamento():
    dados = request.get_json() #// Pega tudo que o usuario enviou e guarda em uma variavel (dados)
    
    novo = Agendamento(
        nome_cliente=dados["nome_cliente"],  
        nome_barber=dados["nome_barber"],
        data_hora=datetime.strptime(dados["data_hora"], "%Y-%m-%d %H:%M"),
    )
    

    db.session.add(novo) #//Coloca o agendamento da fila para salvar     
    db.session.commit()   #// "botão de salvar"

    return jsonify ({
        "mensagem": "Agendamento Criado com sucesso !!",
        "id": novo.id}), 201 #// Mensagem de sucesso

@main.route("/agendamentos", methods=["GET"])
def listar_agendamentos():
    agendamentos = Agendamento.query.all()  #// "Vai no banco e buscA TODOS OS AGENDAMENTOS"

    resultado = []
    for a in agendamentos:   #// PERCORRE CADA AGENDAMENTO CRIADO UM POR UM 
        
        resultado.append ({   #// PEGA CADA AGENDAMENTO E TRANSFORMA EM UM FORMATO LEGÍVEL PARA O USUARIO
            "id": a.id,
            "nome_cliente": a.nome_cliente,
            "nome_barber": a.nome_barber,
            "data_hora": str(a.data_hora),
            "status": a.status
        })

    return jsonify(resultado), 200



@main.route ("/cancelar_agendamentos/<int:id>/", methods=["DELETE"])
def cancelar_agendamento(id):
    agendamento_q = db.session.get(Agendamento,id)


    if agendamento_q is None:
        return jsonify ({"ERROR" : "AGENDAMENTO NÃO ENCONTRADO"}), 404
    else:
        db.session.delete(agendamento_q)
        db.session.commit()
        return jsonify ({"mensagem" : "Agendamento cancelado com sucesso"}), 200
