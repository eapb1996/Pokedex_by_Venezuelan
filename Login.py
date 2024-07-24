from pathlib import Path

from tkinter import Tk, Canvas, Entry, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Pokedex_by_Venezuelan\assets\frame0")

#Ruta reltiva que conecta las imagenes con el archivo Login
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Creamos un objeto usando la clase TK
#Se crea la instancia de esta clase TK
window = Tk()
#Cambiamos el nombre de la ventana
window.title("Login")
# Modificacamos el tamaño de la ventana (pixeles)
window.geometry("1366x768")
#Fondo de pantalla de la ventana
window.configure(bg = "#FFFFFF")
#Configuramos el icono de la aplicación
window.iconbitmap(relative_to_assets('PokeBall.ico'))

#Estilos globales de la ventana
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
#---------------------------------------
#Imagen superior de la pokebola
image_image_1 = PhotoImage(
    file=relative_to_assets("pokebola.png"))
image_1 = canvas.create_image(
    678.0,
    234.0,
    image=image_image_1
)
#---------------------------------------
#Frase superior
canvas.create_text(
    610.0,
    446.0,
    anchor="nw",
    text="Inicio de sesión",
    fill="#000000",
    font=("Montserrat Regular", 20 * -1)
)
#---------------------------------------
#Estilos de la imagen para el input (Usuario)
canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    683.0,
    525.0,
    image=entry_image_1
)
#---------------------------------------
#Estilos del input (Usuario)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=436.0,
    y=505.0,
    width=494.0,
    height=38.0
)
canvas.create_text(
    445.0,
    477.0,
    anchor="nw",
    text="Usuario",
    fill="#000000",
    font=("Montserrat Regular", 15 * -1)
)
#---------------------------------------
#Estilos de la imagen para el input (Contraseña)
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))

entry_bg_2 = canvas.create_image(
    683.0,
    605.0,
    image=entry_image_2
)
#---------------------------------------
#Estilos del input (Contraseña)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)

entry_2.place(
    x=436.0,
    y=585.0,
    width=494.0,
    height=38.0
)

canvas.create_text(
    445.0,
    557.0,
    anchor="nw",
    text="Contraseña",
    fill="#000000",
    font=("Montserrat Regular", 15 * -1)
)
#---------------------------------------
#Boton para iniciar sesión
button_image_1 = PhotoImage(
    file=relative_to_assets("Pokemon_button.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("presioanado"),
    relief="flat"
)
button_1.place(
    x=538.0,
    y=665.0,
    width=130.0,
    height=40.0
)
#---------------------------------------
#Boton para ingresar como invitado
button_image_2 = PhotoImage(
    file=relative_to_assets("Texto_boton.png"))

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)

button_2.place(
    x=713.0,
    y=676.0,
    width=156.0,
    height=18.0
)
#---------------------------------------
# Deshabilitar la capacidad de redimensionar la ventana
window.resizable(False, False)
#---------------------------------------
window.mainloop()
