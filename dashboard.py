import flet as ft

def dashboard_view(page):
    # Paleta de Colores
    CP = "#D35400" # Naranja
    CS = "#5D4037" # Café
    CF = "#FCF8F4" # Fondo Crema

    return ft.View(
        "/dashboard",
        bgcolor=CF,
        padding=0,
        controls=[
            # Barra Superior (AppBar)
            ft.AppBar(
                title=ft.Text("Lupa Urbana", color="white", weight="bold"),
                bgcolor=CS,
                automatically_imply_leading=False, # Quita la flecha de atrás
                actions=[
                    ft.IconButton(ft.icons.NOTIFICATIONS_NONE, icon_color="white"),
                    ft.IconButton(ft.icons.SETTINGS, icon_color="white"),
                ],
            ),
            
            ft.Container(
                padding=20,
                content=ft.Column(
                    spacing=25,
                    controls=[
                        # Saludo
                        ft.Text(
                            "¡Hola de nuevo!", 
                            size=26, 
                            weight="bold", 
                            color=CS
                        ),
                        
                        ft.Text(
                            "¿Qué deseas revisar en tu comunidad?", 
                            size=16, 
                            color="#3E2723"
                        ),

                        # FILA DE BOTONES CIRCULARES (Tu Boceto 6)
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                # Botón MAPA
                                ft.Column([
                                    ft.FloatingActionButton(
                                        icon=ft.icons.MAP, 
                                        bgcolor=CP,
                                        on_click=lambda _: print("Abriendo Mapa...")
                                    ),
                                    ft.Text("MAPA", size=12, weight="bold", color=CS)
                                ], horizontal_alignment="center"),

                                # Botón CHATS
                                ft.Column([
                                    ft.FloatingActionButton(
                                        icon=ft.icons.CHAT_BUBBLE, 
                                        bgcolor=CP,
                                        on_click=lambda _: print("Abriendo Chats...")
                                    ),
                                    ft.Text("CHATS", size=12, weight="bold", color=CS)
                                ], horizontal_alignment="center"),

                                # Botón QUEJAS
                                ft.Column([
                                    ft.FloatingActionButton(
                                        icon=ft.icons.CAMPAIGN, 
                                        bgcolor=CP,
                                        on_click=lambda _: print("Abriendo Quejas...")
                                    ),
                                    ft.Text("QUEJAS", size=12, weight="bold", color=CS)
                                ], horizontal_alignment="center"),
                            ]
                        ),

                        ft.Divider(height=20, color=CS),

                        # Lista de Reportes Recientes
                        ft.Row(
                            alignment="spaceBetween",
                            controls=[
                                ft.Text("REPORTES RECIENTES", weight="bold", color=CS),
                                ft.TextButton("Ver todo", style=ft.ButtonStyle(color=CP))
                            ]
                        ),

                        # Ejemplo de una Tarjeta de Reporte
                        ft.Card(
                            color="white",
                            elevation=2,
                            content=ft.Container(
                                padding=15,
                                content=ft.ListTile(
                                    leading=ft.Icon(ft.icons.LIGHTBULB, color=CP, size=35),
                                    title=ft.Text("Luz fundida en Calle 5", weight="bold"),
                                    subtitle=ft.Text("Estado: Enviado • Hace 2 horas"),
                                    trailing=ft.Icon(ft.icons.ARROW_FORWARD_IOS, size=15, color=CS),
                                )
                            )
                        ),
                    ]
                )
            ),
            
            # Barra de Navegación Inferior
            ft.NavigationBar(
                bgcolor="white",
                destinations=[
                    ft.NavigationDestination(icon=ft.icons.HOME, label="Inicio"),
                    ft.NavigationDestination(icon=ft.icons.LOCATION_ON, label="Mapa"),
                    ft.NavigationDestination(icon=ft.icons.PERSON, label="Perfil"),
                ],
            )
        ]
    )