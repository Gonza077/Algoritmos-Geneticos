import random as rnd
from AlgoritmoGenetico.Cromosoma import Cromosoma
import copy

class Poblacion(object):
 
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
        for i in range(Poblacion.tPobla):
            cromosoma = Cromosoma()   
            Cromosoma._idCiudad=Cromosoma.IDCromosoma+1
            self.arrCromosomas.append(cromosoma)
        Cromosoma.IDCromosoma=1

    def calculoSumaPobla(self):
        """Se calcula la suma de la poblacion a partir del valor de cada cromosoma"""
        for cromosoma in self.arrCromosomas:
            self.sumaPoblacion += cromosoma.getFuncObjetivo()

    def buscoMayoresCromosomas(self,poblacionAnterior):
        """ Busca a los dos mayores cromosomas de la poblacion, recibe un arreglo de cromosomas"""
        poblacionAnterior.arrCromosomas.sort(reverse=True)  #Ordena los cromosomas de mayor a menor segun su valor decimal
        self.arrCromosomas.append(copy.deepcopy(poblacionAnterior.arrCromosomas[0]))
        self.arrCromosomas.append(copy.deepcopy(poblacionAnterior.arrCromosomas[1]))

    def calculoDatosPoblacion(self):
        for cromosoma in self.arrCromosomas:
            cromosoma.calculoDatosCromosoma()
        self.calculoSumaPobla()
        for cromosoma in self.arrCromosomas:        
            cromosoma.calculoFitness(self.sumaPoblacion)
        self.calculoMediaFO()

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
        return [self.ID,self.mediaPoblacionFO]