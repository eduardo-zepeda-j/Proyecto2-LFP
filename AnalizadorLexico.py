from Token import Token 
from Error import Error
import re



class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        
    def impTokens(self):
        cadena = ''
        for i in self.listaTokens:
            cadena+=i.impToken()
            cadena+='\n'
        
        archivo = open('Tokens.txt','w')
        archivo.write(cadena)
        archivo.close()
        
    
    def impErrores(self):
        if len(self.listaErrores)>0:
            print(self.listaErrores)
        else:
            print('No hay errores Lexicos')
        return self.listaErrores
    
    def analizar(self,codigo_fuente):
        self.listaTokens = []
        self.listaErrores=[]
        
        linea = 1
        columna = 1
        buffer = ''
        centinela = '$'
        estado = 0
        codigo_fuente += centinela
        
        i=0
        while i<len(codigo_fuente):
            c = codigo_fuente[i]
            
            
            if estado == 0:
                
                
                if c == '(':
                    buffer += c
                    
                    self.listaTokens.append(Token('(','parA',linea,columna))
                    buffer = ''
                    columna+=1
                
                elif c == ')':
                    buffer += c
                    self.listaTokens.append(Token(')','parC',linea,columna))
                    buffer = ''
                    columna+=1
                elif c == '{':
                    buffer += c
                    self.listaTokens.append(Token('{','llaveA',linea,columna))
                    buffer = ''
                    columna+=1
                
                elif c== '}':
                    buffer += c
                    self.listaTokens.append(Token('}','llaveC',linea,columna))
                    buffer = ''
                    columna+=1
                
                elif c == '[':
                    buffer += c
                    self.listaTokens.append(Token('[','corA',linea,columna))
                    buffer = ''
                    columna+=1
                
                elif c == ']':
                    buffer += c
                    self.listaTokens.append(Token(']','corC',linea,columna))
                    buffer = ''
                    columna+=1
                
                elif c == ';':
                    buffer += c
                    self.listaTokens.append(Token(';','puntoComa',linea,columna))
                    buffer = ''
                    columna+=1
                    
                elif c == ',':
                    buffer += c
                    self.listaTokens.append(Token(',','coma',linea,columna))
                    buffer = ''
                    columna+=1
                    
              
                elif c == '#':
                    
                    buffer += c
                    columna+=1
                    estado = 5
                elif c == "'":
                    buffer += c
                    columna+=1
                    
                    
                    if buffer == "'''":
                        
                        estado = 6
                    
                elif c == '=':
                    buffer += c
                    self.listaTokens.append(Token('=','igual',linea,columna))
                    buffer = ''
                    columna+=1
                    
                elif c == '\n':
                    linea+=1
                    columna=1
                    buffer = ''
                elif c == '\t':
                    columna+=1
                    buffer = ''
                elif c == '\r':
                    pass
                elif c == ' ':
                    columna+=1
                elif re.search('\d',c):
                    buffer+=c
                    columna+=1
                    estado = 1
                
                elif c == '"':
                    buffer += c
                    columna+=1
                    estado = 3
                
                elif re.search('[a-zA-Z]',c):
                    buffer += c
                    columna+=1
                    estado = 4
                
                elif c == '$':
                    self.listaTokens.append(Token(c,'EOF',linea,columna))
                    print('Se acepto la cadena!')
                    break
                
                else:
                    buffer += c
                    print(f'el buffer es -{buffer}-')
                    self.listaErrores.append(Error(f'Caracter {buffer} no valido','Caracter no valido',linea,columna))                    
                    buffer = ''
                    columna+=1
            elif estado ==1:
                if re.search('\d',c):
                    buffer += c
                    columna+=1
                elif c == '.':
                    buffer += c
                    columna+=1
                    estado = 2
                else:
                    
                    self.listaTokens.append(Token(buffer,'entero',linea,columna))
                    buffer = ''
                    i-=1
                    estado = 0
                    
            elif estado == 2:
                if re.search('\d',c):
                    buffer += c
                    columna+=1
                else:
                    self.listaTokens.append(Token(buffer,'decimal',linea,columna))
                    buffer = ''
                    i-=1
                    estado = 0
                    
            elif estado ==3:
                if c == '"':
                    buffer += c
                    self.listaTokens.append(Token(buffer.replace('"',''),'cadena',linea,columna))
                    buffer = ''
                    columna+=1
                    estado = 0
                
                elif c == '\n':
                    buffer += c
                    linea+=1
                    columna=1
                
                elif c == '\t':
                    columna+=1
                
                elif c == '\r':
                    buffer += c
                
                else:
                    buffer += c
                    columna+=1
            
            elif estado ==4:           
                if re.search('[a-zA-Z]',c):
                    buffer += c
                    columna+=1
                else:
                    
                    if buffer == 'Claves':
                        self.listaTokens.append(Token(buffer,'claves',linea,columna))
                    elif buffer == 'Registros':
                        self.listaTokens.append(Token(buffer,'registros',linea,columna))
                    elif buffer == 'imprimirln':
                        self.listaTokens.append(Token(buffer,'imprimirln',linea,columna))
                    elif buffer == 'imprimir':
                        self.listaTokens.append(Token(buffer,'imprimir',linea,columna))
                    elif buffer == 'conteo':
                        self.listaTokens.append(Token(buffer,'conteo',linea,columna))
                    elif buffer == 'promedio':
                        self.listaTokens.append(Token(buffer,'promedio',linea,columna))
                    elif buffer == 'contarsi':
                        self.listaTokens.append(Token(buffer,'contarsi',linea,columna))
                    elif buffer == 'datos':
                        self.listaTokens.append(Token(buffer,'datos',linea,columna))
                    elif buffer == 'sumar':
                        self.listaTokens.append(Token(buffer,'sumar',linea,columna))
                    elif buffer == 'max':
                        self.listaTokens.append(Token(buffer,'max',linea,columna))
                    elif buffer == 'min':
                        self.listaTokens.append(Token(buffer,'min',linea,columna))
                    elif buffer == 'exportarReporte':
                        self.listaTokens.append(Token(buffer,'exportarReporte',linea,columna))
                    
                    
                    buffer = ''
                    i-=1
                    estado = 0
            
            elif estado == 5:
                if c == '\n' or c == '$':
                    
                    self.listaTokens.append(Token(buffer,'comentarioLn',linea,columna))
                    buffer = ''
                    linea += 1
                    estado = 0
                else:
                    
                    buffer += c
                    columna+=1
                    
            elif estado == 6:
                if c == "'":
                    buffer += c
                    columna+=1
                    if buffer.endswith("'''") and buffer.startswith("'''"):
                        
                        self.listaTokens.append(Token(buffer,'comentarioMl',linea,columna))
                        buffer = ''
                        estado = 0
                elif c == '\n':
                    buffer+=c   
                    linea+=1
                    columna=1
                elif c == '\t':
                    buffer+=c
                    columna+=1
                elif c == ' ':
                    buffer+=c
                    columna+=1
                else:
                    buffer += c
                    columna+=1
                    
                    
                
                
            i+=1
        return self.listaTokens
                