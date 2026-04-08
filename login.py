import flet as ft

def login_view(page):
    # Paleta de Colores
    CP = "#D35400" # Naranja
    CS = "#5D4037" # Café
    CF = "#FCF8F4" # Fondo Crema

    return ft.View(
        "/login",
        bgcolor=CF,
        padding=0,
        controls=[
            # Barra Superior con botón para volver
            ft.AppBar(
                leading=ft.IconButton(
                    ft.icons.ARROW_BACK_IOS_NEW, 
                    icon_color="white",
                    on_click=lambda _: page.go("/")
                ),
                title=ft.Text("Iniciar Sesión", color="white", weight="bold"),
                bgcolor=CS,
                center_title=True,
            ),
            
            ft.Container(
                expand=True,
                padding=30,
                content=ft.Column(
                    horizontal_alignment="center",
                    alignment="center",
                    spacing=20,
                    controls=[
                        # Icono de Seguridad
                        ft.Icon(
                            ft.icons.LOCK_PERSON, 
                            size=80, 
                            color=CP
                        ),
                        
                        ft.Text(
                            "Bienvenido de nuevo", 
                            size=24, 
                            weight="bold", 
                            color=CS
                        ),
                        
                        ft.Container(height=10),

                        # Campo: Usuario
                        ft.TextField(
                            label="Usuario o Correo",
                            border_color=CS,
                            focused_border_color=CP,
                            prefix_icon=ft.icons.PERSON,
                            label_style=ft.TextStyle(color=CS),
                        ),

                        # Campo: Contraseña
                        ft.TextField(
                            label="Contraseña",
                            password=True,
                            can_reveal_password=True,
                            border_color=CS,
                            focused_border_color=CP,
                            prefix_icon=ft.icons.LOCK,
                            label_style=ft.TextStyle(color=CS),
                        ),

                        ft.Container(height=20),

                        # Botón Entrar
                        ft.ElevatedButton(
                            "ENTRAR",
                            width=300,
                            height=55,
                            style=ft.ButtonStyle(
                                color="white",
                                bgcolor=CP,
                                shape=ft.RoundedRectangleBorder(radius=12),
                            ),
                            on_click=lambda _: page.go("/dashboard")
                        ),

                        # Enlace: Olvidé mi contraseña
                        ft.TextButton(
                            "¿Olvidaste tu contraseña?",
                            style=ft.ButtonStyle(color=CS)
                        ),
                    ]
                )
            )
        ]
    )