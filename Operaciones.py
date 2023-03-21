class Operacion:
    def __init__(self, tipo) :
        self.tipo = tipo 
        self.operandos = []  #lista los valores de la operacion

    def operar(self):  ##Comno se pueden sumar objetos se creo esta funcion
        res = '' # 1 + (1 + 1) = 3      #describe la operacion 
        resnum = 0          #Es la operacion ya realizada, resultado
        if self.tipo.lower() == 'suma':  #Se valida el tipo con una palabra
            for operando in self.operandos:
                if type(operando) is not Operacion:  #significa que es algo simple como un numero
                    res += operando + ' + '
                    resnum += float(operando) #con flotante para evitar clavos
                else:
                    operado = operando.operar()     #Recursividad??
                    res += "(" + operado[0] + ") + "  #Par identificar que era operacion concatenada
                    resnum += operado[1]

        elif self.tipo.lower() == 'multiplicacion':
            resnum = 1
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' * '
                    resnum = resnum * float(operando)
                else:
                    res += "(" + operando.operar() + ") * "
                    resnum = resnum * float(operado[1])
        
        return [res[0:-3], resnum] # [0: -3] para eliminar caracteres inecesarios