import os
import re

def ResultadoPDF(listaOperaciones, listaResultados):
    #variable auxiliara para tener siempre cadena 
    no_operaciones = len(listaOperaciones)
    print("cantidad de operaciones: "+str(no_operaciones))

    #Iniciando estructura Grapviz
    texto ="digraph {\n"
    texto += "\trankdir=LR\n"

    for operacion in listaOperaciones:
        operacion = re.sub("\+","Suma",operacion)
        operacion = re.sub("\*","Multiplicacion",operacion)
        operacion = re.sub("\(|\)","",operacion)
        resul = operacion.split()
        if "Suma" in resul:
            print("si esta suma")
        for i in resul:
            print(str(i))

    # resultado[0] = re.sub("\(|\)","",resultado[0])  #eliminar caracteres espesificos de una cadena 
    # print("Aqui se creara el pdf con los resultados")
    # texto ="graph {\n"
    # texto += "\trankdir=LR\n"
    # for nodo in aux_cadena:
    #     texto += f"\t{str(nodo)}[shape=circle style=filled color = blue]\n"
    # texto +="}\n"
    
    file = open("grafo.dot", "w")
    file.write(texto)
    file.close
    os.system("dot -Tpdf grafo.dot -o  grafo.pdf")

# b [shape=circle style=filled color=blue]
    # # abrir archivo modo escritura
    # file = open("grafo.dot", "w")
    # # escribir en el archivo el grafo
    # file.write()
    # #@ cerrar el archivo
    # file.close()
    # # ejecutar el comando dot 
    # os.system("dot -Tpdf grafo.dot -o  grafo.pdf")



        # resultado[0] = re.sub("\(|\)","",resultado[0])  #eliminar caracteres espesificos de una cadena 
        # contenido = resultado[0].split()

        # if '+' in contenido:
        #     print("Es suma")