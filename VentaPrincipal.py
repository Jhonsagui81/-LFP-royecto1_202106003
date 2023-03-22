from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

#para poder analizar texto
from automata import Automata
from Operaciones import Operacion



ruta = ""
#Analizar
def Analizar():
    funcion = Automata()
    print("entra a analizar")
    
    contenido = caja_texto.get(1.0, 'end-1c')
    
    resultado = funcion.analizar(contenido, Operacion('suma'))
    
    funcion.imprimrResultados(resultado)

        # caja_texto.delete(1.0, END)
        # # autom.imprimir_tokens()
        # if funcion.estado_actual in funcion.estados_aceptacion:
        #     for oper in resultado[1]:
        #         resultado = oper.operar()
        #         print(resultado[0], "=", resultado[1])


#Guardar como...
def savefileas():    
    try:
        path = FileDialog.asksaveasfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
        root.title('Notepad - ' + path)
    
    except:
        return   
    
    with open(path, 'w') as f:
        f.write(caja_texto.get('1.0', END))

#Guardar en el mismo archivo 
def Guardar():
    if ruta != "":
        contenido = caja_texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
    else:
        savefileas()

#Abrir Archivo
def AbrirArchivo():
    print("HAs presionado para crear un nuevo archivo")
    global ruta

    mensaje.set('Abrir fichero')

    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(
        ("Ficheros de texto", "*.txt"),
        ),
        title= "Abrir un fichero"
    )

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        caja_texto.delete(1.0, 'end')
        caja_texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")


root = Tk()
root.title("MENU PRINCIPAL")
root.config(width=400, height=300, bg="White")


mensaje = StringVar()
monitor = Label(root, textvariable=mensaje, justify='right')
monitor.grid()
##CREAR CAJA DE TEXTO
caja_texto = Text(root)
caja_texto.grid(row=0, column=1)
caja_texto.config(width=40, height=20, bg="gray")

##CREAR BOTONES
etiqueta = Label(root, text="", bg="White").grid(row=1, column=1)
boton_analizar = Button(root, text="Analizar", bg="Blue", fg="White", padx=30, command=Analizar).grid(row=2, column=0)
boton_guardar = Button(root, text="Guardar", bg="Green", fg="White", padx=45, command=Guardar).grid(row=2, column=1)
boton_errores = Button(root, text="Errores", bg="Red", fg="White", padx=30).grid(row=2, column=2)

##CREAR BARRA DE MENU
barra_menu = Menu()
#Agregando items
menu_archivo = Menu(barra_menu, tearoff=False)

#Agregar funcionalidad en la primera opcion del menu
menu_archivo.add_command(
    label="Abrir",
    command=AbrirArchivo
)

menu_archivo.add_command(
    label="Guardar Como...",
    command=savefileas
)

menu_archivo.add_separator()
menu_archivo.add_command(
    label="Salir",
    command=root.destroy
)

##agregar opcion en la barra menu
barra_menu.add_cascade(menu=menu_archivo, label="Archivo")

#segundo item
menu_ayuda = Menu(barra_menu, tearoff=False)
#Agregando funcionalidad a la opcion
menu_ayuda.add_command(
    label="Manual de Usuario"
    #command = funcion 
)
menu_ayuda.add_command(
    label="Manual Tecnico"
    #command = funcion 
)
menu_ayuda.add_command(
    label="Temas de ayuda"
    #command = funcion 
)

barra_menu.add_cascade(menu=menu_ayuda, label="Ayuda")

#Insertar en la ventana
root.config(menu = barra_menu)
root.mainloop()