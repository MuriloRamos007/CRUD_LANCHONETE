import mysql.connector
from models.produto import Produto

class Produto_Controller:

    #pip install mysql-connector-python para instalar a conexão

    #criar um novo registro no banco de dados
    def inserir(conexao, Produto):
        #usar o %s para
        try:
            cursor = conexao.cursor()
            query = "INSERT INTO produtos(Descricao, Preco, Quantidade) VALUES(%s, %s, %s)"
            cursor.execute(query, (Produto.descricao, Produto.preco, Produto.qtd))
            conexao.commit()
            print(f"{Produto.descricao} Registrado com sucesso!")
            
        except mysql.connector.Error as e:
            print(f"Erro ao conectar com o BD:{e}")

        finally:
            cursor.close()

    #Listar todas as informações da tabela
    def listar(conexao):
        listaProdutos=[]
        try:
            cursor = conexao.cursor()
            query = "SELECT * FROM produtos"
            cursor.execute(query)
            registros = cursor.fetchall()

            for registro in registros:
                objeto = Produto(*registro)
                listaProdutos.append(objeto)
            
        except mysql.connector.Error as e:
            print(f"Erro ao conectar com o BD:{e}")

        finally:        
            cursor.close()

        return listaProdutos

    #atualiza uma irformação de uma linha
    def update(conexao, Id, Preco, Quantidade):
        try:
            cursor = conexao.cursor()
            query = "UPDATE produtos SET Preco=%s, Quantidade=%s WHERE Id=%s"
            cursor.execute(query, (Preco, Quantidade, Id))
            conexao.commit()
            print(f"{Id} Atualizado com sucesso!")

        except mysql.connector.Error as e:
            print(f"Erro ao atualizar o Produto:{e}")

        finally:
            cursor.close()

    #deletar uma linha
    def delete(conexao, Id):
        try:
            cursor = conexao.cursor()
            query = "DELETE FROM produtoS WHERE Id = %s"
            cursor.execute(query, (Id,))
            conexao.commit()
            print(f"{Id} Deletado com sucesso!")

        except mysql.connector.Error as e:
            print(f"Erro ao deletar o Produto:{e}")

        finally:
            cursor.close()

    #buscar as informações de uma linha
    def buscar(conexao,Descricao):
        listaProdutos=[]
        try:
            cursor = conexao.cursor()
            query = "SELECT * FROM produtos WHERE Descricao like %s "
            cursor.execute(query, ("%"+Descricao+"%",))
            registros1 = cursor.fetchall()

            for produto in registros1:
                objeto = Produto(*produto)
                listaProdutos.append(objeto)

        except mysql.connector.Error as e:
            print(f"Erro ao buscar o Produto:{e}")

        finally:
            cursor.close()

            return listaProdutos
