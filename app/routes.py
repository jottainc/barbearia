# //   Criação das rotas  // #

from flask import Blueprint, request, jsonify, render_template

from app import db
from datetime import datetime
from app.models import Agendamento

main = Blueprint("Main", __name__)

@main.route("/")
def index():
    return render_template ("index.html")   #Criando a rota para renderizar o html no servidor/navegador

@main.route("/agendamento", methods=["POST"])
def criar_agendamento():
    dados = request.get_json()
    novo = Agendamento(
        nome_cliente=dados["nome_cliente"],
        nome_barbeiro=dados["nome_barbeiro"],
        data_hora=datetime.strptime(dados["data_hora"], "%Y-%m-%d %H:%M"),
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({"mensagem": "Agendamento criado com sucesso!", "id": novo.id}), 201

@main.route("/agendamentos", methods=["GET"])
def listar_agendamentos():
    agendamentos = Agendamento.query.all()
    resultado = []
    for a in agendamentos:
        resultado.append({
            "id": a.id,
            "nome_cliente": a.nome_cliente,
            "nome_barbeiro": a.nome_barbeiro,
            "data_hora": str(a.data_hora),
            "status": a.status
        })
    return jsonify(resultado), 200

@main.route("/cancelar_agendamentos/<int:id>/", methods=["DELETE"])
def cancelar_agendamento(id):
    agendamento_q = db.session.get(Agendamento, id)
    
    if agendamento_q is None:
        return jsonify({"ERROR": "Agendamento não encontrado"}), 404
    else:   
     db.session.delete(agendamento_q)
     db.session.commit()
     return jsonify({"mensagem": "Agendamento cancelado com sucesso"}), 200
