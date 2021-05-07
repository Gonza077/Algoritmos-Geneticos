from enum import Enum
import random as rnd
import cromosoma as cr

class Ruleta():

    def aplicarSeleccion(self,poblacionAnterior,booleano):   
        ruleta=[0]
        valor=0     
        paresPadres=[]         
        for cromosoma in poblacionAnterior.arrCromosomas:       
            valor+=cromosoma.funcFitness
            ruleta.append(valor)
        if (booleano):  #Dependiendo del valor de si se aplica elitismo o no                                  
            for _ in range(4): #Se debe armar 4 pares de longitud 2, tengo que castearlo a entero por que tira error
                pares=[]
                while ( len(pares) < 2 ): #Se debe armar el par, esto garantiza que siempre se forme
                    numAleatorio = rnd.random()     
                    for j in range(len(poblacionAnterior.arrCromosomas)-1):  #Esto es ya que se debe recorrer toda la ruleta hasta encontrar el intervalo
                        if (numAleatorio >= ruleta[j] and numAleatorio < ruleta[j+1]):
                            pares.append(poblacionAnterior.arrCromosomas[j])
                paresPadres.append(pares)
        else:
            for _ in range(5): #Se debe armar 5 pares de longitud 2, tengo que castearlo a entero por que tira error
                pares=[]
                while ( len(pares) < 2 ): #Se debe armar el par, esto garantiza que siempre se forme
                    numAleatorio = rnd.random()     
                    for j in range(len(poblacionAnterior.arrCromosomas)-1):  #Esto es ya que se debe recorrer toda la ruleta hasta encontrar el intervalo
                        if (numAleatorio >= ruleta[j] and numAleatorio < ruleta[j+1]):
                            pares.append(poblacionAnterior.arrCromosomas[j])
                paresPadres.append(pares)
        return paresPadres

class Torneo():

    def aplicarSeleccion(self, poblacionAnterior,booleano):
        t = 2
        paresPadres = []
        if (booleano):
            for _ in range(0,4):
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
        else:
            for _ in range(0,5):
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

class CrossOverUnPunto():

    probCrossover=0.75

    def aplicoCrossover(self,padres):
        nuevosCromosomas=[]
        for par in padres:  #Padres viene de a pares
            padre=par[0] 
            madre=par[1]
            if(rnd.random() <= CrossOverUnPunto.probCrossover):      
                hijo1=cr.Cromosoma()
                hijo2=cr.Cromosoma()
                posicionCorte=rnd.randint(0,cr.Cromosoma.tCromo-1)
                #Se instancia los primeros N genes de cada padre hasta la posicion de corte en cada hijo
                for j in range(0,posicionCorte):
                    hijo1.insertoGen(padre.arrGenes[j])
                    hijo2.insertoGen(madre.arrGenes[j])
                    #Posteriormente se intercambian los genes de cada padre en los hijos, luego de la posicion del corte
                for k in range(posicionCorte,cr.Cromosoma.tCromo):
                    hijo1.insertoGen(madre.arrGenes[k])
                    hijo2.insertoGen(padre.arrGenes[k])             
                #Se guarda cada cromosoma en la nueva poblacion
                nuevosCromosomas.append(hijo1)
                nuevosCromosomas.append(hijo2)          
            else:
                #Se guarda cada cromosoma en la nueva poblacion
                nuevosCromosomas.append(padre)
                nuevosCromosomas.append(madre)       
        return nuevosCromosomas

class MutacionInvertida():

    probMutacion=0.05

    def aplicoMutacion(self,cromosomas):
        for cromosoma in cromosomas:          
            if(rnd.random() <= MutacionInvertida.probMutacion):   
                cromosoma.mutoGen()




