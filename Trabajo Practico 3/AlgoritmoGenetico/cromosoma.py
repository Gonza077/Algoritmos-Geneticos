import random
#import copy
from CiudadDAO import *

class Cromosoma(object):

    IDCromosoma = 1
    Dominio = None
    tCromo = None
    ciudadesDAO = None

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
        # Crear una lista con los números del 1 al 24.
        lista = [ num for num in range(1,24)]

        # Agregar genes al cromosoma hasta llegar a los 24
        while lista:
            pick = random.choice(lista)
            lista.remove(pick)
            self._genes.append(pick)

    def instancioGenesParaCrossover(self):
        # Creo un cromosoma donde todos sus genes tienen el valor 0
        for _ in range(0, 23):
            self._genes.append(0)
    
    def calculoDatosCromosoma(self):
        #ciudadDAO = CiudadesDAO()
        #ciudadDAO.cargarCiudades()
        for i in range(-1, len(self._genes)-1):
            self._funcObjetivo += self.ciudadesDAO.getDistanciaById(self._genes[i], self._genes[i+1])
            

    def calculoFitness(self,sumaPoblacion): 
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada cromosoma"""
        self.funcFitness = 1 - (self._funcObjetivo / sumaPoblacion)

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

    def mutoGen(self):
        while True:
            #Solo se copia el valor, si no se copia la direccion de memoria y se modifica el valor seleccionado
            genMutado1 = random.choice(self._genes)
            genMutado2 = random.choice(self._genes)          
            if genMutado1!=genMutado2:
                #Se necesita un auxiliar por el hecho de que cuando se modifica un valor, se volveria a pisar el mismo indice
                aux1=self._genes.index(genMutado1)
                aux2=self._genes.index(genMutado2)
                #print(f"Nro: {genMutado1} - Posicion: {self._genes.index(genMutado1)}")
                #print(f"Nro: {genMutado2} - Posicion: {self._genes.index(genMutado2)}")
                self._genes[aux1] , self._genes[aux2] = genMutado2 , genMutado1
                break

    @classmethod
    def instanciarCiudades(self):
        ciudadesDAO = CiudadesDAO()
        ciudadesDAO.cargarCiudades()