import re
class Operacion:
    def __init__(self, tipo) :
        self.tipo = tipo 
        self.operandos = []  #lista los valores de la operacion
        self.texto = ''
        self.aux = 0


    def operar(self, id): 
        res = '' # 1 + (1 + 1) = 3      #describe la operacion string  
        resnum = 0          #resultado de la operacion
        cont_resta = 0
        #SUMA
        if self.tipo.lower() == 'suma':  
            for operando in self.operandos:
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    res += operando + ' + '
                    resnum += float(operando) #con flotante para evitar clavos

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
                    anidada = operado[0].split()    #se descompone 
                    for i in anidada:   #se itera 
                        self.aux += int(i)   #se crea el total interno 
                        self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                        self.texto += f"\t{str(self.tipo.lower())+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                    self.texto += f"\t{str(self.tipo.lower())+str(id+100)} [shape=circle style=filled color = blue, label=<{'suma: '+ str(self.aux)}>]\n "  #crea subnodo del original
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(self.tipo.lower())+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
            #finaliza For
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{'suma: '+ str(resnum)}>]\n " #nodo original de cada operacion
        #RESTA
        if self.tipo.lower() == 'resta':  
            for operando in self.operandos:
                cont_resta +=1
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    res += operando + ' - '
                    if cont_resta == 1:
                        resnum += float(operando) #con flotante para evitar clavos
                    else:
                        resnum -= float(operando)

                    #grafica
                    self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores - [cadena, resultado]
                    #en caso venga anidada sera aux para obtener nodos internos
                    res += "(" + operado[0] + ") - "# y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    resnum -= operado[1]  #Se suma el resultado de la operacion anidada al total

                    cont_sub_resta = 0
                    
                    #Descomponer operacion anidada
                    operado[0] = re.sub("\+","",operado[0]) #quita el signo 
                    operado[0] = re.sub("\-","",operado[0]) #quita el signo 
                    anidada = operado[0].split()    #se descompone 
                    for i in anidada:   #se itera 
                        if cont_sub_resta == 1:
                            self.aux += int(i)   #se crea el total interno 
                        else:
                            self.aux -= int(i)
                        self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n " #nodo operacion anidada
                        self.texto += f"\t{str(self.tipo.lower())+str(id+100)} -> {str(i)} [shape=record color=red]\n"  #coneccion con subnodo del original 
                    self.texto += f"\t{str(self.tipo.lower())+str(id+100)} [shape=circle style=filled color = blue, label=<{'Resta: ' + str(self.aux)}>]\n "  #crea subnodo del original
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(self.tipo.lower())+str(id+100)} [shape=record color=red]\n"  #se conectan con el original
            #finaliza For
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{'Resta: '+ str(resnum)}>]\n " 

        #MULTIPLICACION
        elif self.tipo.lower() == 'multiplicacion':
            resnum = 1
            for operando in self.operandos:
                # print("los valores: "+str(operando))
                if type(operando) is not Operacion:
                    #Grafica
                    self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"

                    res += operando + ' * '
                    resnum = resnum * float(operando)
                else:
                    res += "(" + operando.operar(id) + ") * "
                    resnum = resnum * float(operado[1])
                    #grafica
                    self.texto += f"\t{str(operado)} [shape=circle style=filled color = blue]\n "
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operado)} [shape=record color=red]\n"
            #termina for
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{'Multiplica: '+ str(resnum)}>]\n "
        
        return [res[0:-3], resnum, self.texto] # [0: -3] para eliminar caracteres inecesarios