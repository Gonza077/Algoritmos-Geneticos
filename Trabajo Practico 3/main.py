from Ciudad import *
import pandas as pd
import numpy as np

def cargarCiudades():
    ciudades=[]
    hojaExcel = pd.read_excel('./TablaCapitalesOriginal.xlsx')
    for fila in hojaExcel.values:
        ciudad=Ciudad()
        ciudad.agregarNombre(fila[0])
        for j in range(1,len(fila)):
            ciudad.agregarCiudad(hojaExcel.columns[j], fila[j])
        ciudades.append(ciudad)
    return ciudades

ciudades=cargarCiudades()

# for ciudad in ciudades:
#     ciudad.datosCiudad()

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
    # Agrego la ultima ciudad que encontro
    ruta.append(ciudad)
    # Agrego al final de nuevo la ciudad inicial, nos dijo en clase Victor que lo hagamos
    ciudad  = getCiudad(listaCiudades, nombreCiudad)
    ruta.append(ciudad)
        
    return ruta

def condicionFiltro(x):
    return type(x.getDistancia()) == float

# Se podría meter todo esto en una función
def main():
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
        for c in ruta:
            print(f"Ciudad: {c.getNombre()} - Distancia {c.getDistancia()}")
        #
        ciudades_filtradas = list(filter(condicionFiltro, ruta))
        print(f"Lista de ciudades filtradas: {ciudades_filtradas}")
        arreglo_distancias = list(map(lambda x:x.getDistancia(), ciudades_filtradas))
        print(f"Lista de ciudades mapeadas: {arreglo_distancias}")
        print(f"Total de ciudades mapeadas: {len(arreglo_distancias)}")
        print(f"La distancia total es: {np.sum(arreglo_distancias)}")

# Programa Principal
main()