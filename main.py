import flet as ft
from welcome import welcome_view
from login import login_view
from registro import registro_view
from dashboard import dashboard_view

def main(page: ft.Page):
    page.title = "Lupa Urbana"
    page.window_width = 380
    page.window_height = 750
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(welcome_view(page))
        elif page.route == "/login":
            page.views.append(login_view(page))
        elif page.route == "/registro":
            page.views.append(registro_view(page))
        elif page.route == "/dashboard":
            page.views.append(dashboard_view(page))
        page.update()

    page.on_route_change = route_change
    
    # Asegur ar que la vista inicial se muestre
    page.route = "/"
    route_change(None)

if __name__ == "__main__":
    # Actualizado: run en lugar de app()
    ft.run(
        main, 
        view=ft.AppView.WEB_BROWSER, 
        port=8080,
        host="0.0.0.0"
    )