from tkinter import *
from tkinter.messagebox import *


root = Tk()  ##Crea ventana principal

##METODO GRID()
#se puede utilizar para darle un orden, caso contrario que con pack()
# etiqueta.grid(row=2, column=3)

etiqueta = Label(root, text="Primer ventana") #Crea el label
etiqueta.grid(row=0, column=0)  ## Hace que se vea el label en la ventana 

##WIDGETS
marco_principal = Frame() ##marco dentro para colocar cualquier cosa
marco_principal.grid(row=1, column=1) #lA venta se ajusta al tamanio de este

marco_principal.config(width="800", height="500")  #Aplicando modificaciones
marco_principal.config(bg="red")

#Funcionalidad al boton
def click_botom():
    texxto = Label(root, text=f'Se almaceno "{entrada.get()}" correctamente').grid(row=3, column=1)

##BOTONES
boton1 = Button(root, text="No me toques", bg="cyan", padx=50, pady=20, command=click_botom).grid(row=1, column=2) 

##CAJAS DE TEXTO
entrada = Entry(root, width=100, bg="yellow", fg="firebrick")
entrada.insert(0, "Escribe aqui...")
entrada.grid(row=2,column=1)

root.mainloop()  ##mantiene refrescando la ventana
