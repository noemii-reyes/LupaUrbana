import flet as ft

def welcome_view(page):
    # Configuración de Colores
    COLOR_PRIMARIO = "#D35400"    # Naranja
    COLOR_SECUNDARIO = "#5D4037"  # Café
    COLOR_FONDO = "#FCF8F4"       # Crema

    return ft.View(
        "/",  # Ruta raíz
        horizontal_alignment="center",
        vertical_alignment="center",
        bgcolor=COLOR_FONDO,
        controls=[
            # Contenedor del Logo (Círculo con Lupa)
            ft.Container(
                content=ft.Text(
                    "🔍", 
                    size=80
                ),
                border=ft.border.all(4, COLOR_SECUNDARIO),
                border_radius=100,
                padding=20,
            ),
            
            # Títulos
            ft.Column(
                horizontal_alignment="center",
                spacing=0,
                controls=[
                    ft.Text(
                        "LUPA", 
                        size=55, 
                        weight="bold", 
                        color=COLOR_SECUNDARIO
                    ),
                    ft.Text(
                        "URBANA", 
                        size=22, 
                        color=COLOR_PRIMARIO, 
                        weight="w500"
                    ),
                ]
            ),
            
            ft.Container(height=50), # Espacio visual
            
            # Botones de Acción
            ft.Column(
                horizontal_alignment="center",
                spacing=15,
                controls=[
                    ft.ElevatedButton(
                        "INICIAR SESIÓN",
                        width=300,
                        height=55,
                        style=ft.ButtonStyle(
                            color="white",
                            bgcolor=COLOR_PRIMARIO,
                            shape=ft.RoundedRectangleBorder(radius=12),
                        ),
                        on_click=lambda _: page.go("/login")
                    ),
                    ft.OutlinedButton(
                        "CREAR CUENTA",
                        width=300,
                        height=55,
                        style=ft.ButtonStyle(
                            color=COLOR_SECUNDARIO,
                            side=ft.BorderSide(2, COLOR_SECUNDARIO),
                            shape=ft.RoundedRectangleBorder(radius=12),
                        ),
                        on_click=lambda _: page.go("/registro")
                    ),
                ]
            ),
            
            # Frase decorativa inferior
            ft.Container(
                margin=ft.margin.only(top=40),
                content=ft.Text(
                    "Tu reporte hace la diferencia", 
                    size=14, 
                    color=COLOR_SECUNDARIO,
                    italic=True
                )
            )
        ]
    )