import re
class Operacion:
    def __init__(self, tipo) :
        self.tipo = tipo 
        self.operandos = []  #lista los valores de la operacion
        self.texto = ''


    def operar(self, id):  ##Comno se pueden sumar objetos se creo esta funcion
        res = '' # 1 + (1 + 1) = 3      #describe la operacion string  
        resnum = 0          #Es la operacion ya realizada, resultado
        if self.tipo.lower() == 'suma':  #Se valida el tipo con una palabra
            
            for operando in self.operandos:
                # print("los valores: "+str(operando))  trae valores y algo raro
                if type(operando) is not Operacion:  #significa que es algo simple como un NUMERO 
                    #resultado numerico 
                    res += operando + ' + '
                    resnum += float(operando) #con flotante para evitar clavos

                    #grafica
                    self.texto += f"\t{str(operando)} [shape=circle style=filled color = blue]\n "
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(operando)} [shape=record color=red]\n"
                else:
                    operado = operando.operar(id)     #Recursividad en caso la operacion venga anidada con el else llamamos de nuevo para traer los numeros
                    # regresa con valores
                    aux = 0
                    res += "(" + operado[0] + ") + "#y asignarlos en el tipo de operacion.  Par identificar que era operacion concatenada
                    resnum += operado[1]
                    
                    operado[0] = re.sub("\+","",operado[0])
                    anidada = operado[0].split()
                    for i in anidada:
                        aux += int(i)
                        self.texto += f"\t{str(i)} [shape=circle style=filled color = blue]\n "
                        self.texto += f"\t{str(self.tipo.lower())+str(id+100)} -> {str(i)} [shape=record color=red]\n"  
                    self.texto += f"\t{str(self.tipo.lower())+str(id+100)} [shape=circle style=filled color = blue, label=<{'suma: '+ str(aux)}>]\n "
                    self.texto += f"\t{str(self.tipo.lower())+str(id)} -> {str(self.tipo.lower())+str(id+100)} [shape=record color=red]\n"
            #finaliza For
            self.texto += f"\t{str(self.tipo.lower())+str(id)} [shape=circle style=filled color = blue, label=<{'suma: '+ str(resnum)}>]\n "
        
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