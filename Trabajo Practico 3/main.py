from UserInterface import uiPyQT
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from Ciudad import *
import pandas as pd
import numpy as np
from AlgoritmoGenetico.Cromosoma import *
from AlgoritmoGenetico.Poblacion import *
from AlgoritmoGenetico.OperadoresGeneticos import *
from AlgoritmoGenetico.Generacion import *

def cargarCiudades():
    ciudades=[]
    hojaExcel = pd.read_excel('./TablaCapitales.xlsx')
    for fila in hojaExcel.values:
        ciudad=Ciudad()
        ciudad.agregarNombre(fila[0])
        for j in range(1,len(fila)):
            ciudad.agregarCiudad(hojaExcel.columns[j])
        ciudades.append(ciudad)
    return ciudades

def nombreCiudades():
    nombres=[]
    for ciudad in ciudades:
        nombres.append(ciudad._nombre)
    return nombres

ciudades=cargarCiudades()

for ciudad in ciudades:
    ciudad.datosCiudad()

def getCiudad(listaCiudades, nombre):
    for ciu in listaCiudades:
        if ciu.getNombre().lower() == nombre.lower():
            return ciu
            
def buscarRuta(listaCiudades, nombreCiudad):
    ruta = []
    ciudad = Ciudad()

    # Se supone que ingresa siempre una ciudad válida
    ciudad = getCiudad(listaCiudades, nombreCiudad)

    # TORESEARCH Solución a un error de tipos de datos, 
    #   TODO/DONE https://realpython.com/python-type-checking/#type-systems
    
    ruta.append(ciudad)
    # Tengo que ir descartando de la busqueda las ciudades que ya estan en el arreglo de rutas.
    #     Creo que va a hacer el arreglo de ciudades con objetos y no con tuplas.
    proxCiudad = ciudad.getCiudadMasCercana(ruta)
    
    # TODO No esta funcionando el corte. Cuando llega a la ultima ciudad deberia cortar y tira error
    while len(ruta) <= 23:
        ruta.append(proxCiudad)
        # Le tengo que pedir a la lista de ciudades que cargamos desde Pandas
        #     donde esta la proxima mas cercana.
        ciudad = getCiudad(listaCiudades, proxCiudad.getNombre())
        proxCiudad = ciudad.getCiudadMasCercana(ruta)
    # Saco la ciudad inicial, ya que luego la agregamos al final
    ruta.pop(0)
    # Agrego la distancia de la ciudad final a la incial, nos dijo Victor en clase que lo hagamos.
    proxCiudad = ciudad.getCiudadMasCercana(ruta)
    ruta.append(proxCiudad)

    return ruta

def buscarRutaMinima(listaCiudades):
    rutaMinima = []
    # Uso esta distancia mínima para buscar la menor, se podría hacer de una mejor manera, OBVIO.
    distanciaMinima = 100000

    for ciu in listaCiudades:
        ruta = buscarRuta(listaCiudades, ciu.getNombre())
        arreglo_distancias = list(map(lambda x:x.getDistancia(), ruta))
        distTotal = np.sum(arreglo_distancias)
        if (distTotal < distanciaMinima):
            distanciaMinima = distTotal
            rutaMinima = ruta
        print(f"La ruta mínima desde {ciu.getNombre()} es de:{distTotal} Km.")
        # print(f'{list(map(lambda x:x.getNombre(), ruta))}')

    return rutaMinima

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
        ruta = buscarRuta(ciudades, ciudad_origen)
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
        ruta = buscarRutaMinima(ciudades)
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