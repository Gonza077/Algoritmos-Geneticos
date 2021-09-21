from AlgoritmoGenetico.cromosoma import *
import copy

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
        for _ in range(0, Poblacion.tPobla):
            cr = Cromosoma()
            cr.instancioGenes()
            self.arrCromosomas.append(cr)

    def calculoSumaPobla(self):
        """Se calcula la suma de la poblacion a partir del valor de cada cromosoma"""
        for cromosoma in self.arrCromosomas:
            self.sumaPoblacion += cromosoma.getFuncObjetivo()

    def calculoMediaFO(self):
        """Se calcula la media poblacional""" 
        self.mediaPoblacionFO = self.sumaPoblacion / len(self.arrCromosomas)

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
        paresPadres=self.tipoSeleccion.aplicarSeleccion(poblacionAnterior,len(self.arrCromosomas))   
        cromosomasNuevos=self.tipoCrossover.aplicoCrossover(paresPadres)  #Por que a los cromosomas del elitismo, no hay que modificarlos 
        self.tipoMutacion.aplicoMutacion(cromosomasNuevos)
        for cromosoma in cromosomasNuevos:
            self.arrCromosomas.append(cromosoma)

    def ATupla(self):
        cadena1="".join([ str(gen) for gen in self.maxCromosoma.arrGenes])  
        cadena2="".join([ str(gen) for gen in self.minCromosoma.arrGenes])       
        return [self.ID,self.minCromosoma.funcObjetivo,cadena2,self.maxCromosoma.funcObjetivo,cadena1,self.mediaPoblacionFO]