import random as rnd
from Cromosoma import *
import copy
from enum import Enum

class Poblacion(object):

    IDPoblacion = 1
    tPobla=None
    tipoCrossover=None
    tipoSeleccion=None
    tipoMutacion=None

    #Metodo de clase
    @staticmethod
    def reseteoIDPoblacion():
        Poblacion.IDPoblacion=1

    #Metodos de instancia
    def __init__(self):
        self.ID = Poblacion.IDPoblacion 
        self.sumaPoblacion=0     
        self.arrCromosomas=[] 
        self.mediaPoblacionFO=0
        self.minCromosoma = None
        self.maxCromosoma = None
        Poblacion.IDPoblacion +=1
      
    def instacioParques(self):
        for _ in range(0,Poblacion.tPobla):
            cromosoma = Cromosoma()
            cromosoma.intancioAerogeneradores()   
            self.arrCromosomas.append(cromosoma)
        Cromosoma.reseteoIDCromosoma()

    def calculoSumaPobla(self):
        """Se calcula la suma de la Cromosoma a partir del valor de cada cromosoma"""
        for cromosoma in self.arrCromosomas:
            self.sumaPoblacion += cromosoma.getFuncObjetivo()

    def calculoMediaFO(self):
        """Se calcula la media poblacional""" 
        self.mediaPoblacionFO = self.sumaPoblacion / len(self.arrCromosomas)

    def calculoDatosPoblacion(self):
        for cromosoma in self.arrCromosomas:
            cromosoma.calculoFuncObjetivo()
        self.calculoSumaPobla()
        self.calculoMediaFO()
        for cromosoma in self.arrCromosomas:   
            cromosoma.calculoFitness(self.sumaPoblacion)
        self.buscoMayorCromosoma()
        self.buscoMenorCromosoma()

    def creoNuevoCromosoma(self,CromosomaAnterior):
        cromosomasNuevos=[] 
        paresPadres=self.tipoSeleccion.aplicarSeleccion(CromosomaAnterior,len(self.arrCromosomas))   
        cromosomasNuevos=self.tipoCrossover.aplicoCrossover(paresPadres)  #Por que a los cromosomas del elitismo, no hay que modificarlos 
        self.tipoMutacion.aplicoMutacion(cromosomasNuevos)
        for parque in cromosomasNuevos:
            self.arrCromosomas.append(cromosoma)

    def buscoMenorCromosoma(self):
        self.minCromosoma=copy.deepcopy(self.arrCromosomas[0]) #Deepcopy nos permite tomar el objeto sin hacer referencia a la memoria
        for cromosoma in self.arrCromosomas:               
            if (self.minCromosoma > cromosoma):
                self.minCromosoma = copy.deepcopy(cromosoma)    
    
    def buscoMayorCromosoma(self):
        """ Busca al mayor cromosoma de la poblacion instnaciada"""
        self.maxCromosoma=copy.deepcopy(self.arrCromosomas[0])  #Deepcopy nos permite tomar el objeto sin hacer referencia a la memoria
        for cromosoma in self.arrCromosomas:
            if (self.maxCromosoma < cromosoma):
                self.maxCromosoma= copy.deepcopy(cromosoma) 

    def buscoMayoresCromosomas(self,poblacionAnterior):
        """ Busca al mayor cromosoma de la poblacion enviada como parametro"""
        poblacionAnterior.arrCromosomas.sort(reverse=True)  #Ordena los cromosomas de mayor a menor segun su valor decimal
        self.arrCromosomas.append(copy.deepcopy(poblacionAnterior.arrCromosomas[0]))
        self.arrCromosomas.append(copy.deepcopy(poblacionAnterior.arrCromosomas[1]))
    
    def creoNuevaPoblacion(self,poblacionAnterior):
        cromosomasNuevos=[] 
        if (Poblacion.elitismo):
            self.buscoMayoresCromosomas(poblacionAnterior)
        paresPadres=self.tipoSeleccion.aplicarSeleccion(poblacionAnterior,len(self.arrCromosomas))
        cromosomasNuevos=self.tipoCrossover.aplicoCrossover(paresPadres)  #Por que a los cromosomas del elitismo, no hay que modificarlos 
        self.tipoMutacion.aplicoMutacion(cromosomasNuevos)
        for cromosoma in cromosomasNuevos:
            self.arrCromosomas.append(cromosoma)

    def ATupla(self):    
        return [self.ID,self.minCromosoma.getFuncObjetivo(),self.maxCromosoma.getFuncObjetivo(),self.mediaPoblacionFO]

    def diseñoParques(self):
        print("---------------------------------------------")
        print(f"Poblacion N°{self.ID}\n")
        for cromosoma in self.arrCromosomas:
            cromosoma.datosParque() 
        print("---------------------------------------------")
