import flet as ft
# Importamos las vistas desde tus archivos separados
# Asegúrate de que los archivos se llamen exactamente así:
from welcome import welcome_view
from login import login_view
from registro import registro_view
from dashboard import dashboard_view

def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Lupa Urbana"
    page.window_width = 380
    page.window_height = 750
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
