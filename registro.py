import flet as ft

def registro_view(page):
    # Paleta de Colores
    CP = "#D35400" # Naranja
    CS = "#5D4037" # Café
    CF = "#FCF8F4" # Fondo Crema

    return ft.View(
        "/registro",
        bgcolor=CF,
        padding=0,
        controls=[
            # Barra Superior
            ft.AppBar(
                leading=ft.IconButton(
                    ft.icons.ARROW_BACK_IOS_NEW, 
                    icon_color="white",
                    on_click=lambda _: page.go("/")
                ),
                title=ft.Text("Crear Cuenta", color="white", weight="bold"),
                bgcolor=CS,
                center_title=True,
            ),
            
            ft.Container(
                padding=25,
                content=ft.Column(
                    scroll=ft.ScrollMode.ALWAYS, # Permite bajar si el teclado estorba
                    spacing=15,
                    controls=[
                        ft.Text(
                            "Únete a Lupa Urbana", 
                            size=22, 
                            weight="bold", 
                            color=CS
                        ),
                        
                        # Campo: Nombre
                        ft.TextField(
                            label="Nombre Completo",
                            border_color=CS,
                            focused_border_color=CP,
                            prefix_icon=ft.icons.PERSON_ADD_ALT_1,
                        ),

                        # Campo: Ubicación
                        ft.TextField(
                            label="Colonia / Sector",
                            border_color=CS,
                            focused_border_color=CP,
                            prefix_icon=ft.icons.LOCATION_CITY,
                        ),

                        # Selector de Rol (Vecino o Jefe)
                        ft.Dropdown(
                            label="¿Cuál es tu rol?",
                            border_color=CS,
                            focused_border_color=CP,
                            label_style=ft.TextStyle(color=CS),
                            options=[
                                ft.dropdown.Option("Vecino"),
                                ft.dropdown.Option("Jefe de Manzana"),
                            ],
                        ),

                        ft.Divider(height=10, color="transparent"),

                        # Sección de Evidencia
                        ft.Text(
                            "Evidencia de Domicilio (INE o Comprobante)", 
                            size=14, 
                            color=CS,
                            weight="bold"
                        ),
                        
                        ft.ElevatedButton(
                            "SUBIR DOCUMENTO",
                            icon=ft.icons.UPLOAD_FILE,
                            width=400,
                            style=ft.ButtonStyle(
                                bgcolor=CS,
                                color="white",
                                shape=ft.RoundedRectangleBorder(radius=10)
                            ),
                            on_click=lambda _: print("Abriendo selector de archivos...")
                        ),

                        ft.Container(height=10),

                        # Botón Finalizar
                        ft.ElevatedButton(
                            "REGISTRARME",
                            width=400,
                            height=55,
                            style=ft.ButtonStyle(
                                color="white",
                                bgcolor=CP,
                                shape=ft.RoundedRectangleBorder(radius=12),
                            ),
                            on_click=lambda _: page.go("/dashboard")
                        ),
                        
                        ft.Row(
                            alignment="center",
                            controls=[
                                ft.Checkbox(check_color="white", active_color=CP),
                                ft.Text("Acepto términos y condiciones", size=12, color=CS)
                            ]
                        )
                    ]
                )
            )
        ]
    )