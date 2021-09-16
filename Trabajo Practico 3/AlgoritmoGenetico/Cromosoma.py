import random
from CiudadesDAO import CiudadesDAO
import copy

class Cromosoma():

    def __init__(self):
        self._genes = []
        self._funcObjetivo = 0

        # Crear una lista con los números del 1 al 23.
        lista = [ num for num in range(1,24)]

        # Agregar genes al cromosoma hasta llegar a los 23
        while lista:
            pick = random.choice(lista)
            lista.remove(pick)
            self._genes.append(pick)

    def calcularFuncObjetivo(self):
        distTotal = 0
        idCiudades = copy.deepcopy(self._genes)
        # Solo para prueba
        ciudadesDAO = cargarCiudades()
        # self.minCromosoma=copy.deepcopy(self.arrCromosomas[0])
        while len(idCiudades) != 1:
            ciudadActual = ciudadesDAO[idCiudades[0] - 1]
            ciudadSiguiente = ciudadesDAO[idCiudades[1] - 1]
            distancia = ciudadActual.getDistanciaTo(ciudadSiguiente)
            distTotal += distancia
            idCiudades.pop(0)

        print(f'La distancia total es: {distTotal}')

    def mostrarGenes(self):
        print('Lista de genes:')
        print(CiudadesDAO.retornarCiudades())
        print(self._genes)