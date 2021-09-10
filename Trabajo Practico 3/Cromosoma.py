import random

class Cromosoma():

    def __init__(self):
        self._genes = []

        # Crear una lista con los números del 1 al 23.
        lista = [ num for num in range(1,24)]

        # Agregar genes al cromosoma hasta llegar a los 23
        while lista:
            pick = random.choice(lista)
            lista.remove(pick)
            self._genes.append(pick)


    def mostrarGenes(self):
        print('Lista de genes:')
        print(self._genes)