import random as rnd
from cromosoma import Cromosoma
import copy
from enum import Enum

class parqueEolico(object):
 
    """parqueEolico genetica del algoritmo"""
    IDparqueEolico = 1
    tParque=None
    cantMaxCromosomas=25
    tipoCrossover=None
    tipoSeleccion=None
    tipoMutacion=None


    #Metodo de clase
    @staticmethod
    def reseteoIDparqueEolico():
        parqueEolico.IDparqueEolico=1

    #Metodos de instancia
    def __init__(self):
        self.ID = parqueEolico.IDparqueEolico
        parqueEolico.IDparqueEolico +=1       
        self.arrCromosomas=[]
        self.potencia=0
        self.mediaPotencia=0   
        
    def instancioCromosomas(self):
        for _ in range(0,parqueEolico.tParque):
            cromosoma = Cromosoma() 
            cromosoma.instancioGenes()   
            self.arrCromosomas.append(cromosoma)

    def calculoSumaPobla(self):
        """Se calcula la suma de la parqueEolico a partir del valor de cada cromosoma"""
        for cromosoma in self.arrCromosomas:
            #Aca tendriamos que calcular cada potencia en base si hay molinos adelante del mismo
            #Hay que pensar como hacerlo
            self.potencia += cromosoma.funcObjetivo / self.cantMaxCromosomas

    def calculoMediaFO(self):
        """Se calcula la media parqueEolicoal""" 
        self.mediaPotencia = self.potencia / len(self.arrCromosomas)

    def calculoDatosparqueEolico(self):
        for cromosoma in self.arrCromosomas:
            cromosoma.calculoDatosCromosoma()
        self.calculoSumaPobla()
        for cromosoma in self.arrCromosomas:        
            cromosoma.calculoFitness(self.potencia)
        self.calculoMediaFO()

    def creoNuevoParqueEolico(self,parqueEolicoAnterior):
        cromosomasNuevos=[] 
        paresPadres=self.tipoSeleccion.aplicarSeleccion(parqueEolicoAnterior,len(self.arrCromosomas))   
        cromosomasNuevos=self.tipoCrossover.aplicoCrossover(paresPadres)  #Por que a los cromosomas del elitismo, no hay que modificarlos 
        self.tipoMutacion.aplicoMutacion(cromosomasNuevos)
        for cromosoma in cromosomasNuevos:
            self.arrCromosomas.append(cromosoma)