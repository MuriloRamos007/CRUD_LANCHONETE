from database.conector import Conector
from controllers.produto_controller import Produto_Controller

conexao = Conector.conectar()

if conexao!=None:
    print("Conectado com o banco de dados")
  
    produtos =  Produto_Controller.buscar(conexao, "X")
    if produtos!=[]:
        for produto in produtos:
            produto.listar()
    else:
        print("Nenhum produto encontrado!")
    
    Conector.fechar_conexao(conexao)