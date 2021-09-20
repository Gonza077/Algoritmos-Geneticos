from Ciudad import *
from CiudadesDAO import CiudadesDAO
import pandas as pd
import numpy as np

def getCiudad(nombre):
    for ciu in CiudadesDAO.retornarCiudades():
        if ciu.getNombre().lower() == nombre.lower():
            return ciu
            
def buscarRuta(nombreCiudad):
    ruta = []
    ciudad = Ciudad()

    # Se supone que ingresa siempre una ciudad válida
    ciudad = getCiudad(nombreCiudad)

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
        ciudad = getCiudad(proxCiudad.getNombre())
        proxCiudad = ciudad.getCiudadMasCercana(ruta)
    # Saco la ciudad inicial, ya que luego la agregamos al final
    ruta.pop(0)
    # Agrego la distancia de la ciudad final a la incial, nos dijo Victor en clase que lo hagamos.
    proxCiudad = ciudad.getCiudadMasCercana(ruta)
    ruta.append(proxCiudad)
    return ruta

def buscarRutaMinima():
    rutaMinima = []
    # Uso esta distancia mínima para buscar la menor, se podría hacer de una mejor manera, OBVIO.
    distanciaMinima = float("inf")

    for ciu in CiudadesDAO.retornarCiudades():
        ruta = buscarRuta(ciu.getNombre())
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

