import random as rnd
from cromosoma import Cromosoma

class Poblacion(object):

    """Poblacion genetica del algoritmo"""
    IDPoblacion = 1
    tPobla=None
    probCrossover=None
    probMutacion=None

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
        self.mediaPoblacionFO = round( self.sumaPoblacion / len(self.arrCromosomas) ,5)

    def buscoMenorCromosoma(self):
        self.minCromosoma=self.arrCromosomas[0] 
        for cromosoma in self.arrCromosomas:               
            if (self.minCromosoma> cromosoma):
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
            if (cromoMayor2 < cromosoma ):
                cromoMayor2 = cromosoma
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

    def datosPoblacion(self):      
        print(f"Poblacion ID: {self.ID}, media de la FO fue: {self.mediaPoblacionFO}")                  
        cadena1="".join([ str(gen) for gen in self.maxCromosoma.arrGenes])  #Hace el casteo de un arreglo de enteros a una cadena de los genes
        cadena2="".join([ str(gen) for gen in self.minCromosoma.arrGenes])
        print(f"El cromosoma {cadena1} fue el mas grande y su FO es {self.maxCromosoma.funcObjetivo}")
        print(f"El cromosoma {cadena2} fue el mas chico y su FO es {self.minCromosoma.funcObjetivo}")
        print("-----------------------------------------------------")
        
    def aplicoSeleccionRuleta(self,poblacionAnterior):
        ruleta=[0]
        valor=0     
        paresPadres=[]         
        for cromosoma in poblacionAnterior.arrCromosomas:       
            valor+=cromosoma.funcFitness
            ruleta.append(valor)                                        
        for _ in range(int(Poblacion.tPobla/2)): #Se debe armar 5 pares de longitud 2, tengo que castearlo a entero por que tira error
            pares=[]
            while ( len(pares) < 2 ): #Se debe armar el par, esto garantiza que siempre se forme
                numAleatorio = rnd.random()     
                for j in range(Poblacion.tPobla-1):  #Esto es ya que se debe recorrer toda la ruleta hasta encontrar el intervalo
                    if (numAleatorio >= ruleta[j] and numAleatorio < ruleta[j+1]):
                        pares.append(poblacionAnterior.arrCromosomas[j])
            paresPadres.append(pares)  
        return paresPadres

    def seleccionTorneo(self, poblacionAnterior):
        t = 2
        paresPadres = []
        for _ in range(0,5):
            pares = []
            for _ in range(0, t):
                # Elijo aleatoriamente 2 cromosomas
                crom1 = poblacionAnterior.arrCromosomas[rnd.randint(0,9)]
                crom2 = poblacionAnterior.arrCromosomas[rnd.randint(0,9)]
                if crom1.valorDecimal >= crom2.valorDecimal: # Elijo el mejor de ambos
                    pares.append(crom1)
                else:
                    pares.append(crom2)
            paresPadres.append(pares)
        return paresPadres
    
    def aplicoOperadorCrossover(self,padres):     
        for par in padres:  #Padres viene de a pares
            padre=par[0] 
            madre=par[1]
            if(rnd.random() <= Poblacion.probCrossover):      
                hijo1=Cromosoma()
                hijo2=Cromosoma()
                posicionCorte=rnd.randint(0,Cromosoma.tCromo-1)
                #Se instancia los primeros N genes de cada padre hasta la posicion de corte en cada hijo
                for j in range(0,posicionCorte):
                    hijo1.insertoGen(padre.arrGenes[j])
                    hijo2.insertoGen(madre.arrGenes[j])
                #Posteriormente se intercambian los genes de cada padre en los hijos, luego de la posicion del corte
                for k in range(posicionCorte,Cromosoma.tCromo):
                    hijo1.insertoGen(madre.arrGenes[k])
                    hijo2.insertoGen(padre.arrGenes[k])  
                #Luego una vez de aplicars el crossover se aplica la mutacion a los hijos             
                self.aplicoOperadorMutacion(hijo1)
                self.aplicoOperadorMutacion(hijo2)
                #Se guarda cada cromosoma en la nueva poblacion
                self.arrCromosomas.append(hijo1)
                self.arrCromosomas.append(hijo2)          
            else:
                #Se aplica mutacion a los padres
                self.aplicoOperadorMutacion(padre)
                self.aplicoOperadorMutacion(madre)
                #Se guarda cada cromosoma en la nueva poblacion
                self.arrCromosomas.append(padre)
                self.arrCromosomas.append(madre)

    def aplicoOperadorMutacion(self,cromosoma):
        if(rnd.random()<= Poblacion.probMutacion):   
            cromosoma.mutoGen()

    def creoNuevaPoblacion(self,poblacionAnterior):             
        paresPadres=self.aplicoSeleccionRuleta(poblacionAnterior)     
        self.aplicoOperadorCrossover(paresPadres)

    def aplicoElitismo(self,poblacionAnterior):
        self.buscoMayoresCromosomas(poblacionAnterior)
        self.creoNuevaPoblacion(poblacionAnterior)

    def aplicoTorneo(self, poblacionAnterior):
        paresPadres = self.seleccionTorneo(poblacionAnterior)
        self.aplicoOperadorCrossover(paresPadres)

    def ATupla(self):
        cadena1="".join([ str(gen) for gen in self.maxCromosoma.arrGenes])  
        cadena2="".join([ str(gen) for gen in self.minCromosoma.arrGenes])       
        return [self.ID,self.minCromosoma.funcObjetivo,cadena2,self.maxCromosoma.funcObjetivo,cadena1,self.mediaPoblacionFO]