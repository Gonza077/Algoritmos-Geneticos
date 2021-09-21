import random
from CiudadesDAO import CiudadesDAO
import copy

class Cromosoma():
    
    tCromo=None

    def __init__(self):
        self._genes = []
        self._funcObjetivo = 0
        # Crear una lista con las ciudades, se usa deepcopy para no alterar los datos del DAO
        lista = [num for num in range(1,25)] 
        # Agregar genes al cromosoma hasta llegar a las 23 ciudades, la seleccion se hace de forma aleatoria
        while lista:
            pick = random.choice(lista)
            lista.remove(pick)
            self._genes.append(pick)

    def calcularFuncObjetivo(self):
        pass

    def getGenes(self):
        print('Lista de genes:')
        print(self._genes)

    def getFuncObjetivo(self):
        return self._funcObjetivo