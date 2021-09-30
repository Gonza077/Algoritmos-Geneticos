from Ciudad import Ciudad
import random
import copy
import CiudadesDAO

class Cromosoma(object):

    IDCromosoma = 1
    Dominio = None
    tCromo = None

    def __init__(self):
        self._funcFitness = 0
        self._genes = []
        self._funcObjetivo = 0
        lista = [ num for num in range(1,25)]
        # Agregar genes al cromosoma hasta llegar a los 23
        while lista:
            pick = random.choice(lista)
            lista.remove(pick)
            self._genes.append(pick)

    def instancioGenesParaCrossover(self):
        # Creo un cromosoma donde todos sus genes tienen el valor 0
        for _ in range(len(self._genes)):
            self._genes.append(0)
    
    def calculoDatosCromosoma(self):
        for i in range(-1, len(self._genes)):
            ciudadActual = CiudadesDAO.getCiudadById(self._genes[i])
            self._funcObjetivo += ciudadActual.getDistanciaTo(self._genes[i+1])

    def calculoFitness(self,sumaPoblacion): 
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada cromosoma"""
        self.funcFitness = self._funcObjetivo / sumaPoblacion

    def mostrarGenes(self):
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
                # print(f"Nro: {genMutado1} - Posicion: {self._genes.index(genMutado1)}")
                # print(f"Nro: {genMutado2} - Posicion: {self._genes.index(genMutado2)}")
                self._genes[aux1] , self._genes[aux2] = genMutado2 , genMutado1
                break
        # print(f"Nro: {genMutado1} - Posicion: {self._genes.index(genMutado1)}")
        # print(f"Nro: {genMutado2} - Posicion: {self._genes.index(genMutado2)}")

