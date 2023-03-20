from Tonken import Tonken

class Automata:
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u","v","w","x","y","z", "-"]
    numeros = ["1","2","3","4","5","6","7","8","9","0","."]
    tabla_tokens = []
    cadena = ''
    fila = 0
    columna = 0
    estado_actual = 0
    estado_anterior = 0
    estados_aceptacion = [26] #El unico estado de aceptacion 

#hacer prueba que pasa si intento hacer minuscula un numero tomado como caracter 
#Ver que el estado de aceptacion este bien en el codigo y en

    def analizar(self, cadena): #Analiza todo nuestro archivo - cadena tendra todo el archivo
        operacion = False
        operaciones = []
        token = ''

        while len(cadena) > 0:
            char = cadena[0]
            #Para saltos de lineas y espacion en blanco 
            if char == '\n':
                self.fila += 1
                self.columna = 0
                cadena = cadena[1:] #abaab -> #baab
                continue
            elif char == '\t':
                self.columna += 4
                cadena = cadena[1:]
                continue
            elif char == ' ':
                self.columna += 1
                cadena = cadena[1:] #abaab -> #baab
                continue

            #Inicia el Automata 
            if self.estado_actual == 0:
                if char == '{':
                    self.guardar_token(char)
                    self.estado_anterior = 0
                    self.estado_actual = 1

            elif self.estado_actual == 1:     # q1
                if char == '{':
                    self.guardar_token(char)
                    self.estado_anterior = 1
                    self.estado_actual = 2
                elif char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 1
                    self.estado_actual = 19

            elif self.estado_actual == 2:     #q2
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 2
                    self.estado_actual = 3

            elif self.estado_actual == 3:     #q3
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 3
                    self.estado_actual = 4

            elif self.estado_actual == 4:     #q4
                if char.lower() in self.letras:
                    token += char 
                    self.estado_anterior = 4
                    self.estado_actual = 4
                elif char == '"':
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 4
                    self.estado_actual = 5

            elif self.estado_actual == 5:    #q5
                if char == ':':
                    self.guardar_token(char)
                    self.estado_anterior = 5
                    self.estado_actual = 6

            elif self.estado_actual == 6:    #q6
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 6
                    self.estado_actual = 7

            elif self.estado_actual == 7:    #q7
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 7
                    self.estado_actual = 8

            elif self.estado_actual == 8:    #q8
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 8
                    self.estado_actual = 8
                elif char == '"': 
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 8
                    self.estado_actual = 9

            elif self.estado_actual == 9:    #q9
                if char == ',':
                    self.guardar_token(char)
                    self.estado_anterior = 9
                    self.estado_actual = 10

            elif self.estado_actual == 10:   #q10
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 10
                    self.estado_actual = 11
                elif char == '}': #bucle a q18 
                    self.guardar_token(char)
                    self.estado_anterior = 10
                    self.estado_actual = 18

            elif self.estado_actual == 11:   #q11
                if char.lower() in self.letras:
                    token += char 
                    self.estado_anterior = 11
                    self.estado_actual = 12

            elif self.estado_actual == 12:   #q12
                if char.lower() in self.letras or char.lower() in self.numeros:
                    token += char
                    self.estado_anterior = 12
                    self.estado_actual = 12
                elif char == '"':
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 12
                    self.estado_actual = 13

            elif self.estado_actual == 13:   #q13
                if char == ':':
                    self.guardar_token(char)
                    self.estado_anterior = 13
                    self.estado_actual = 14

            elif self.estado_actual == 14:   #q14
                if char in self.numeros: 
                    token += char
                    self.estado_anterior = 14
                    self.estado_actual = 15
                elif char == '[': #Bucle a q2
                    # token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 14
                    self.estado_actual = 2

            elif self.estado_actual == 15:   #q15 
                if char in self.numeros: #Lazo 
                    token += char 
                    self.estado_anterior = 15
                    self.estado_actual = 15
                elif char == '}': #avanza 
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 15
                    self.estado_actual = 18
                elif char == ',' or char == ']': #bucle a q10
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 15
                    self.estado_actual = 10

            elif self.estado_actual == 18:   #q18 
                if char == ',':     #bucle a q1
                    self.guardar_token(char)
                    self.estado_anterior = 18
                    self.estado_actual = 1
                elif char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 18
                    self.estado_actual = 19

            elif self.estado_actual == 19:   #q19 
                if char.lower() in self.letras: 
                    token += char
                    self.estado_anterior = 19
                    self.estado_actual = 20

            elif self.estado_actual == 20:    #q20 
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 20
                    self.estado_actual = 20
                elif char == '"': 
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 20
                    self.estado_actual = 21

            elif self.estado_actual == 21:   #q21
                if char == ':':
                    self.guardar_token(char)
                    self.estado_anterior = 21
                    self.estado_actual = 22

            elif self.estado_actual == 22:   #q22
                if char == '"':
                    self.guardar_token(char)
                    self.estado_anterior = 22
                    self.estado_actual = 23

            elif self.estado_actual == 23:   #q23
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 23
                    self.estado_actual = 24

            elif self.estado_actual == 24:   #q24
                if char.lower() in self.letras:
                    token += char
                    self.estado_anterior = 24
                    self.estado_actual = 24
                elif char == '"':
                    self.guardar_token(token)
                    token = ''
                    self.guardar_token(char)
                    self.estado_anterior = 24
                    self.estado_actual = 25

            elif self.estado_actual == 25:   #q25
                if char == '}':
                    self.guardar_token(char)
                    self.estado_anterior = 25
                    self.estado_actual = 26
                elif char == ',':
                    self.guardar_token(char)
                    self.estado_anterior = 25
                    self.estado_actual = 1
# ### SE CAMBIO EL ORDEN DE LOS ESTADOS DE TRANSICION 
#
            #Para finalizar ciclo 
            self.columna += 1  #aumenta columna 
            cadena = cadena[1:] #Elimina el caracter estudiado
        
        return self.estado_actual in self.estados_aceptacion #Retorna True or False
    

    def guardar_token(self, lexema):
        nuevo_token = Tonken(self.fila, self.columna, lexema)
        self.tabla_tokens.append(nuevo_token)
    
    def imprimir_tokens(self):
        print('-'*31)
        print ("| {:<4} | {:<7} | {:<10} |".format('Fila','Columna','Lexema'))
        print('-'*31)
        for token in self.tabla_tokens:
            print ("| {:<4} | {:<7} | {:<10} |".format(token.fila, token.columna, token.lexema))

autom = Automata()
cadena = open('prueba.txt', 'r').read()
print(cadena)
resultado = autom.analizar(cadena)

autom.imprimir_tokens()