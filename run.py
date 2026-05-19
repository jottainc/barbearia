    ##   PONTO DE PARTIDA (PRIMEIRA COISA QUE O PY VAI RODAR QUANDO LIGAR O SERVIDOR)     ##

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

    