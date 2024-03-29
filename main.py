import sys
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
from AnalizadorSintactico import AnalizadorSintactico
from editor import Editor
from AnalizadorLexico import AnalizadorLexico

class VentanaEditor(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = Editor()
        self.ui.setupUi(self)
        self.ui.bCargar.clicked.connect(self.cargar)
        self.ui.bAnalizar.clicked.connect(self.analizar)
        self.ui.bReporte.clicked.connect(self.reporte)
        self.parser = ''
        self.scanner = ''
        self.tokens = []
        self.errores = []
        self.show()
    
    def reporte(self):
        self.parser.crearReporteErrores()
        self.parser.crearReporteTokens()
    
    def cargar(self):
        archivo = QFileDialog.getOpenFileName(self,"Abrir archivo",".","Texto (*.lfp)")
        archivo = open(archivo[0],'r')
        data = archivo.read()
        archivo.close()
        
        self.ui.Editor.setPlainText(data)
        
    def analizar(self):
        self.scanner = AnalizadorLexico()
        listaTokens = self.scanner.analizar(self.ui.Editor.toPlainText())
        
        self.scanner.impTokens()
        self.scanner.impErrores()
        self.parser = AnalizadorSintactico()
        
        self.parser.analizar(listaTokens)
        self.parser.impErrores()
        
        
        console = ''
        for i in self.parser.impresiones:
            console+=i
        
        self.ui.Consola.setPlainText(console)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = VentanaEditor()
    main.show()
    sys.exit(app.exec_())
    