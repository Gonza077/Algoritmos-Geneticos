import math
import random as rnd

"""
    Para hacer:
     - Generar la nueva generación: hay que aplicar 
"""
class Cromosoma(object):

    #Atributos
    funcObjetivo=0  
    arrGenes=[]
    funcFitness=0
    valorDecimal=0

    #Metodos
    def instancioGen(self,tamaño):
        self.arrGenes=[]
        for x in range(0,tamaño):
            self.arrGenes.append(rnd.randint(0,1))
        self.calculaFuncObjetivo()

    def transformoBinarioAEntero(self):
        """Se calculara el valor genetico del cromosoma en numero entero"""
        #Convierto el arreglo de numeros en una cadena para posteriormente pasarla a binario 
        cadena = "".join([str(_) for _ in self.arrGenes])
        self.valorDecimal = int(cadena, 2)

    def calculaFuncObjetivo(self):
        """Se calcula el valor de cada cromosoma"""      
        self.transformoBinarioAEntero()
        self.funcObjetivo = (self.valorDecimal / Dominio) ** 2 #Dominio se define en el cuerpo principal
    
    def calculoFitness(self,sumaPoblacion):
      """Dependiendo de la suma de la poblacion, se calcula el fitness de cada cormosoma"""
      self.funcFitness = self.funcObjetivo / sumaPoblacion
      

class Poblacion(object):
    """Poblacion genetica del algoritmo"""

    #Atributos
    arrPoblacion=[]
    sumaPoblacion=0
    mediaPoblacion=0
    #Instancio
    maxPoblacion=Cromosoma()
    minPoblacion=Cromosoma()
    minPoblacion.valorDecimal=5**99
   

    #Metodos
    def instancioPoblacion(self,tPoblacion,tCromosoma):
        for x in range(0,tPoblacion):
            cromosoma = Cromosoma() 
            cromosoma.instancioGen(tCromosoma)          
            self.arrPoblacion.append(cromosoma)

    def calculoSumaPobla(self):
        """Se calcula la suma de la poblacion a partir del valor de cada cromosoma"""
        for cromosoma in self.arrPoblacion:
            self.sumaPoblacion += cromosoma.valorDecimal
    
    def calculoMediaFO(self):
        """Se calcula la media poblacional"""
        for cromosoma in self.arrPoblacion:
            self.mediaPoblacion += cromosoma.funcObjetivo / len(self.arrPoblacion)

    def buscoMayorCromosoma(self):     
        for cromosoma in self.arrPoblacion:
            if ( self.maxPoblacion.valorDecimal < cromosoma.valorDecimal):
                self.maxPoblacion = cromosoma
            if ( self.minPoblacion.valorDecimal > cromosoma.valorDecimal):
                self.minPoblacion = cromosoma
    
    def calculoValorPoblacion(self):
        self.calculoSumaPobla()
        self.calculoMediaFO()
        self.buscoMayorCromosoma()
        self.calcularFitness()
        
    def muestroValoresPoblacion(self):
        print("----------------------------------")
        print("Los valores de la poblacion fueron:")
        print("La media de la FO fue: ",self.mediaPoblacion)

        print("El maximo valor de la poblacion fue: ",self.maxPoblacion.valorDecimal)
        print("El minimo valor de la poblacion fue: ",self.minPoblacion.valorDecimal)
        print("----------------------------------")

    def calcularFitness(self):
        for cromosoma in self.arrPoblacion:        
            cromosoma.calculoFitness(self.sumaPoblacion)

    def generarNuevaGeneracion(self):
        pass

        
class Generacion(object):

    #Atributos
    arrPoblaciones=[]
    probCrossover = 0.75
    probMutacion =0.05

    #Metodos
    def creoGeneracion(self):
        """Si se ejecuta por primera vez, generara una poblacion, si no, a la existente ya le aplicara la mutacion"""
        if(len(self.arrPoblaciones) == 0 ):
            poblacion = Poblacion()
            poblacion.instancioPoblacion(tPobla, tCromo)
            poblacion.calculoValorPoblacion()
            poblacion.muestroValoresPoblacion()
            self.arrPoblaciones.append(poblacion)
        else:
            self.generoNuevaGeneracion()

    def generoNuevaGeneracion(self):
        pass
        

def programaPrincipal():
    #cantidadCorridas=int(input("Ingrese la cantidad de corridas"))    
    #tPobla=int(input("Ingrese el tamaño de la poblacion"))
    #tCromo=int(input("Ingrese el tamaño del cromosoma"))
    tCromo=30
    tPobla=10
    cantidadCorridas=20
    i=0
    while (i<cantidadCorridas):
        Generacion().creoGeneracion()
        i+=1

#Main
Dominio=2**30-1  #Dominio es una variable global
programaPrincipal()
