from UserInterface import uiPyQT
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from Ciudad import *
from CiudadDAO import *
import pandas as pd
import numpy as np
from AlgoritmoGenetico.Cromosoma import *
from AlgoritmoGenetico.Poblacion import *
from AlgoritmoGenetico.OperadoresGeneticos import *
from AlgoritmoGenetico.Generacion import *

def condicionFiltro(x):
    return type(x.getDistancia()) == float

# Se podría meter todo esto en una función
def menuConsola():
    print(f"--------------------------------------------------------")
    print(f"Que desea hacer:")
    print(f"1- Buscar ruta mínima desde una ciudad:")
    print(f"2- Buscar ruta mínima total usando una Heuristica")
    print(f"3- Buscar ruta mínima total usando un Algoritmo Genético")
    print(f"--------------------------------------------------------")

    opc1 = int(input('Ingrese su opción: '))


    if opc1 == 1:
        print(f"Ingrese su ciudad de origen:")
        ciudad_origen = input()
        ruta = CiudadesDAO.buscarRuta(ciudad_origen)
        print(f"La ruta encontrada es:")
        print(f'{list(map(lambda x:x.getNombre(), ruta))}')
        # for c in ruta:
        #     print(f"Ciudad: {c.getNombre()} - Distancia {c.getDistancia()}")
        ciudades_filtradas = list(filter(condicionFiltro, ruta))
        # print(f"Lista de ciudades filtradas: {ciudades_filtradas}")
        arreglo_distancias = list(map(lambda x:x.getDistancia(), ciudades_filtradas))
        # print(f"Lista de ciudades mapeadas: {arreglo_distancias}")
        print(f"Total de ciudades: {len(arreglo_distancias)}")
        print(f"La distancia total es: {np.sum(arreglo_distancias)}")

    if opc1 == 2:
        ruta = CiudadesDAO.buscarRutaMinima()
        print("La ruta minima encontrada es:")
        print(f'{list(map(lambda x:x.getNombre(), ruta))}')
        ciudades_filtradas = list(filter(condicionFiltro, ruta))
        # print(f"Lista de ciudades filtradas: {ciudades_filtradas}")
        arreglo_distancias = list(map(lambda x:x.getDistancia(), ciudades_filtradas))
        # print(f"Lista de ciudades mapeadas: {arreglo_distancias}")
        print(f"Total de ciudades: {len(arreglo_distancias)}")
        print(f"La distancia total es: {np.sum(arreglo_distancias)}")

    if opc1 == 3:
        Corridas = 200
        Cromosoma.tCromo = 24
        Poblacion.tPobla = 50
        Poblacion.tipoSeleccion = Ruleta()
        Poblacion.tipoCrossover = CrossOverCiclico(0.75)
        Poblacion.tipoMutacion = MutacionAdjointSwap(0.05)
        Poblacion.elitismo = False
        generacion = Generacion()
        for _ in range(0, Corridas):
            generacion.creoGeneracion()

class ExampleApp(QtWidgets.QMainWindow, uiPyQT.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    #CARGA DE LOS DATOS DEL EXCEL
    CiudadesDAO.cargarCiudades()
    main()
    #menuConsola()
# Programa Principal
main()