import random
from CiudadesDAO import CiudadesDAO
import copy

class Cromosoma():
    
    tCromo=None

    def __init__(self):
        self._genes = []
        self._funcObjetivo = 0

        # Crear una lista con las ciudades 
        lista = copy.deepcopy(CiudadesDAO.retornarCiudades()) 

        lista.remove(random.choice(lista)) #Se remueve una ciudad, ya que esta simularia "la ciudad de origen"

        # Agregar genes al cromosoma hasta llegar a las 23 ciudades, la seleccion se hace de forma aleatoria
        while lista:
            pick = random.choice(lista)
            lista.remove(pick)
            self._genes.append(pick)

    def calcularFuncObjetivo(self):
        distTotal = 0
        idCiudades = copy.deepcopy(self._genes)
        while len(idCiudades) != 1:
            ciudadActual = ciudadesDAO[idCiudades[0] - 1]
            ciudadSiguiente = ciudadesDAO[idCiudades[1] - 1]
            distancia = ciudadActual.getDistanciaTo(ciudadSiguiente)
            distTotal += distancia
            idCiudades.pop(0)
        print(f'La distancia total es: {distTotal}')

    def mostrarGenes(self):
        print('Lista de genes:')
        print(self._genes)