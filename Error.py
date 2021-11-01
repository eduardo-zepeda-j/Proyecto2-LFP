class Error:
    def __init__(self,descripcion,tipo,linea,columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        
    def impError(self):
        return ("Descripcion: "+self.descripcion+" Tipo: "+self.tipo+" Linea: "+str(self.linea)+" Columna: "+str(self.columna))