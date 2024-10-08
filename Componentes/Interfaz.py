from tkinter import filedialog as FileDialog
from tkPDFViewer import tkPDFViewer as pdf
from io import open
import tkinter as tk
from tkinter import Toplevel

#para poder analizar texto
from Componentes.automata import Automata 
from Componentes.Operaciones import Operacion

#variables absolutas
ruta = ""

#Variables global para interfas
v1 = pdf.ShowPdf()
v3 = pdf.ShowPdf()
v5 = pdf.ShowPdf()
ventana = tk.Tk()
caja_texto = tk.Text(ventana, height=30, width=100)

# Función para abrir el Manual Tecnico
def abrir_Tecnico():
    # Crear una nueva ventana emergente para mostrar el PDF
    ventana_Tecnico = Toplevel(ventana)
    ventana_Tecnico.title("Manual Tecnico")
    ventana_Tecnico.geometry("630x700+400+100")
    ventana_Tecnico.configure(bg="White")

    # # Abrir el archivo PDF
    # filename = FileDialog.askopenfilename(initialdir=os.getcwd(),
    #                                     title="select pdf file",
    #                                     filetypes = (("PDF File","*.pdf"),
    #                                                 ("PDF File","*.PDF"),
    #                                                 ("All file","*.txt")))
    v3.img_object_li.clear()
    v5.img_object_li.clear()
    v2 = v1.pdf_view(ventana_Tecnico, pdf_location=open("/home/jhonatan/Documentos/Universidad_USAC/Semestre5/01_LenguajesFormales/Proyecto1/Documentacion/ManualTecnico.pdf", "r"),width=77, height=100)
    
    v2.pack(pady=(0,0))

# Funcion para abrir el Manual de Usuario
def abrir_Usuario():
    # Crear una nueva ventana emergente para mostrar el PDF
    ventana_pdf = Toplevel(ventana)
    ventana_pdf.title("Manual de Usuario")
    ventana_pdf.geometry("630x700+400+100")
    ventana_pdf.configure(bg="White")
    
    v1.img_object_li.clear()
    v5.img_object_li.clear()
    v4 = v3.pdf_view(ventana_pdf, pdf_location=open("/home/jhonatan/Documentos/Universidad_USAC/Semestre5/01_LenguajesFormales/Proyecto1/Documentacion/MANUAL_DE_USUARIO.pdf", "r"),width=77, height=100)
    v4.pack(pady=(0,0))

def abrir_Ayuda():
    # Crear una nueva ventana emergente para mostrar el PDF
    ventana_pdf = Toplevel(ventana)
    ventana_pdf.title("Informacion")
    ventana_pdf.geometry("630x700+400+100")
    ventana_pdf.configure(bg="White")
    
    v1.img_object_li.clear()
    v3.img_object_li.clear()
    v4 = v3.pdf_view(ventana_pdf, pdf_location=open("/home/jhonatan/Documentos/Universidad_USAC/Semestre5/01_LenguajesFormales/Proyecto1/Documentacion/INFORMACION_DESARROLLADOR.pdf", "r"),width=77, height=100)
    v4.pack(pady=(0,0))
