import flet as ft
from view.produto_view import produto_view

def main(Page: ft.Page):
    Page.title = "Lanchonete do Taboca"
    Page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    Page.scroll = ft.ScrollMode.AUTO

    def chama_produto(e):
        coluna = produto_view(Page)
        Page.clean()
        Page.add(coluna)

    Page.add(
        ft.ElevatedButton(
            "Produtos", 
            on_click=chama_produto)
        )

ft.app(main)