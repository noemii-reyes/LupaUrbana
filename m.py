import flet as ft

def main(page: ft.Page):
    page.add(ft.Text("Si ves esto, Codespaces está funcionando bien"))

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)