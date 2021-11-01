from Token import Token
from Error import Error
from registro import Registro

class AnalizadorSintactico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.i = 0
        self.impresiones = []
        self.registros = []
        self.claves = []
        
    def analizar(self, listaTokens):
        self.i = 0
        self.listaTokens = listaTokens
        
        self.inicio()
        
        
        
    def inicio(self):
        
        self.lista_instrucciones()
   
    def funcError(self):
        linea = self.listaTokens[self.i].linea
        columna = self.listaTokens[self.i].columna
        self.listaErrores.append(Error(self.listaTokens[self.i].lexema,'Error Sintactico',linea,columna))
        self.i+=1
        
          
    def instruccion(self):
        
        if self.listaTokens[self.i].tipo == 'registros':
            self.ins_registros()
        elif self.listaTokens[self.i].tipo == 'claves':
            self.ins_claves()
        elif self.listaTokens[self.i].tipo == 'imprimir':
            self.ins_imprimir()
            
        elif self.listaTokens[self.i].tipo == 'imprimirln':
            self.ins_imprimirln()
        
        elif self.listaTokens[self.i].tipo == 'conteo':
            self.ins_conteo()   
        
        elif self.listaTokens[self.i].tipo == 'promedio':
            self.ins_promedio()
        elif self.listaTokens[self.i].tipo == 'contarsi':
            
            self.ins_contarsi()
        elif self.listaTokens[self.i].tipo == 'datos':
            self.ins_datos()
        elif self.listaTokens[self.i].tipo == 'sumar':
            self.ins_sumar()
        elif self.listaTokens[self.i].tipo == 'max':
            self.ins_max()
        elif self.listaTokens[self.i].tipo == 'min':
            self.ins_min()
    
    
    def ins_datos(self):
        if self.listaTokens[self.i].tipo == 'datos':
            self.i+=1
            
            if self.listaTokens[self.i].tipo == 'parA':
                self.i+=1
                
                if self.listaTokens[self.i].tipo == 'parC':
                    self.i+=1
                        
                    if self.listaTokens[self.i].tipo == 'puntoComa':
                        self.i+=1
                        cadenaClaves = ''
                        lenMax = 0
                        
                        cadenaRegistros = ''          
                                         
                        for i in self.registros:
                            for a in i.data:
                                agregado = f'{a.lexema}'
                                lenA = len(agregado)
                            
                                add =agregado.count('i')
                                add+=agregado.count('l')
                                add+=agregado.count('1')
                                add+=agregado.count('j')
                                
                                for b in range(add):
                                    lenA+=1
                                
                                if lenA > lenMax:
                                    lenMax = lenA
                        
                        
                        for i in self.claves:
                            agregado = f'{i.lexema}'
                            lenA = len(agregado)
                            if lenA > lenMax:
                                lenMax = lenA
                        
                        for i in self.registros:
                            for a in i.data:
                                agregado = f'{a.lexema}'
                                lenA = len(agregado)
                                espacios = lenMax - lenA
                                espacio = ''
                                for b in range(espacios):
                                    if b%2 == 0:
                                        espacio+=' '
                                cadenaRegistros +=espacio+ agregado+espacio
                            cadenaRegistros += '\n'
                        
                        for i in self.claves:
                            
                            agregado = f'{i.lexema}'
                            lenA = len(agregado)
                            espacios = lenMax - lenA
                            espacio = ''
                            for b in range(espacios):
                                if b%2 == 0:
                                    espacio += ' '
                            cadenaClaves +=espacio+ agregado+espacio
                        cadenaClaves += '\n'
                        self.impresiones += f'\n{cadenaClaves}'
                        self.impresiones += f'\n{cadenaRegistros}'
                        
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
        else:
            self.funcError()
        
        self.impresiones.append(f'\nLa cantidad de registros es: {len(self.registros)}')  

    def ins_contarsi(self):
        
        if self.listaTokens[self.i].tipo == 'contarsi':
            self.i+=1
            if self.listaTokens[self.i].tipo == 'parA':
                self.i+=1
                if self.listaTokens[self.i].tipo == 'cadena':
                    token = self.listaTokens[self.i]
                    self.i+=1
                    if self.listaTokens[self.i].tipo == 'coma':
                        self.i+=1
                        if self.listaTokens[self.i].tipo == 'cadena' or self.listaTokens[self.i].tipo == 'entero' or self.listaTokens[self.i].tipo == 'decimal':
                            token2 = self.listaTokens[self.i]
                            self.i+=1
                            if self.listaTokens[self.i].tipo == 'parC':
                                self.i+=1
                                if self.listaTokens[self.i].tipo == 'puntoComa':
                                    self.i+=1
                                    index = 0
                                    for a in self.claves:
                                        if a.lexema  == token.lexema:
                                            index = self.claves.index(a)
                                            break
                                    cadena = ''
                                    contador = 0
                                    
                                    for a in self.registros:
                                        tokenComp = a.data[index].lexema
                                        
                                        if tokenComp == token2.lexema:
                                            contador+=1

                                        
                                    cadena += f'Existen {contador} registros de {token.lexema} con valor {token2.lexema}'
                                        
                                    
                                    self.impresiones += f'\n{cadena}'
                                    
                                else:
                                    self.funcError()
                            else:
                                self.funcError()
                        else:
                            self.funcError()
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
        else:
            self.funcError()
    def ins_promedio(self):
        
        if self.listaTokens[self.i].tipo == 'promedio':
            self.i+=1
            if self.listaTokens[self.i].tipo == 'parA':
                self.i+=1
                if self.listaTokens[self.i].tipo == 'cadena':
                    token = self.listaTokens[self.i]
                    
                    self.i+=1
                    if self.listaTokens[self.i].tipo == 'parC':
                        self.i+=1
                        if self.listaTokens[self.i].tipo == 'puntoComa':
                            self.i+=1
                            index = 0
                            for a in self.claves:
                                if a.lexema  == token.lexema:
                                    index = self.claves.index(a)
                                    break
                            promedio = 0
                            for a in self.registros:
                                promedio +=int(a.data[index].lexema)
                            promedio = promedio/len(self.registros)
                            self.impresiones += (f'\nPromedio en el campo {token.lexema} es:\n{promedio}')
                            
                        else:
                            self.funcError()
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
        else:
            self.funcError()
            
    def ins_max(self):
        
        if self.listaTokens[self.i].tipo == 'max':
            self.i+=1
            if self.listaTokens[self.i].tipo == 'parA':
                self.i+=1
                if self.listaTokens[self.i].tipo == 'cadena':
                    token = self.listaTokens[self.i]
                    
                    self.i+=1
                    if self.listaTokens[self.i].tipo == 'parC':
                        self.i+=1
                        if self.listaTokens[self.i].tipo == 'puntoComa':
                            self.i+=1
                            index = 0
                            for a in self.claves:
                                if a.lexema  == token.lexema:
                                    index = self.claves.index(a)
                                    break
                            max = 0
                            for a in self.registros:
                                current = float(a.data[index].lexema)
                                if current > max:
                                    max = current

                            
                            self.impresiones += (f'\nEl maximo en el campo {token.lexema} es:\n{max}')
                            
                        else:
                            self.funcError()
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
        else:
            self.funcError()
    
    def ins_min(self):
        
        if self.listaTokens[self.i].tipo == 'min':
            self.i+=1
            if self.listaTokens[self.i].tipo == 'parA':
                self.i+=1
                if self.listaTokens[self.i].tipo == 'cadena':
                    token = self.listaTokens[self.i]
                    
                    self.i+=1
                    if self.listaTokens[self.i].tipo == 'parC':
                        self.i+=1
                        if self.listaTokens[self.i].tipo == 'puntoComa':
                            self.i+=1
                            index = 0
                            for a in self.claves:
                                if a.lexema  == token.lexema:
                                    index = self.claves.index(a)
                                    break
                            
                            listaComparacion = []
                            for a in self.registros:
                                current = float(a.data[index].lexema)
                                listaComparacion.append(current)
                            
                            menor = min(listaComparacion)
                                    
                                
                                

                            
                            self.impresiones += (f'\nEl minimo en el campo {token.lexema} es:\n{menor}')
                            
                        else:
                            self.funcError()
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
        else:
            self.funcError()
                    
    def ins_sumar(self):
        
        if self.listaTokens[self.i].tipo == 'sumar':
            self.i+=1
            if self.listaTokens[self.i].tipo == 'parA':
                self.i+=1
                if self.listaTokens[self.i].tipo == 'cadena':
                    token = self.listaTokens[self.i]
                    
                    self.i+=1
                    if self.listaTokens[self.i].tipo == 'parC':
                        self.i+=1
                        if self.listaTokens[self.i].tipo == 'puntoComa':
                            self.i+=1
                            index = 0
                            for a in self.claves:
                                if a.lexema  == token.lexema:
                                    index = self.claves.index(a)
                                    break
                            suma = 0
                            for a in self.registros:
                                suma +=int(a.data[index].lexema)
                            
                            self.impresiones += (f'\nLa suma de los registros\nen el campo {token.lexema} es: {suma}')
                            
                        else:
                            self.funcError()
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
        else:
            self.funcError()
                            
    def ins_conteo(self):
        if self.listaTokens[self.i].tipo == 'conteo':
            self.i+=1
            
            if self.listaTokens[self.i].tipo == 'parA':
                self.i+=1
            
                if self.listaTokens[self.i].tipo == 'parC':
                    self.i+=1
                    
                    if self.listaTokens[self.i].tipo == 'puntoComa':
                        self.i+=1
                        registros = []
                        indexA = 0
                        indexB = 0
                        for a in self.listaTokens:
                        
                            if a.tipo == 'registros':
                                indexA = self.listaTokens.index(a)
                                break
     
                        for b in self.listaTokens[indexA:]:
                        
                            if b.tipo == 'corC':
                                indexB = self.listaTokens.index(b)+1
                                break
                        
                        for c in self.listaTokens[indexA+3:indexB-1]:
                            
                            registros.append(c)
             
                        listIndex = []
                        for a in registros:
                            if a.lexema == '{':
                                listIndex.append(registros.index(a))
                            elif a.lexema == '}':
                                listIndex.append(registros.index(a))
                        
                        
                        registro = Registro()
                        i = 0
                        while i<len(listIndex):
                            
                            indexA = listIndex[i]
                            indexB = listIndex[i+1]
                            i+=2
                            for c in registros[indexA+1:indexB]:
                                if c.lexema != ',':
                                    registro.data.append(c)
                                
                            self.registros.append(registro)
                            registro = Registro()
                        
                                
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
        else:
            self.funcError()
        
        self.impresiones.append(f'\nLa cantidad de registros es: {len(self.registros)}')
    
    def ins_imprimir(self):
        
        if self.listaTokens[self.i].tipo == 'imprimir':
            self.i+=1
            if self.listaTokens[self.i].tipo == 'parA':
                self.i+=1
                if self.listaTokens[self.i].tipo == 'cadena':
                    cadena = self.listaTokens[self.i].lexema
                    
                   
                    self.i+=1
                    if self.listaTokens[self.i].tipo == 'parC':
                        self.i+=1
                        
                        if self.listaTokens[self.i].tipo == 'puntoComa':
                            self.i+=1
                            
                            self.impresiones.append(cadena)
                        else:
                            self.funcError()
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
        
    def ins_imprimirln(self):
        if self.listaTokens[self.i].tipo == 'imprimirln':
            self.i+=1
            if self.listaTokens[self.i].tipo == 'parA':
                self.i+=1
                if self.listaTokens[self.i].tipo == 'cadena':
                    cadena = '\n'+self.listaTokens[self.i].lexema
                    self.i+=1
                    if self.listaTokens[self.i].tipo == 'parC':
                        self.i+=1
                        if self.listaTokens[self.i].tipo == 'puntoComa':
                            self.i+=1
                            
                            self.impresiones.append(cadena)
                        else:
                            self.funcError()
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
        
    def ins_claves(self):
        if self.listaTokens[self.i].tipo == 'claves':
            self.i+=1
            if self.listaTokens[self.i].tipo == 'igual':
                self.i+=1
                if self.listaTokens[self.i].tipo == 'corA':
                    self.i+=1
                    self.lista_claves()
                    if self.listaTokens[self.i].tipo == 'corC':
                        self.i+=1
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
    
    def lista_claves(self):
        self.clave()
        self.lista_claves2()
    
    def clave(self):
        if self.listaTokens[self.i].tipo == 'cadena':
            self.claves.append(self.listaTokens[self.i])
            self.i+=1
            self.lista_claves2()
        else:
            self.funcError()
    def lista_claves2(self):
        if self.listaTokens[self.i].tipo == 'corC':
            pass
            
        else:
            self.clave()
            self.lista_claves2()
        
    def lista_instrucciones2(self):
        
        if self.listaTokens[self.i].tipo == 'registros':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'claves':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'imprimir':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'imprimirln':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'comentarioLn' or self.listaTokens[self.i].tipo == 'comentarioMl':
            self.i+=1    
            self.lista_instrucciones2()
            
        elif self.listaTokens[self.i].tipo == 'conteo':
            self.instruccion()
            self.lista_instrucciones2()
        
        elif self.listaTokens[self.i].tipo == 'promedio':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'contarsi':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'datos':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'sumar':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'max':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'min':
            self.instruccion()
            self.lista_instrucciones2()
        
        elif self.listaTokens[self.i].tipo == 'EOF':
            print('analisis sintactico terminado')
        else:
            self.funcError()
            
    def lista_instrucciones(self):
        if self.listaTokens[self.i].tipo == 'registros':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'claves':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'imprimir':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'imprimirln':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'comentarioLn' or self.listaTokens[self.i].tipo == 'comentarioMl':
            self.i+=1    
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'conteo':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'promedio':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'contarsi':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'datos':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'sumar':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'max':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'min':
            self.instruccion()
            self.lista_instrucciones2()
        
        else:
            self.funcError()
            
    def ins_registros(self):
        if self.listaTokens[self.i].tipo == 'registros':
            self.i+=1
            if self.listaTokens[self.i].tipo == 'igual':
                self.i+=1
                if self.listaTokens[self.i].tipo == 'corA':
                    self.i+=1
                    self.lista_registros()
                    if self.listaTokens[self.i].tipo == 'corC':
                        self.i+=1
                    else:
                        self.funcError()
                else:
                    self.funcError()
            else:
                self.funcError()
              
    def lista_registros(self):
        self.registro()
        self.lista_registros2()
        
    def registro(self):
        if self.listaTokens[self.i].tipo == 'llaveA':
            self.i +=1
            self.lista_val_reg()
            if self.listaTokens[self.i].tipo == 'llaveC':
                self.i +=1
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(Error(self.listaTokens[self.i].lexema,'Error Sintactico',linea,columna))
        else:
            self.funcError()
    
    def lista_registros2(self):
        if self.listaTokens[self.i].tipo == 'corC':
            pass
        else:
            self.registro()
            self.lista_registros2()
    
    def lista_val_reg(self):
        self.val_reg()
        self.lista_val_reg2()
        
    def val_reg(self):
        if self.listaTokens[self.i].tipo == 'cadena':
            self.i+=1
            
        elif self.listaTokens[self.i].tipo == 'entero':
            self.i+=1
        elif self.listaTokens[self.i].tipo == 'decimal':
            self.i+=1
        else:
            self.funcError()
        
    def lista_val_reg2(self):
        if self.listaTokens[self.i].tipo == 'llaveC':
            pass
        elif self.listaTokens[self.i].tipo == 'coma':
            self.i+=1
            self.val_reg()
            self.lista_val_reg2()
            
    def impErrores(self):
        if len(self.listaErrores) == 0:
            print('No hay errores sintacticos')
        else:
            for i in self.listaErrores:
                
                i.impError()