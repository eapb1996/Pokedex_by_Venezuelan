import tkinter as tk
from pathlib import Path
from tkinter import ttk
from Library.librerias import recoger_sesion, drop_sesion

# Rutas relativas de las imágenes
ASSETS_PATH = Path(r"C:\Pokedex_by_Venezuelan\assets")

# Función para asignar la ruta a las imágenes
def relative_to_assets(path: str) -> Path:
    
    full_path = ASSETS_PATH / Path(path)
    if not full_path.exists():
        raise FileNotFoundError(f"Image not found: {full_path}")
    return full_path

# Clase principal de la aplicación
class Balls(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pokedex")
        self.geometry("1366x768")
        self.container = tk.Frame(self)
        self.resizable(False, False)  # No permitir cambiar el tamaño de la ventana
        self.container.pack(fill="both", expand=True)
        self.current_frame = None
        self.iconbitmap(relative_to_assets('PokeBall.ico'))
        self.show_frame(SecondaryPage)

    def show_frame(self, page_class):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.current_frame = page_class(self.container, self)
        self.current_frame.pack(fill="both", expand=True)

    def open(self):
        self.mainloop()

class SecondaryPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        main_page = Main_PW(self, controller)
        main_page.pack(fill="both", expand=True)

class Main_PW(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        usuario=recoger_sesion()
        self.usuario=usuario
        self.config(bg="#FFFFFF")
        self.create_widgets()

    def create_widgets(self):
        self.images = {}
        canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Cargar y almacenar las imágenes
        self.images["image_1"] = tk.PhotoImage(file=relative_to_assets("main_relleno_lateral.png"))
        canvas.create_image(107.0, 412.0, image=self.images["image_1"])

        self.images["image_2"] = tk.PhotoImage(file=relative_to_assets("main_relleno_general.png"))
        canvas.create_image(789.0, 413.0, image=self.images["image_2"])

        self.images["image_3"] = tk.PhotoImage(file=relative_to_assets("main_barra.png"))
        canvas.create_image(682.0, 29.0, image=self.images["image_3"])

        self.images["button_volver"] = tk.PhotoImage(file=relative_to_assets("main_boton_volver.png"))
        tk.Button(
            self,
            image=self.images["button_volver"],
            borderwidth=0,
            highlightthickness=0,
            activebackground="#E83030",
            command=lambda: self.open_seleccion(),
            relief="flat"
        ).place(x=1135.0, y=15.0, width=208.0, height=29.0)
        
        self.images["registrar"] = tk.PhotoImage(file=relative_to_assets("main_boton_registrar.png"))
        tk.Button(
            self,
            image=self.images["registrar"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame(Registrar),
            relief="flat"
        ).place(x=1.0, y=57.0, width=213.0, height=58.0)

        self.images["button_image_2"] = tk.PhotoImage(file=relative_to_assets("main_boton_modificar.png"))
        tk.Button(
            self,
            image=self.images["button_image_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame(Modificar),
            relief="flat"
        ).place(x=1.0, y=173.0, width=213.0, height=58.0)

        self.images["button_image_3"] = tk.PhotoImage(file=relative_to_assets("main_boton_listado.png"))
        tk.Button(
            self,
            image=self.images["button_image_3"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        ).place(x=1.0, y=115.0, width=213.0, height=58.0)

        self.images["button_image_4"] = tk.PhotoImage(file=relative_to_assets("main_boton_eliminar.png"))
        tk.Button(
            self,
            image=self.images["button_image_4"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame(Eliminar),
            relief="flat"
        ).place(x=1.0, y=231.0, width=213.0, height=58.0)

    def open_seleccion(self):
        self.controller.destroy()  ##### Cierra solo la ventana  actual
        from Vistas.R_selection import selection
        selection().open() 

class Registrar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        usuario=recoger_sesion()
        self.usuario=usuario
        self.controller = controller
        self.config(bg="#FFFFFF")
        self.create_widgets()

    def create_widgets(self):
        self.images = {}  # Diccionario para almacenar las imagenes

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Cargar y almacenar las imagenes
        self.images["image_1"] = tk.PhotoImage(file=relative_to_assets("main_relleno_lateral.png"))
        canvas.create_image(107.0, 412.0, image=self.images["image_1"])

        self.images["image_2"] = tk.PhotoImage(file=relative_to_assets("main_relleno_general.png"))
        canvas.create_image(789.0, 413.0, image=self.images["image_2"])

        self.images["image_3"] = tk.PhotoImage(file=relative_to_assets("main_barra.png"))
        canvas.create_image(682.0, 29.0, image=self.images["image_3"])

        # Cargar y almacenar las imagenes
        self.images["button_volver"] = tk.PhotoImage(file=relative_to_assets("main_boton_volver.png"))
        tk.Button(
            self,
            image=self.images["button_volver"],
            borderwidth=0,
            highlightthickness=0,
            activebackground="#E83030",
            command=lambda: None,
            relief="flat"
        ).place(x=1135.0, y=15.0, width=208.0, height=29.0)
        
        self.images["button_image_5"] = tk.PhotoImage(file=relative_to_assets("main_boton_registrar.png"))
        tk.Button(
            self,
            image=self.images["button_image_5"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: {self.hide_widgets(), self.controller.show_frame(Registrar)},
            relief="flat"
        ).place(x=1.0, y=57.0, width=213.0, height=58.0)

        self.images["button_image_2"] = tk.PhotoImage(file=relative_to_assets("main_boton_modificar.png"))
        tk.Button(
            self,
            image=self.images["button_image_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: {self.controller.show_frame(Modificar)},
            relief="flat"
        ).place(x=1.0, y=173.0, width=213.0, height=58.0)

        self.images["button_image_3"] = tk.PhotoImage(file=relative_to_assets("main_boton_listado.png"))
        tk.Button(
            self,
            image=self.images["button_image_3"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        ).place(x=1.0, y=115.0, width=213.0, height=58.0)

        self.images["button_image_4"] = tk.PhotoImage(file=relative_to_assets("main_boton_eliminar.png"))
        tk.Button(
            self,
            image=self.images["button_image_4"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: {self.controller.show_frame(Eliminar)},
            relief="flat"
        ).place(x=1.0, y=231.0, width=213.0, height=58.0)
        
        #Formulario para el registro
        
        # Titulos de los inputs
        canvas.create_text(263.0, 106.0, anchor="nw", text="Ingrese la información del pokemon a agregar", fill="#4C4C4C", font=("Montserrat Medium", 15))
        canvas.create_text(805.0, 152.0, anchor="nw", text="Subir imagen pokemon", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(263.0, 152.0, anchor="nw", text="Nombre", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(520.0, 149.0, anchor="nw", text="Tipo", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(263.0, 252.0, anchor="nw", text="Peso", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(520.0, 252.0, anchor="nw", text="Altura", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(779.0, 253.0, anchor="nw", text="Sexo", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(263.0, 352.0, anchor="nw", text="Descripción", fill="#000000", font=("Montserrat Regular", 15))
        #-------------------------------------------------------------------------------------
        # Crear y colocar los widgets
        nombre = tk.Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, borderwidth=0.5, relief="solid").place(x=520.0, y=282.0, width=237.0, height=38.0)

        peso = tk.Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, borderwidth=0.5, relief="solid").place(x=263.0, y=182.0, width=237.0, height=38.0)

        altura = tk.Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, borderwidth=0.5, relief="solid").place(x=263.0, y=282.0, width=237.0, height=37.5)
        
        #Select tipo de pokemon
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox",
                        fieldbackground="#FFFFFF",  # Fondo del campo de entrada
                        background="#FF0000",  # Fondo del desplegable
                        bordercolor="#000716",  # Color del borde
                        arrowcolor="#FFFFFF",  # Color de la flecha
                        padding= "9",
                        ) # padding para agrandar la altura del select
        
        pokemon_types = [
        "Agua", "Bicho", "Dragón", "Eléctrico", "Fuego", "Hada", "Hielo",
        "Lucha", "Normal", "Planta", "Psíquico", "Roca", "Siniestro", "Tierra",
        "Veneno", "Volador"
        ]
        
        tipos_de_pokemones = ttk.Combobox(self, values=pokemon_types, state="readonly", width=30, font=("Montserrat Medium", 10)).place(x=520.0, y=181.5)
        #-------------------------------------------------------------------------------
        # Select sexo del pokemon
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox",
                        fieldbackground="#FFFFFF",  # Fondo del campo de entrada
                        background="#FF0000",  # Fondo del desplegable
                        bordercolor="#000716",  # Color del borde
                        arrowcolor="#FFFFFF",  # Color de la flecha
                        padding= "9",
                        ) # padding para agrandar la altura del select
        
        pokemon_sex = ["Masculino", "Femenino"]
        
        tipos_de_sexo = ttk.Combobox(self, values=pokemon_sex, state="readonly", width=30, font=("Montserrat Medium", 10)).place(x=779.0, y=282.0)
        #-------------------------------------------------------------------------------
        # TextArea
        text_area = tk.Text(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, wrap=tk.WORD)
        text_area.place(x=265.0, y=382.0, width=751.0, height=238.0)
        
        # Ajustar la apariencia del Text widget para que se parezca al Entry
        text_area.config(font=("Montserrat Medium", 10), padx=10, pady=10, borderwidth=0.5, relief="solid")
        #-------------------------------------------------------------------------------
        # Cargar y almacenar las imágenes
        self.images['boton_R'] = tk.PhotoImage(file=relative_to_assets("R_Boton_registrar.png"))
        self.images['pokebola_off'] = tk.PhotoImage(file=relative_to_assets("R_Pokebola_off.png"))
        self.images['pokebola_on'] = tk.PhotoImage(file=relative_to_assets("R_Pokebola_on.png"))
        
         # Inicializar la variable booleana
        self.change_pokeball = False
        
        # Crear el botón con la imagen inicial
        self.button = tk.Button(
            self,
            image=self.images["pokebola_off"],
            background="#ffffff",        # Fondo del botón
            activebackground="#ffffff",  # Fondo del botón cuando está activo
            relief="flat",               # Sin relieve en el botón
            bd=0,                        # Sin borde en el botón
            command=lambda:activar_otra_pokebola(self)
        )
        self.button.place(x=870.0, y=177.0)

        #Funcion para activar el color de la pokebola
        def activar_otra_pokebola(self):
            # Cambiar el estado de la variable booleana
            self.change_pokeball = not self.change_pokeball
        
            # Actualizar la imagen del botón según el estado de la variable
            if self.change_pokeball:
                self.button.config(image=self.images["pokebola_on"])
            else:
                self.button.config(image=self.images["pokebola_off"])

        # Crear el botón
        boton_R = self.images['boton_R']
        tk.Button(
            self,
            image=boton_R,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("B_registrar clicked"),
            relief="flat",
        ).place(x=265.0, y=635.0, width=130.0, height=40.0)
        
        canvas.create_text(
            226.0,
            5.0,
            anchor="nw",
            text="Pokédex",
            fill="#000000",
            font=("Inter", 40 * -1)
        )
        canvas.create_text(
            26.0,
            9.0,
            anchor="nw",
            text=self.usuario,
            fill="#000000",
            font=("Inter", 18 * -1)
        )
        canvas.create_text(
            26.0,
            31.0,
            anchor="nw",
            text="Admin",
            fill="#000000",
            font=("Inter", 14 * -1)
        )
        
     # Guarda el canvas para poder ocultarlo
        self.canvas = canvas
        
    def hide_widgets(self):
        self.button_registrar.place_forget()
        self.button_volver.place_forget()
        self.button_modificar.place_forget()
        self.button_listado.place_forget()
        self.button_eliminar.place_forget()
        self.input_nombre.place_forget()
        self.button_e.place_forget()
        self.canvas.itemconfigure(self.label_info, state='hidden')
        self.canvas.itemconfigure(self.label_nombre, state='hidden')
        self.canvas.itemconfigure(self.navbar_title, state='hidden')
        self.canvas.itemconfigure(self.navbar_subtitle_1, state='hidden')
        self.canvas.itemconfigure(self.navbar_subtitle_2, state='hidden')

class Eliminar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        usuario=recoger_sesion()
        self.usuario=usuario
        self.config(bg="#FFFFFF")
        self.create_widgets()

    def create_widgets(self):
        self.images = {}  # Diccionario para almacenar las imágenes

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Cargar y almacenar las imágenes de las esquinas
        self.images["image_1"] = tk.PhotoImage(file=relative_to_assets("main_relleno_lateral.png"))
        canvas.create_image(107.0, 412.0, image=self.images["image_1"])

        self.images["image_2"] = tk.PhotoImage(file=relative_to_assets("main_relleno_general.png"))
        canvas.create_image(789.0, 413.0, image=self.images["image_2"])

        self.images["image_3"] = tk.PhotoImage(file=relative_to_assets("main_barra.png"))
        canvas.create_image(682.0, 29.0, image=self.images["image_3"])

        # Cargar y almacenar las imágenes de los botones
        self.images["button_image_5"] = tk.PhotoImage(file=relative_to_assets("main_boton_registrar.png"))
        self.button_registrar = tk.Button(
            self,
            image=self.images["button_image_5"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: {self.hide_widgets(), self.controller.show_frame(Registrar)},
            relief="flat"
        )
        self.button_registrar.place(x=1.0, y=57.0, width=213.0, height=58.0)
        
        self.images["button_image_1"] = tk.PhotoImage(file=relative_to_assets("main_boton_volver.png"))
        self.button_volver = tk.Button(
            self,
            image=self.images["button_image_1"],
            borderwidth=0,
            activebackground="#E83030",
            highlightthickness=0,
            relief="flat"
        )
        self.button_volver.place(x=1135.0, y=15.0, width=208.0, height=29.0)

        self.images["button_image_2"] = tk.PhotoImage(file=relative_to_assets("main_boton_modificar.png"))
        self.button_modificar = tk.Button(
            self,
            image=self.images["button_image_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: {self.hide_widgets(), self.controller.show_frame(Modificar)},
            relief="flat"
        )
        self.button_modificar.place(x=1.0, y=173.0, width=213.0, height=58.0)

        self.images["button_image_3"] = tk.PhotoImage(file=relative_to_assets("main_boton_listado.png"))
        self.button_listado = tk.Button(
            self,
            image=self.images["button_image_3"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_listado.place(x=1.0, y=115.0, width=213.0, height=58.0)

        self.images["button_image_4"] = tk.PhotoImage(file=relative_to_assets("main_boton_eliminar.png"))
        self.button_eliminar = tk.Button(
            self,
            image=self.images["button_image_4"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: {self.controller.show_frame(Eliminar)},
            relief="flat"
        )
        self.button_eliminar.place(x=1.0, y=231.0, width=213.0, height=58.0)
        
        # Formulario para el eliminar
        self.label_info = canvas.create_text(263.0, 106.0, anchor="nw", text="Ingrese la información del pokemon a Eliminar", fill="#4C4C4C", font=("Montserrat Medium", 15))
        
        # Texto para el nombre
        self.label_nombre = canvas.create_text(263.0, 152.0, anchor="nw", text="Nombre", fill="#000000", font=("Montserrat Regular", 15))
        
        self.input_nombre = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0, 
            borderwidth=0.5, 
            relief="solid"
        )
        self.input_nombre.place(x=263.0, y=182.0, width=237.0, height=38.0)
        
        # Cargar y almacenar las imágenes
        self.images['boton_Eliminar_f'] = tk.PhotoImage(file=relative_to_assets("Boton_eliminar.png"))
        
        # Cargar y almacenar la imagen del botón
        self.button_e = tk.Button(
            image=self.images['boton_Eliminar_f'],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_e.place(x=265.0, y=264.0, width=130.0, height=40.0)
        
        # Texto del navbar
        self.navbar_title = canvas.create_text(226.0, 5.0, anchor="nw", text="Pokédex", fill="#000000", font=("Inter", 40 * -1))
        self.navbar_subtitle_1 = canvas.create_text(26.0, 9.0, anchor="nw", text=self.usuario, fill="#000000", font=("Inter", 18 * -1))
        self.navbar_subtitle_2 = canvas.create_text(26.0, 31.0, anchor="nw", text="Admin", fill="#000000", font=("Inter", 14 * -1))

        # Guarda el canvas para poder ocultarlo
        self.canvas = canvas
        
    def hide_widgets(self):
        self.button_registrar.place_forget()
        self.button_volver.place_forget()
        self.button_modificar.place_forget()
        self.button_listado.place_forget()
        self.button_eliminar.place_forget()
        self.input_nombre.place_forget()
        self.button_e.place_forget()
        self.canvas.itemconfigure(self.label_info, state='hidden')
        self.canvas.itemconfigure(self.label_nombre, state='hidden')
        self.canvas.itemconfigure(self.navbar_title, state='hidden')
        self.canvas.itemconfigure(self.navbar_subtitle_1, state='hidden')
        self.canvas.itemconfigure(self.navbar_subtitle_2, state='hidden')

class Modificar(tk.Frame):
    def __init__(self, parent, controller):
        usuario=recoger_sesion()
        self.usuario=usuario
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#FFFFFF")
        self.create_widgets()

    def create_widgets(self):
        self.images = {}  # Diccionario para almacenar las imagenes

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Cargar y almacenar las imagenes
        self.images["image_1"] = tk.PhotoImage(file=relative_to_assets("main_relleno_lateral.png"))
        canvas.create_image(107.0, 412.0, image=self.images["image_1"])

        self.images["image_2"] = tk.PhotoImage(file=relative_to_assets("main_relleno_general.png"))
        canvas.create_image(789.0, 413.0, image=self.images["image_2"])

        self.images["image_3"] = tk.PhotoImage(file=relative_to_assets("main_barra.png"))
        canvas.create_image(682.0, 29.0, image=self.images["image_3"])

        # Cargar y almacenar las imagenes
        self.images["button_volver"] = tk.PhotoImage(file=relative_to_assets("main_boton_volver.png"))
        tk.Button(
            self,
            image=self.images["button_volver"],
            activebackground="#E83030",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        ).place(x=1135.0, y=15.0, width=208.0, height=29.0)
        
        self.images["button_image_5"] = tk.PhotoImage(file=relative_to_assets("main_boton_registrar.png"))
        tk.Button(
            self,
            image=self.images["button_image_5"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: {self.controller.show_frame(Registrar)},
            relief="flat"
        ).place(x=1.0, y=57.0, width=213.0, height=58.0)

        self.images["button_image_2"] = tk.PhotoImage(file=relative_to_assets("main_boton_modificar.png"))
        tk.Button(
            self,
            image=self.images["button_image_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: {self.hide_widgets(), self.controller.show_frame(Modificar)},
            relief="flat"
        ).place(x=1.0, y=173.0, width=213.0, height=58.0)

        self.images["button_image_3"] = tk.PhotoImage(file=relative_to_assets("main_boton_listado.png"))
        tk.Button(
            self,
            image=self.images["button_image_3"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        ).place(x=1.0, y=115.0, width=213.0, height=58.0)

        self.images["button_image_4"] = tk.PhotoImage(file=relative_to_assets("main_boton_eliminar.png"))
        tk.Button(
            self,
            image=self.images["button_image_4"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: {self.controller.show_frame(Eliminar)},
            relief="flat"
        ).place(x=1.0, y=231.0, width=213.0, height=58.0)
        
        #Formulario para el registro
        
        # Titulos de los inputs
        canvas.create_text(263.0, 106.0, anchor="nw", text="Ingrese la información del pokemon a modificar", fill="#4C4C4C", font=("Montserrat Medium", 15))
        canvas.create_text(805.0, 152.0, anchor="nw", text="Subir imagen pokemon", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(263.0, 152.0, anchor="nw", text="Nombre", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(520.0, 149.0, anchor="nw", text="Tipo", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(263.0, 252.0, anchor="nw", text="Peso", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(520.0, 252.0, anchor="nw", text="Altura", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(779.0, 253.0, anchor="nw", text="Sexo", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(263.0, 352.0, anchor="nw", text="Descripción", fill="#000000", font=("Montserrat Regular", 15))
        #-------------------------------------------------------------------------------------
        # Crear y colocar los widgets
        nombre = tk.Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, borderwidth=0.5, relief="solid").place(x=520.0, y=282.0, width=237.0, height=38.0)

        peso = tk.Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, borderwidth=0.5, relief="solid").place(x=263.0, y=182.0, width=237.0, height=38.0)

        altura = tk.Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, borderwidth=0.5, relief="solid").place(x=263.0, y=282.0, width=237.0, height=37.5)
        
        #Select tipo de pokemon
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox",
                        fieldbackground="#FFFFFF",  # Fondo del campo de entrada
                        background="#FF0000",  # Fondo del desplegable
                        bordercolor="#000716",  # Color del borde
                        arrowcolor="#FFFFFF",  # Color de la flecha
                        padding= "9",
                        ) # padding para agrandar la altura del select
        
        pokemon_types = [
        "Agua", "Bicho", "Dragón", "Eléctrico", "Fuego", "Hada", "Hielo",
        "Lucha", "Normal", "Planta", "Psíquico", "Roca", "Siniestro", "Tierra",
        "Veneno", "Volador"
        ]
        
        tipos_de_pokemones = ttk.Combobox(self, values=pokemon_types, state="readonly", width=30, font=("Montserrat Medium", 10)).place(x=520.0, y=181.5)
        #-------------------------------------------------------------------------------
        # Select sexo del pokemon
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox",
                        fieldbackground="#FFFFFF",  # Fondo del campo de entrada
                        background="#FF0000",  # Fondo del desplegable
                        bordercolor="#000716",  # Color del borde
                        arrowcolor="#FFFFFF",  # Color de la flecha
                        padding= "9",
                        ) # padding para agrandar la altura del select
        
        pokemon_sex = ["Masculino", "Femenino"]
        
        tipos_de_sexo = ttk.Combobox(self, values=pokemon_sex, state="readonly", width=30, font=("Montserrat Medium", 10)).place(x=779.0, y=282.0)
        #-------------------------------------------------------------------------------
        # TextArea
        text_area = tk.Text(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, wrap=tk.WORD)
        text_area.place(x=265.0, y=382.0, width=751.0, height=238.0)
        
        # Ajustar la apariencia del Text widget para que se parezca al Entry
        text_area.config(font=("Montserrat Medium", 10), padx=10, pady=10, borderwidth=0.5, relief="solid")
        #-------------------------------------------------------------------------------
        # Cargar y almacenar las imágenes
        self.images['boton_M'] = tk.PhotoImage(file=relative_to_assets("M_boton.png"))
        self.images['pokebola_off'] = tk.PhotoImage(file=relative_to_assets("R_Pokebola_off.png"))
        self.images['pokebola_on'] = tk.PhotoImage(file=relative_to_assets("R_Pokebola_on.png"))
        
         # Inicializar la variable booleana
        self.change_pokeball = False
        
        # Crear el botón con la imagen inicial
        self.button = tk.Button(
            self,
            image=self.images["pokebola_off"],
            background="#ffffff",        # Fondo del botón
            activebackground="#ffffff",  # Fondo del botón cuando está activo
            relief="flat",               # Sin relieve en el botón
            bd=0,                        # Sin borde en el botón
            command=lambda:activar_otra_pokebola(self)
        )
        self.button.place(x=870.0, y=177.0)

        #Funcion para activar el color de la pokebola
        def activar_otra_pokebola(self):
            # Cambiar el estado de la variable booleana
            self.change_pokeball = not self.change_pokeball
        
            # Actualizar la imagen del botón según el estado de la variable
            if self.change_pokeball:
                self.button.config(image=self.images["pokebola_on"])
            else:
                self.button.config(image=self.images["pokebola_off"])

        # Crear el botón
        boton_M = self.images['boton_M']
        tk.Button(
            self,
            image=boton_M,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("B_registrar clicked"),
            relief="flat",
        ).place(x=265.0, y=635.0, width=130.0, height=40.0)
        
        canvas.create_text(
            226.0,
            5.0,
            anchor="nw",
            text="Pokédex",
            fill="#000000",
            font=("Inter", 40 * -1)
        )
        canvas.create_text(
            26.0,
            9.0,
            anchor="nw",
            text=self.usuario,
            fill="#000000",
            font=("Inter", 18 * -1)
        )
        canvas.create_text(
            26.0,
            31.0,
            anchor="nw",
            text="Admin",
            fill="#000000",
            font=("Inter", 14 * -1)
        )
        
     # Guarda el canvas para poder ocultarlo
        self.canvas = canvas
        
    def hide_widgets(self):
        self.button_registrar.place_forget()
        self.button_volver.place_forget()
        self.button_modificar.place_forget()
        self.button_listado.place_forget()
        self.button_eliminar.place_forget()
        self.input_nombre.place_forget()
        self.button_e.place_forget()
        self.canvas.itemconfigure(self.label_info, state='hidden')
        self.canvas.itemconfigure(self.label_nombre, state='hidden')
        self.canvas.itemconfigure(self.navbar_title, state='hidden')
        self.canvas.itemconfigure(self.navbar_subtitle_1, state='hidden')
        self.canvas.itemconfigure(self.navbar_subtitle_2, state='hidden')

class Listado(tk.Frame):
    pass
       
# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = Balls()
    app.mainloop()