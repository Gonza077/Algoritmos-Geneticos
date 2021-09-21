import random
import copy

class Cromosoma(object):

    IDCromosoma = 1
    Dominio = None
    tCromo = None

    def __init__(self):
        self._funcFitness = 0
        self._genes = []
        self._funcObjetivo = 0
        self._valorDecimal = 0

    #Operadores logicos, ya que Python no permite comparar obejtos 
    def __gt__(self, cromosoma):
        return self._valorDecimal > cromosoma._valorDecimal

    def __lt__(self, cromosoma):
        return self._valorDecimal < cromosoma._valorDecimal

    def __ge__(self, cromosoma):
        return self._valorDecimal >= cromosoma._valorDecimal

    def __le__(self, cromosoma):
        return self._valorDecimal <= cromosoma._valorDecimal

    def __eq__(self, cromosoma):
        return self._valorDecimal == cromosoma._valorDecimal

    def __ne__(self, cromosoma):
        return self._valorDecimal != cromosoma._valorDecimal

    def instancioGenes(self):
        # Crear una lista con los números del 1 al 23.
        lista = [ num for num in range(1,24)]

        # Agregar genes al cromosoma hasta llegar a los 23
        while lista:
            pick = random.choice(lista)
            lista.remove(pick)
            self._genes.append(pick)

    def instancioGenesParaCrossover(self):
        # Creo un cromosoma donde todos sus genes tienen el valor 0
        for _ in range(0, 23):
            self._genes.append(0)
    
    def calculoDatosCromosoma(self):
        for i in range(-1, len(self._genes)):
            self._funcObjetivo += self._genes[i].getDistanciaTo(self._genes[i+1])

    def calculoFitness(self,sumaPoblacion): 
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada cromosoma"""
        self.funcFitness = self._funcObjetivo / sumaPoblacion

    def mostrarGenes(self):
        print('Lista de genes:')
        print(self._genes)

    def setGenEnPosicion(self, gen, posicion):
        #Por el momento supongo que la lista esta instanciada
        self._genes[posicion] = gen

    def getGenEnPosicion(self, posicion):
        return self._genes[posicion]

    def getGenes(self):
        return self._genes

    def getFuncObjetivo(self):
        return self._funcObjetivo

    def getFitness(self):
        return self._funcFitness