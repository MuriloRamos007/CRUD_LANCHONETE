import flet as ft
from database.conector import Conector
from controllers.produto_controller import Produto_Controller
from models.produto import Produto

def produto_view(page):

    conexao = Conector.conectar()

    elementos = []

    if conexao != None:
        produtos = Produto_Controller.listar(conexao)

        dt_rows = []

        def salvar(e):
            produto = Produto(parCod=None,
                              parDescricao=desc_field.value, 
                              parPreco=valor_field.value, 
                              parQtd=qtd_field.value)
            
            Produto_Controller.inserir(conexao, produto)

            page.snack_bar = ft.SnackBar(ft.Text("Item adicionado com sucesso!!!"))
            page.snack_bar.open = True

        page.snack_bar = ft.SnackBar(ft.Text("Conexão com o banco de dados estabelecido!!!"))
        page.snack_bar.open = True

        desc_field = ft.TextField(label="Descrição")
        valor_field = ft.TextField(label="Valor")
        qtd_field = ft.TextField(label="Quantidade no Estoque")
        salvar_button = ft.ElevatedButton(text="Salvar", on_click=salvar)

        divisor = ft.Divider(height=5)
        tabela = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Produto")),
                ft.DataColumn(ft.Text("Valor")),
                ft.DataColumn(ft.Text("Quantidade")),
                ft.DataColumn(ft.Text("Deletar?")),
            ],
            rows=[]
        )

        if produtos != []:
            for produto in produtos:
                dt_row = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(produto.cod)),
                        ft.DataCell(ft.Text(produto.descricao)),
                        ft.DataCell(ft.Text(produto.preco)),
                        ft.DataCell(ft.Text(produto.qtd)),
                        ft.DataCell(ft.IconButton(ft.icons.DELETE, on_click=lambda e: Produto_Controller.delete(conexao, produto.cod))),
                    ]
                )
                dt_rows.append(dt_row)
            tabela.rows = dt_rows

        elementos.append(desc_field)
        elementos.append(valor_field)
        elementos.append(qtd_field)
        elementos.append(salvar_button) 
        elementos.append(divisor) 
        elementos.append(tabela) 

    else:
        dlg = ft.SnackBar(ft.Text("Falha na conexão com o banco de Dados!!!"))
        page.snack_bar = dlg
        dlg.open = True
        elementos.append(dlg)

    return ft.Column(
        controls=elementos
    )
