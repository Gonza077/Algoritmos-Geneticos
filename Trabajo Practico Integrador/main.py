from Generacion import *
from Poblacion import *
from Cromosoma import *
from OperadoresGeneticos import *
import openpyxl as opyxl

from UserInterface import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
    
class App(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()





# CantPoblaciones=[200]   
# generaciones=[]
# #Parametros del Parque 
# Cromosoma.tCromo=10  #Sera una matriz de 10x10
# Cromosoma.CantAerogeneradores=25
# Cromosoma.VelocidadViento=25 #Velocidad del viento
# Cromosoma.TamañoCelda=180 #Distancia Minima de 4*R, donde R es 45 m
# #Parametros de la Poblacion
# Poblacion.tPobla=50 #Cantidad de cromosomas x Poblacion
# Poblacion.tipoSeleccion=Ruleta()
# Poblacion.tipoCrossover=CrossOverUnPunto(0.9)
# Poblacion.tipoMutacion=MutacionInvertida(0.05)
# Poblacion.elitismo=True

# for x in CantPoblaciones:
#     generacion=Generacion()
#     for _ in range(x):        
#         generacion.creoPoblacion()
#     Poblacion.reseteoIDPoblacion() #Metodo de clase que vuelve el ID a 1
#     generaciones.append(generacion)

# #Se crea una archivo XLSX y se elimina la primer pagina
# wb = opyxl.Workbook() 
# wb.remove(wb.active) 
# print("\n")
# for generacion in generaciones:
#     generacion.datosGeneracion(wb)
#     print("\n")