#Analizar
def Analizar():
    funcion = Automata()  #objeto tipo Automata
    operacion = Operacion('Error')
    contenido = caja_texto.get(1.0, 'end-1c') #Extrae contenido de la caja (Interfaz)
    
    funcion.reiniciando()
    operacion.Reiniciando()

    resultado = funcion.analizar(contenido, Operacion('suma'))  #Se llama al automata y se le pasa lo extraido.  REtorna valores
    lista_errores = funcion.imprimir_errores()  #REtorna la lista de errores 
    # lista_errores_logicos = funcion.ErrorLogico(resultado)

    #Borrar datos del doc 
    texto = ''
    #Si hay errores -> no pdf 
    if len(lista_errores) == 0:
        print("No hay errores")
        # if len(lista_errores_logicos) == 0:
        # print("No hay errores")
        funcion.imprimrResultados(resultado)
        # else:
        #     print("Si hay errores")
        #     caja_texto.delete(1.0, tk.END)
        #     caja_texto.insert(1.0, "ALERTA: Existen ERRORES LOGICOS en el documento, De clic en el boton 'Errores' para ver los detalles")

        #     for log in lista_errores_logicos:
        #         texto += '{\n'
        #         texto += '\t{\n'
        #         texto += f'\t\t"No.":{log.id}\n'
        #         texto += '\t\t"Descripcion-Token":{ \n'
        #         texto += f'\t\t\t"Lexema": {log.lexema}\n'
        #         texto += f'\t\t\t"Tipo": {log.tipoError}\n'
        #         texto += f'\t\t\t"Columna": {log.columna}\n'
        #         texto += f'\t\t\t"Fila": {log.fila}\n'
        #         texto += '\t\t}\n'
        #         texto += '\t},\n'
        #     texto += '}\n'
        #     operacion.Reiniciando()
        #     lista_errores_logicos = []
        #     print(texto)
        #     file = open("./Documentacion/Errores.txt", "w")
        #     file.write(texto)
        #     file.close()
            
    else:
        print("Si hay errores")
        caja_texto.delete(1.0, tk.END)
        caja_texto.insert(1.0, "ALERTA: Existen errores en el documento, De clic en el boton 'Errores' para ver los detalles")
        
        for val in lista_errores:
            texto += '{\n'
            texto += '\t{\n'
            texto += f'\t\t"No.":{val.id}\n'
            texto += '\t\t"Descripcion-Token":{ \n'
            texto += f'\t\t\t"Lexema": {val.lexema}\n'
            texto += f'\t\t\t"Tipo": {val.tipoError}\n'
            texto += f'\t\t\t"Columna": {val.columna}\n'
            texto += f'\t\t\t"Fila": {val.fila}\n'
            texto += '\t\t}\n'
            texto += '\t},\n'
        texto += '}\n'
        print(texto)
        file = open("/home/jhonatan/Documentos/Universidad_USAC/Semestre5/01_LenguajesFormales/Proyecto1/Documentacion/Errores.txt", "w")
        file.write(texto)
        file.close()

    #si hay errores no pdf
    
#Abrir Archivo
def AbrirArchivoError():

    fichero = open("/home/jhonatan/Documentos/Universidad_USAC/Semestre5/01_LenguajesFormales/Proyecto1/Documentacion/Errores.txt", 'r')
    contenido = "Estos Son los errores detectados: \n\n"
    contenido += fichero.read()
    caja_texto.delete(1.0, 'end')
    caja_texto.insert('insert', contenido)
    fichero.close()
    ventana.title(ruta + " - Mi editor")

#Guardar como...
def savefileas():    
    try:
        path = FileDialog.asksaveasfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
        ventana.title('Notepad - ' + path)
    
    except:
        return   
    
    with open(path, 'w') as f:
        f.write(caja_texto.get('1.0', tk.END))

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
    global ruta

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
        ventana.title(ruta + " - Mi editor")

#Ventana Root
def Interfaz():
    ventana.title("MenuPrincipal")
    ventana.geometry("800x600")

    # Creamos la barra de menú
    barra_menu = tk.Menu(ventana)

    # Creamos las opciones de menú "Archivo" y "Ayuda"
    menu_archivo = tk.Menu(barra_menu, tearoff=False)
    menu_ayuda = tk.Menu(barra_menu, tearoff=False)

    # Agregamos las opciones de menú "Abrir", "Guardar Como" y "Salir" a la opción "Archivo"
    menu_archivo.add_command(label="Abrir", command=AbrirArchivo)
    menu_archivo.add_command(label="Guardar Como", command=savefileas)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=ventana.quit)

    # Agregamos las opciones de menú "Manual Técnico", "Manual de Usuario" y "Ayuda" a la opción "Ayuda"
    menu_ayuda.add_command(label="Manual Técnico", command=abrir_Tecnico)
    menu_ayuda.add_command(label="Manual de Usuario", command=abrir_Usuario)
    menu_ayuda.add_separator()
    menu_ayuda.add_command(label="Ayuda", command=abrir_Ayuda)

    # Agregamos las opciones de menú "Archivo" y "Ayuda" a la barra de menú
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

    # Configuramos la barra de menú en la ventana
    ventana.config(menu=barra_menu)

    # Creamos una caja de texto grande en la parte superior de la ventana
    caja_texto.pack()

    # Creamos tres botones en la parte inferior de la ventana
    boton1 = tk.Button(ventana, text="Analizar",bg="Blue",fg="White", height=5, width=20, command=Analizar)
    boton2 = tk.Button(ventana, text="Guardar",bg="Green",fg="White", height=5, width=20, command=Guardar)
    boton3 = tk.Button(ventana, text="Errores",bg="Red",fg="White", height=5, width=20, command=AbrirArchivoError)


    boton1.pack(side=tk.LEFT, padx=20, pady=20)
    boton2.pack(side=tk.LEFT, padx=20, pady=20)
    boton3.pack(side=tk.LEFT, padx=20, pady=20)


    # Establecemos la posición de los botones en la ventana
    boton1.pack(side="left")
    boton2.pack(side="left")
    boton3.pack(side="right")

    ventana.mainloop()
