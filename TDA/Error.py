class Error:
    def __init__(self, fila, columna, lexema, tipoError, id):
        self.fila = fila  #Fila del caracter 
        self.columna = columna  #Columna del caracter
        self.lexema = lexema    #El caracter xd
        self.tipoError = tipoError
        self.id = id 