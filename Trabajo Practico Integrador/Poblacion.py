import random as rnd
from ParqueEolico import *
import copy
from enum import Enum

class Poblacion(object):

    IDPoblacion = 1
    CantParques=None
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
        self.sumatoriaPotencia=0     
        self.arrParques=[] 
        Poblacion.IDPoblacion +=1 
        
    def instacioParques(self):
        for _ in range(0,Poblacion.CantParques):
            parqueEolico = ParqueEolico()
            parqueEolico.intancioAerogeneradores()   
            self.arrParques.append(parqueEolico)
        ParqueEolico.reseteoIDParques()

    def calculoSumaPobla(self):
        """Se calcula la suma de la parqueEolico a partir del valor de cada cromosoma"""
        for parque in self.arrParques:
            self.sumatoriaPotencia += parque.potenciaParque

    def calculoDatosParqueEolico(self):
        #Calculo los datos de cada parque
        for parque in self.arrParques:
            parque.calculoPotenciaParque()
        #Calculo la sumatoria de potencia de la poblacion
        self.calculoSumaPobla()
        #Calculo del Fitness de cada parque
        for parque in self.arrParques:   
            parque.calculoFitness(self.sumatoriaPotencia)

    def creoNuevoParqueEolico(self,parqueEolicoAnterior):
        parquesNuevos=[] 
        paresPadres=self.tipoSeleccion.aplicarSeleccion(parqueEolicoAnterior,len(self.arrParques))   
        parquesNuevos=self.tipoCrossover.aplicoCrossover(paresPadres)  #Por que a los cromosomas del elitismo, no hay que modificarlos 
        self.tipoMutacion.aplicoMutacion(parquesNuevos)
        for parque in parquesNuevos:
            self.arrParques.append(cromosoma)
    
    def diseñoParques(self):
        print("---------------------------------------------")
        print(f"Poblacion N°{self.ID}\n")
        for parque in self.arrParques:
            parque.datosParque() 
        print("---------------------------------------------")
