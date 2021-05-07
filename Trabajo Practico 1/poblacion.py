import random as rnd
from cromosoma import Cromosoma
from enum import Enum

class Poblacion(object):
 
    """Poblacion genetica del algoritmo"""
    IDPoblacion = 1
    tPobla=None
    tipoCrossover=None
    tipoSeleccion=None
    tipoMutacion=None
    elitismo=None

    #Metodo de clase
    @staticmethod
    def reseteoIDPoblacion():
        Poblacion.IDPoblacion=1

    #Metodos de instancia
    def __init__(self):
        self.ID = Poblacion.IDPoblacion
        Poblacion.IDPoblacion +=1       
        self.arrCromosomas=[]
        self.sumaPoblacion=0
        self.mediaPoblacionFO=0   
        
    def instancioCromosomas(self):
        for _ in range(0,Poblacion.tPobla):
            cromosoma = Cromosoma() 
            cromosoma.instancioGenes()   
            self.arrCromosomas.append(cromosoma)

    def calculoSumaPobla(self):
        """Se calcula la suma de la poblacion a partir del valor de cada cromosoma"""
        for cromosoma in self.arrCromosomas:
            self.sumaPoblacion += cromosoma.funcObjetivo

    def calculoMediaFO(self):
        """Se calcula la media poblacional""" 
        self.mediaPoblacionFO = self.sumaPoblacion / len(self.arrCromosomas)

    def buscoMenorCromosoma(self):
        self.minCromosoma=self.arrCromosomas[0] 
        for cromosoma in self.arrCromosomas:               
            if (self.minCromosoma > cromosoma):
                self.minCromosoma = cromosoma               
    
    def buscoMayorCromosoma(self):
        """ Busca al mayor cromosoma de la poblacion instnaciada"""
        self.maxCromosoma=self.arrCromosomas[0] 
        for cromosoma in self.arrCromosomas:
            if (self.maxCromosoma < cromosoma):
                self.maxCromosoma = cromosoma

    def buscoMayoresCromosomas(self,poblacionAnterior):
        """ Busca al mayor cromosoma de la poblacion enviada como parametro"""
        cromoMayor1=poblacionAnterior.arrCromosomas[0]
        cromoMayor2=poblacionAnterior.arrCromosomas[1]
        for cromosoma in poblacionAnterior.arrCromosomas:
            if (cromoMayor1 < cromosoma):
                cromoMayor1 = cromosoma
        poblacionAnterior.arrCromosomas.pop(poblacionAnterior.arrCromosomas.index(cromoMayor1))
        for cromosoma in poblacionAnterior.arrCromosomas:
            if (cromoMayor2 < cromosoma):
                cromoMayor2 = cromosoma
        poblacionAnterior.arrCromosomas.append(cromoMayor1)
        self.arrCromosomas.append(cromoMayor1)
        self.arrCromosomas.append(cromoMayor2)
        
    def calculoDatosPoblacion(self):
        for cromosoma in self.arrCromosomas:
            cromosoma.calculoDatosCromosoma()
        self.calculoSumaPobla()
        for cromosoma in self.arrCromosomas:        
            cromosoma.calculoFitness(self.sumaPoblacion)
        self.calculoMediaFO()
        self.buscoMenorCromosoma()
        self.buscoMayorCromosoma()

    def creoNuevaPoblacion(self,poblacionAnterior):
        cromosomasNuevos=[] 
        if (Poblacion.elitismo):
            self.buscoMayoresCromosomas(poblacionAnterior)
        paresPadres=self.tipoSeleccion.aplicarSeleccion(poblacionAnterior,Poblacion.elitismo)   
        cromosomasNuevos=self.tipoCrossover.aplicoCrossover(paresPadres)  #Por que a los cromosomas del elitismo, no hay que modificarlos 
        self.tipoMutacion.aplicoMutacion(cromosomasNuevos)
        for cromosoma in cromosomasNuevos:
            self.arrCromosomas.append(cromosoma)

    def datosPoblacion(self):      
        print(f"Poblacion ID: {self.ID}, media de la FO fue: {self.mediaPoblacionFO}")                  
        cadena1="".join([ str(gen) for gen in self.maxCromosoma.arrGenes])  #Hace el casteo de un arreglo de enteros a una cadena de los genes
        cadena2="".join([ str(gen) for gen in self.minCromosoma.arrGenes])
        print(f"El cromosoma {cadena1} fue el mas grande y su FO es {self.maxCromosoma.funcObjetivo}")
        print(f"El cromosoma {cadena2} fue el mas chico y su FO es {self.minCromosoma.funcObjetivo}")
        print("-----------------------------------------------------")       

    def ATupla(self):
        cadena1="".join([ str(gen) for gen in self.maxCromosoma.arrGenes])  
        cadena2="".join([ str(gen) for gen in self.minCromosoma.arrGenes])       
        return [self.ID,self.minCromosoma.funcObjetivo,cadena2,self.maxCromosoma.funcObjetivo,cadena1,self.mediaPoblacionFO]