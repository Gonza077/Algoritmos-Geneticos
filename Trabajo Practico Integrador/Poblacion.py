import random as rnd
from Cromosoma import *
import copy

class Poblacion(object):

    IDPoblacion = 1
<<<<<<< HEAD
    CantParques=None
=======
    tPobla=None
>>>>>>> gonza
    tipoCrossover=None
    tipoSeleccion=None
    tipoMutacion=None

    #Metodo de clase
    @staticmethod
    def reseteoIDPoblacion():
        Poblacion.IDPoblacion=1

    #Metodos de instancia
    def __init__(self):
<<<<<<< HEAD
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
=======
        self._ID = Poblacion.IDPoblacion 
        self._sumaPoblacion=0     
        self._arrCromosomas=[] 
        self._mediaPoblacionFO=0
        self._minCromosoma = None
        self._maxCromosoma = None
        Poblacion.IDPoblacion +=1
      
    def instacioParques(self):
        for _ in range(0,Poblacion.tPobla):
            cromosoma = Cromosoma()
            cromosoma.intancioAerogeneradores()   
            self._arrCromosomas.append(cromosoma)
        Cromosoma.reseteoIDCromosoma()

    def calculoSumaPobla(self):
        """Se calcula la suma de la Cromosoma a partir del valor de cada cromosoma"""
        for cromosoma in self._arrCromosomas:
            self._sumaPoblacion += cromosoma.getFuncObjetivo()

    def calculoMediaFO(self):
        """Se calcula la media poblacional""" 
        self._mediaPoblacionFO = self._sumaPoblacion / len(self._arrCromosomas)

    def calculoDatosPoblacion(self):
        for cromosoma in self._arrCromosomas:
            cromosoma.calculoFuncObjetivo()
        self.calculoSumaPobla()
        self.calculoMediaFO()
        for cromosoma in self._arrCromosomas:   
            cromosoma.calculoFitness(self._sumaPoblacion)
        self.buscoMayorCromosoma()
        self.buscoMenorCromosoma()

    def buscoMenorCromosoma(self):
        self._minCromosoma=copy.deepcopy(self._arrCromosomas[0]) #Deepcopy nos permite tomar el objeto sin hacer referencia a la memoria
        for cromosoma in self._arrCromosomas:               
            if (self._minCromosoma > cromosoma):
                self._minCromosoma = copy.deepcopy(cromosoma)    
    
    def buscoMayorCromosoma(self):
        """ Busca al mayor cromosoma de la poblacion instnaciada"""
        self._maxCromosoma=copy.deepcopy(self._arrCromosomas[0])  #Deepcopy nos permite tomar el objeto sin hacer referencia a la memoria
        for cromosoma in self._arrCromosomas:
            if (self._maxCromosoma < cromosoma):
                self._maxCromosoma= copy.deepcopy(cromosoma) 

    def buscoMayoresCromosomas(self,poblacionAnterior):
        """ Busca al mayor cromosoma de la poblacion enviada como parametro"""
        poblacionAnterior._arrCromosomas.sort(reverse=True)  #Ordena los cromosomas de mayor a menor segun su valor decimal
        self._arrCromosomas.append(copy.deepcopy(poblacionAnterior._arrCromosomas[0]))
        self._arrCromosomas.append(copy.deepcopy(poblacionAnterior._arrCromosomas[1]))
        self._arrCromosomas.append(copy.deepcopy(poblacionAnterior._arrCromosomas[2]))
        self._arrCromosomas.append(copy.deepcopy(poblacionAnterior._arrCromosomas[3]))
    
    def creoNuevaPoblacion(self,poblacionAnterior):
        cromosomasNuevos=[] 
        if (Poblacion.elitismo):
            self.buscoMayoresCromosomas(poblacionAnterior)
        paresPadres=self.tipoSeleccion.aplicarSeleccion(poblacionAnterior,len(self._arrCromosomas))
        cromosomasNuevos=self.tipoCrossover.aplicoCrossover(paresPadres)  #Por que a los cromosomas del elitismo, no hay que modificarlos 
        self.tipoMutacion.aplicoMutacion(cromosomasNuevos)
        for cromosoma in cromosomasNuevos:
            self._arrCromosomas.append(cromosoma)

    def ATupla(self):    
        return [self._ID,self._minCromosoma.getFuncObjetivo(),self._maxCromosoma.getFuncObjetivo(),self._mediaPoblacionFO,self._sumaPoblacion]

    def getMediaPoblacion(self):
        return self._mediaPoblacionFO

    def getMinCromosoma(self):
        return self._minCromosoma
    
    def getMaxCromosoma(self):
        return self._maxCromosoma

    def getCromosomas(self):
        return self._arrCromosomas
    
    def getSumaPoblacional(self):
        return self._sumaPoblacion

    def diseñoParques(self):
        print("---------------------------------------------")
        print(f"Poblacion N°{self._ID}\n")
        for cromosoma in self._arrCromosomas:
            cromosoma.datosParque() 
>>>>>>> gonza
        print("---------------------------------------------")
