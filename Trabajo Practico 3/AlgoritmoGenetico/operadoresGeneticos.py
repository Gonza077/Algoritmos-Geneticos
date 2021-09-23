from enum import Enum
import random as rnd
from AlgoritmoGenetico.cromosoma import *

class Ruleta():

    def aplicarSeleccion(self,poblacionAnterior,cantCromosomasPobla):
        ruleta=[0]
        valor=0     
        paresPadres=[]         
        for cromosoma in poblacionAnterior.arrCromosomas:       
            valor+=cromosoma.funcFitness
            ruleta.append(valor)
        for _ in range ((len(poblacionAnterior.arrCromosomas) - cantCromosomasPobla) // 2): #Se debe armar 5 pares de longitud 2, tengo que castearlo a entero por que tira error
                pares=[]
                while ( len(pares) < 2 ): #Se debe armar el par, esto garantiza que siempre se forme
                    numAleatorio = rnd.random()     
                    for j in range(len(poblacionAnterior.arrCromosomas)-1):  #Esto es ya que se debe recorrer toda la ruleta hasta encontrar el intervalo
                        if (numAleatorio >= ruleta[j] and numAleatorio < ruleta[j+1]):
                            pares.append(poblacionAnterior.arrCromosomas[j])
                paresPadres.append(pares)
        return paresPadres

class Torneo():

    def aplicarSeleccion(self, poblacionAnterior,cantCromosomasPobla):
        t = 2
        paresPadres = []
        for _ in range ((len(poblacionAnterior.arrCromosomas)- cantCromosomasPobla)//2):
            pares = []
            for _ in range(0, t):
                # Elijo aleatoriamente 2 cromosomas
                crom1 = poblacionAnterior.arrCromosomas[rnd.randint(0,9)]
                crom2 = poblacionAnterior.arrCromosomas[rnd.randint(0,9)]
                if crom1 >= crom2: # Elijo el mejor de ambos
                    pares.append(crom1)
                else:
                    pares.append(crom2)
            paresPadres.append(pares)
        return paresPadres

class CrossOverCiclico():

    def __init__(self,probCross):
        self.probCrossover=probCross

    def aplicoCrossover(self,padres):
        nuevosCromosomas=[]
        #for par in padres:  #Padres viene de a pares
        for par in padres:
            padre=par[0] 
            madre=par[1]
            if(rnd.random() <= self.probCrossover):
                hijo1 = self.getGenesHijo(padre, madre)     
                hijo2 = self.getGenesHijo(madre, padre)
                nuevosCromosomas.append(hijo1)
                nuevosCromosomas.append(hijo2)
            else:
                #Se guarda cada cromosoma en la nueva poblacion
                nuevosCromosomas.append(padre)
                nuevosCromosomas.append(madre)    
        return nuevosCromosomas

    def getGenesHijo(self, padre, madre):
        hijo=Cromosoma()
        hijo.instancioGenesParaCrossover() # todos los genes son 0
        posicionGen = 0 # arranco de la 1er posicion del array
        while True:
            hijo.setGenEnPosicion(padre.getGenEnPosicion(posicionGen), posicionGen) # Inserto el gen en la posicion correspondiente
            gen = madre.getGenEnPosicion(posicionGen)   # Busco el proximo gen a insertar
            posicionGen = self.encontrarGen(gen, padre) # Busco la posicion del proximo gen a insertar
            if(self.encontrarGen(gen, hijo) != None):   # Si el gen ya se encuentra en el hijo, se corta el bucle
                break
        for i in range(0, len(madre.getGenes())):         # Relleno con los genes de "la madre" los que todavia se encuentra en 0
            if(hijo.getGenEnPosicion(i) == 0):
                hijo.setGenEnPosicion(madre.getGenEnPosicion(i), i)
        return hijo

    def encontrarGen(self, gen, cromosoma):
        # Busco el indice de un gen en el array
        # utilizo try - catch porque la funcion index devuelve un error cuando no encuentra un valor
        try:
            genes = cromosoma.getGenes()
            posicionGen = genes.index(gen)
            return posicionGen
        except ValueError:
            return None

class MutacionAdjointSwap():

    def __init__(self,probMuta):
        self.probMutacion=probMuta

    def aplicoMutacion(self,cromosomas):
        for cromosoma in cromosomas:          
            if(rnd.random() <= self.probMutacion):   
                cromosoma.mutoGen()
