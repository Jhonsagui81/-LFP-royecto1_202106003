import re
from TDA.Error import Error
import math

class Operacion:
    errores_tabla = []
    inidiceError = 0

    def __init__(self, tipo) :
        self.tipo = tipo 
        self.operandos = []  #lista los valores de la operacion
        self.texto = ''
        self.aux = 0
        


    def operar(self, id): 
        res = '' # 1 + (1 + 1) = 3      #describe la operacion string  
        resnum = 0          #resultado de la operacion
        tipo = ""
        cont_resta = 0
        cont_division = 0
        cont_potencia = 0
        cont_raiz = 0
        cont_inverso = 0
        cont_seno = 0
        cont_coseno = 0
        cont_tangente = 0
        
        #SUMA
        
        if self.tipo.lower() == 'suma':  
            tipo = "Suma"
            for operando in self.operandos:
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Suma"
                    res += operando + ' + '
                    resnum += round(float(operando), 2) #con flotante para evitar clavos
                    
                    #grafica
                    self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"

                    
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") + "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    resnum += operado[1]  #Se suma el resultado de la operacion anidada al total
                    
                    #Descomponer operacion anidada
                    operado[0] = re.sub("\+|\^|\√|\@|\#|\$|\%","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\*","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                    anidada = operado[0].split()    #se descompone 
                    for i in anidada:   #se itera 
                        self.aux += float(i)   #se crea el total interno 
                        self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                        self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                    self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3])+': '+ str(round(operado[1],2))}>]\n "  #crea subnodo del original
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
            #finaliza For
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n " #nodo original de cada operacion
        
        #RESTA
        elif self.tipo.lower() == 'resta':  
            tipo = "Resta"
            for operando in self.operandos:
                cont_resta +=1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Resta"
                    res += operando + ' - '
                    if cont_resta == 1:
                        resnum += round(float(operando), 2) #con flotante para evitar clavos
                    else:
                        resnum -= round(float(operando), 2)

                    #grafica
                    self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"

                    
                else:
                    
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") - "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    if cont_resta == 1:
                        resnum += operado[1]  #Se suma el resultado de la operacion anidada al total
                    else:
                        resnum -= operado[1]

                    #Descomponer operacion anidada
                    operado[0] = re.sub("\+|\^|\√|\@|\#|\$|\%","",operado[0]) #quita el signo  
                    operado[0] = re.sub("\-","",operado[0]) #quita el signo
                    operado[0] = re.sub("\*","",operado[0]) #quita el signo  
                    operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                    anidada = operado[0].split()    #se descompone 
                    for i in anidada:   #se itera 

                        self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                        self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                    self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3])+': '+ str(round(operado[1], 2))}>]\n "  #crea subnodo del original
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
            #finaliza For
            cont_resta = 0
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n " 

        #MULTIPLICACION
        elif self.tipo.lower() == 'multiplicacion':
            resnum = 1
            tipo = "Multiplicacion"
            for operando in self.operandos:
                # print("los valores: "+str(operando))
                if type(operando) is not Operacion:
                    #Grafica
                    tipo = "Multiplicacion"
                    self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                    self.texto += f"\t{str(tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"

                    res += operando + ' * '
                    resnum = resnum * round(float(operando), 2)

                    
                else:
                    operado = operando.operar(id) 
                    res += "(" + operado[0]+ ") * "
                    resnum = resnum * float(operado[1])
        
                    #Descomponer operacion anidada
                    operado[0] = re.sub("\+|\^|\√|\@|\#|\$|\%","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\*","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\(|\)|\'","",operado[0]) #quita el signo 
                    anidada = operado[0].split()    #se descompone 
                    #grafica
                    for i in anidada:   #se itera 
                        self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                        self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                    self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3]) +': '+ str(round(operado[1]))}>]\n "  #crea subnodo del original
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
            #termina for
            self.texto += f"\t{str(tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n "
        
        #Division
        elif self.tipo.lower() == 'division':  
            tipo = "division"
            for operando in self.operandos:
                cont_division += 1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "division"
                    if cont_division == 2:
                        if operando == "0":
                            #Pendiendteeee...
                            print("Se produjo un error logico")
                            self.inidiceError +=1
                            self.guardar_error('/', "Error Logico", self.inidiceError)
                        else:
                            #En caso sea el segundo valor
                            res += operando + ' / '
                            resnum /= round(float(operando), 2) #con flotante para evitar clavos
                    #En caso sea el primer valor
                    if cont_division == 1:
                        res += operando + ' / '
                        resnum += round(float(operando), 2)
                    #grafica
                    self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"

                    
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") / "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada

                    if cont_division == 2:
                        if operado[1] == 0:   #solucion problema division
                            #Pendiendteeee...
                            print("Se produjo un error logico")
                            self.inidiceError +=1
                            self.guardar_error('/', "Error Logico", self.inidiceError)
                        else:
                            #En caso sea el segundo valor un numero != 0
                            resnum /= operado[1]
                    #En caso sea el primer valor
                    if cont_division == 1:
                        resnum += operado[1] 
                    #Descomponer operacion anidada
                    operado[0] = re.sub("\+|\^|\√|\@|\#|\$|\%","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\*","",operado[0]) #quita el signo
                    operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                    anidada = operado[0].split()    #se descompone 
                    for i in anidada:   #se itera 
                        self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                        self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                    self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3])+':'+ str(round(operado[1]))}>]\n "  #crea subnodo del original
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
            #finaliza For.
            cont_division = 0
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n " #nodo original de cada operacion

        #Potencia math.pow(x,y)
        elif self.tipo.lower() == 'potencia':  
            tipo = "Potencia"
            for operando in self.operandos:
                cont_potencia += 1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Potencia"

                    if cont_potencia == 1:
                        res += operando + ' ^ '
                        resnum += round(float(operando), 2) #con flotante para evitar clavos
                    elif cont_potencia == 2:
                        res += operando + ' ^ '
                        aux = resnum
                        for ex in range(1, round(float(operando))):
                            resnum = resnum * aux #con flotante para evitar clavos

                    #grafica
                    self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"

                    
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") ^ "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada

                    if cont_potencia == 1:
                        resnum += operado[1]
                    #En caso sea el primer valor
                    else:
                        aux1 = resnum
                        for i in range(1,round(float(operado[1]))):
                            resnum = resnum * aux1 #con flotante para evitar clavos

                    #Descomponer operacion anidada
                    operado[0] = re.sub("\+|\^|\√|\@|\#|\$|\%","",operado[0]) #quita el signo  
                    operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\*","",operado[0]) #quita el signo
                    operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                    anidada = operado[0].split()    #se descompone 
                    for i in anidada:   #se itera 
                        self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                        self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                    self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3])+':'+ str(round(operado[1]))}>]\n "  #crea subnodo del original
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
            #finaliza For
            cont_potencia = 0
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n " #nodo original de cada operacion

        #Raiz math.sqrt(x)
        elif self.tipo.lower() == 'raiz':  
            tipo = "Raiz"
            for operando in self.operandos:
                cont_raiz += 1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Raiz" 

                    if cont_raiz == 1:
                        #if operando < 0  - ERRor
                        res += operando + ' √ '
                        resnum = math.sqrt(float(operando)) #con flotante para evitar clavos

                        #grafica
                        self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                        self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"
                    elif cont_raiz == 2:
                        #Error - Solo se permite 1 valor 
                        print("Error logico, solo se permite 1 valor xd")

                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") √ "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada

                    if cont_raiz == 1:
                        resnum = math.sqrt(operado[1]) 
                        #Grafica sub elementos 
                        operado[0] = re.sub("\+|\^|\√|\@|\#|\$|\%","",operado[0]) #quita el signo  
                        operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\*","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                        anidada = operado[0].split()    #se descompone 
                        for i in anidada:   #se itera 
                            self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                            self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                        self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3])+': '+ str(round(operado[1],2))}>]\n "  #crea subnodo del original
                        self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
                    else:
                        print("Error logico, solo se permite 1 valor rt")
                        #Pendiende guardarError 
                    
            #finaliza For
            cont_raiz = 0
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n " #nodo original de cada operacion
        
        #Inverso 1/x
        elif self.tipo.lower() == 'inverso':  
            tipo = "Inverso"
            for operando in self.operandos:
                cont_inverso += 1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Inverso"
                    if cont_inverso == 1:
                        #if operando = 0  - ERRor divison by cero
                        res += operando + ' @ '
                        resnum = 1/float(operando) #con flotante para evitar clavos

                        #grafica
                        self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                        self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"
                    elif cont_inverso == 2:
                        #Error - Solo se permite 1 valor 
                        print("Error logico, solo se permite 1 valor xd")
                    
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") @ "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    if cont_inverso == 1:
                        #if operado [1] == 0: Error division by cero
                        resnum = 1/operado[1]
                        #Grafica sub elementos 
                        operado[0] = re.sub("\+|\^|\√|\@|\#|\$|\%","",operado[0]) #quita el signo  
                        operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\*","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                        anidada = operado[0].split()    #se descompone 
                        for i in anidada:   #se itera 
                            self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                            self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                        self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3])+': '+ str(round(operado[1],2))}>]\n "  #crea subnodo del original
                        self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
                    else:
                        print("Error logico, solo se permite 1 valor rt")
                        #Pendiende guardarError 
            #Finaliza for        
            cont_inverso = 0
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n " #nodo original de cada operacion
        
        #Sena math.sin(x)
        elif self.tipo.lower() == 'seno':  
            tipo = "Seno"
            for operando in self.operandos:
                cont_seno += 1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Seno"
                    if cont_seno == 1:
                        res += operando + ' # '
                        resnum = math.sin(float(operando)) #con flotante para evitar clavos

                        #grafica
                        self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                        self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"
                    elif cont_seno == 2:
                        #Error - Solo se permite 1 valor 
                        print("Error logico, solo se permite 1 valor xd")
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") # "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    
                    if cont_seno == 1:
                        resnum = math.sin(operado[1]) 
                        #Grafica sub elementos 
                        operado[0] = re.sub("\+|\^|\√|\@|\#|\$|\%","",operado[0]) #quita el signo   
                        operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\*","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                        anidada = operado[0].split()    #se descompone 
                        for i in anidada:   #se itera 
                            self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                            self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                        self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3])+': '+ str(round(operado[1],2))}>]\n "  #crea subnodo del original
                        self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
                    else:
                        print("Error logico, solo se permite 1 valor rt")
                        #Pendiende guardarError 
            #finaliza For
            cont_seno = 0
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n " #nodo original de cada operacion
        
        #Coseno math.cos(x)
        elif self.tipo.lower() == 'coseno':  
            tipo = "Coseno"
            for operando in self.operandos:
                cont_coseno += 1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Coseno"
                    if cont_coseno == 1:
                        res += operando + ' $ '
                        resnum = math.cos(float(operando)) #con flotante para evitar clavos

                        #grafica
                        self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                        self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"
                    elif cont_coseno == 2:
                        #Error - Solo se permite 1 valor 
                        print("Error logico, solo se permite 1 valor xd")
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") $ "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    
                    if cont_coseno == 1:
                        resnum = math.cos(operado[1]) 
                        #Grafica sub elementos 
                        operado[0] = re.sub("\+|\^|\√|\@|\#|\$|\%","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\*","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                        anidada = operado[0].split()    #se descompone 
                        for i in anidada:   #se itera 
                            self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                            self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                        self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3])+': '+ str(round(operado[1],2))}>]\n "  #crea subnodo del original
                        self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
                    else:
                        print("Error logico, solo se permite 1 valor rt")
                        #Pendiende guardarError 
            #finaliza For
            cont_coseno = 0
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n " #nodo original de cada operacion
        
        #tan math.tan(x)
        elif self.tipo.lower() == 'tangente':  
            tipo = "Tangente"
            for operando in self.operandos:
                cont_tangente += 1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Tangente"
                    if cont_tangente == 1:
                        res += operando + ' % '
                        resnum = math.tan(float(operando)) #con flotante para evitar clavos

                        #grafica
                        self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                        self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"
                    elif cont_tangente == 2:
                        #Error - Solo se permite 1 valor 
                        print("Error logico, solo se permite 1 valor xd")
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") % "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    
                    if cont_tangente == 1:
                        resnum = math.tan(operado[1]) 
                        #Grafica sub elementos 
                        operado[0] = re.sub("\+|\^|\√|\@|\#|\$|\%","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\*","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                        operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                        anidada = operado[0].split()    #se descompone 
                        for i in anidada:   #se itera 
                            self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                            self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                        self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3])+': '+ str(round(operado[1],2))}>]\n "  #crea subnodo del original
                        self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
                    else:
                        print("Error logico, solo se permite 1 valor rt")
                        #Pendiende guardarError 
            #finaliza For
            cont_tangente = 0
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n " #nodo original de cada operacion
        
        #Modulo -> math.fmod(x,y)
        elif self.tipo.lower() == 'mod':  
            tipo = "Suma"
            for operando in self.operandos:
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Suma"
                    res += operando + ' + '
                    resnum += round(float(operando), 2) #con flotante para evitar clavos

                    #grafica
                    self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"

                    
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") + "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    resnum += operado[1]  #Se suma el resultado de la operacion anidada al total
                    
                    #Descomponer operacion anidada
                    operado[0] = re.sub("\+","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\*","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                    anidada = operado[0].split()    #se descompone 
                    for i in anidada:   #se itera 
                        self.aux += float(i)   #se crea el total interno 
                        self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                        self.texto += f"\t{str(operado[3])+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                    self.texto += f"\t{str(operado[3])+str(id+100)} [shape=circle style=filled color = blue, label=<{str(operado[3])+': '+ str(round(operado[1],2))}>]\n "  #crea subnodo del original
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado[3])+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
            #finaliza For
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{str(tipo)+': '+ str(round(resnum,2))}>]\n " #nodo original de cada operacion
        
        return [res[0:-3], resnum, self.texto, tipo, self.errores_tabla] # [0: -3] para eliminar caracteres inecesarios
        

    def operarErrores(self, id): 
        res = '' # 1 + (1 + 1) = 3      #describe la operacion string  
        resnum = 0          #resultado de la operacion
        cont_resta = 0
        cont_division = 0
        #SUMA
        tipo = ""
        if self.tipo.lower() == 'suma':  
            tipo = "Suma"
            for operando in self.operandos:
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Suma"
                    res += operando + ' + '
                    resnum += float(operando) #con flotante para evitar clavos

                    
                    
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") + "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    resnum += operado[1]  #Se suma el resultado de la operacion anidada al total
                    
                    #Descomponer operacion anidada
                    operado[0] = re.sub("\+","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\*","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                    anidada = operado[0].split()    #se descompone 
                    
        if self.tipo.lower() == 'resta':  
            tipo = "Resta"
            for operando in self.operandos:
                cont_resta +=1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "Resta"
                    res += operando + ' - '
                    if cont_resta == 1:
                        resnum += float(operando) #con flotante para evitar clavos
                    else:
                        resnum -= float(operando)
                    
                else:
                    
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") - "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    if cont_resta == 1:
                        resnum += operado[1]  #Se suma el resultado de la operacion anidada al total
                    else:
                        resnum -= operado[1]

                    #Descomponer operacion anidada
                    operado[0] = re.sub("\+","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\-","",operado[0]) #quita el signo
                    operado[0] = re.sub("\*","",operado[0]) #quita el signo  
                    operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\(|\)","",operado[0]) #quita el signo 
                    anidada = operado[0].split()    #se descompone 
            cont_resta = 0
            
        #MULTIPLICACION
        elif self.tipo.lower() == 'multiplicacion':
            resnum = 1
            tipo = "Multiplicacion"
            for operando in self.operandos:
                # print("los valores: "+str(operando))
                if type(operando) is not Operacion:
                    #Grafica
                    tipo = "Multiplicacion"
                    res += operando + ' * '
                    resnum = resnum * float(operando)

                    
                else:
                    operado = operando.operar(id) 
                    res += "(" + operado[0]+ ") * "
                    resnum = resnum * float(operado[1])
        
                    #Descomponer operacion anidada
                    operado[0] = re.sub("\+","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\*","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\/","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\(|\)|\'","",operado[0]) #quita el signo 
                    anidada = operado[0].split()    #se descompone 

        
        if self.tipo.lower() == 'division':  
            tipo = "division"
            for operando in self.operandos:
                cont_division += 1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    tipo = "division"
                    if cont_division == 2:
                        if operando == "0":
                            #Pendiendteeee...
                            print("Se produjo un error logico")
                            self.inidiceError +=1
                            self.guardar_error('/', "Error Logico", self.inidiceError)
                        else:
                            #En caso sea el segundo valor
                            res += operando + ' / '
                            resnum /= float(operando) #con flotante para evitar clavos
                    #En caso sea el primer valor
                    if cont_division == 1:
                        res += operando + ' / '
                        resnum += float(operando)
                    
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") / "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada

                    if cont_division == 2:
                        if operando == "0":
                            #Pendiendteeee...
                            print("Se produjo un error logico")
                            self.inidiceError +=1
                            self.guardar_error('/', "Error Logico", self.inidiceError)
                        else:
                            #En caso sea el segundo valor un numero != 0
                            resnum /= float(operado[1])
                    #En caso sea el primer valor
                    if cont_division == 1:
                        resnum += float(operado[1] )
                    #Descomponer operacion anidada
                    
            cont_division += 0
        
        return [res[0:-3], resnum, self.texto, tipo, self.errores_tabla] # [0: -3] para eliminar caracteres inecesarios
    
    def guardar_error(self, lexema, tipoError, id):
        nuevo_token = Error(0, 0, lexema, tipoError, id)
        self.errores_tabla.append(nuevo_token)
    
    def Reiniciando(self):
        self.errores_tabla = []
        self.inidiceError = 0