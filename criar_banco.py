from app import create_app,db  #//De "app" importa a criação de apps e o tradutor que conecta o python ao sql

app = create_app()  #// Aqui eu to ligando a aplicação Flask (o recepcionista do meu sistema), sem isso o py não saberia conversar com o cp

with app.app_context (): #// "Execute tudo que vem em baixo dentro do ambiente da nossa aplicação"
    
    db.create_all ()   #// Serve para criar a tabela de dados de verdade, é como se fosse eu pegar a planta de uma casa e criar ela de verdade  
    
    print ("Banco criado com sucesso")
    

    