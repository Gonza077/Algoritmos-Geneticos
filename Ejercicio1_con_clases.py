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

    #Metodos
    def instancioGen(self,tamaño):
        self.arrGenes=[]
        for x in range(0,tamaño):
            self.arrGenes.append(rnd.randint(0,1))
        self.calculaFuncObjetivo()
        pass

    def transformoBinarioAEntero(self):
        """Se calculara el valor genetico del cromosoma en numero entero"""
        valor=0
        #Convierto el arreglo de numeros en una cadena para posteriormente pasarla a binario 
        cadena = "".join([str(_) for _ in self.arrGenes])
        valor = int(cadena, 2)
        return valor

    def calculaFuncObjetivo(self):
        """Se calcula el valor de cada cromosoma"""       
        self.funcObjetivo = (self.transformoBinarioAEntero() / Dominio) ** 2 #Dominio se define en el cuerpo principal
    
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
    minPoblacion.funcObjetivo=5**99

    #Metodos
    def instancioPoblacion(self,tPoblacion,tCromosoma):
        for x in range(0,tPoblacion):
            cromosoma = Cromosoma() 
            cromosoma.instancioGen(tCromosoma)          
            self.arrPoblacion.append(cromosoma)

    def calculoSumaPobla(self):
        """Se calcula la suma de la poblacion a partir del valor de cada cromosoma"""
        for cromosoma in self.arrPoblacion:
            self.sumaPoblacion += cromosoma.funcObjetivo
    
    def calculoMediaPobla(self):
        """Se calcula la media poblacional"""
        self.mediaPoblacion = self.sumaPoblacion / len(self.arrPoblacion)

    def buscoMayorCromosoma(self):     
        for cromosoma in self.arrPoblacion:
            if ( self.maxPoblacion.funcObjetivo < cromosoma.funcObjetivo):
                self.maxPoblacion = cromosoma
            if ( self.minPoblacion.funcObjetivo> cromosoma.funcObjetivo):
                self.minPoblacion = cromosoma
    
    def calculoValorPoblacion(self):
        self.calculoSumaPobla()
        self.calculoMediaPobla()
        self.buscoMayorCromosoma()
        self.calcularFitness()
        
    def muestroValoresPoblacion(self):
        print("Los valores de la poblacion fueron:")
        print("La media poblacional fue: ",self.mediaPoblacion)
        print("El maximo valor de la poblacion fue: ",self.maxPoblacion.funcObjetivo)
        print("El minimo valor de la poblacion fue: ",self.minPoblacion.funcObjetivo)

    def calcularFitness(self):
        for x in self.arrPoblacion:        
            x.calculoFitness(self.sumaPoblacion)

    def generarNuevaGeneracion(self):
        pass

        
class Generacion(object):

    #Atributos
    arrPoblaciones=[]

    #Metodos
    def creoGeneracion(self):
        """Si se ejecuta por primera vez, generara una poblacion, si no, a la existente ya le aplicara la mutacion"""
        if(self.arrPoblaciones.__sizeof__()==0):
            tCromo=int(input("Ingrese el tamaño del cromosoma"))
            tPobla=int(input("Ingrese el tamaño de la poblacion"))
            poblacion = Poblacion(tPobla,tCromo)
            self.arrPoblaciones.append(tPobla,tCromo)
        else:
            generoNuevaGeneracion()

    def generoNuevaGeneracion(self):
        pass
        

def programaPrincipal():
    """
    tCromo=int(input("Ingrese el tamaño del cromosoma"))
    tPobla=int(input("Ingrese el tamaño de la poblacion"))
    poblacion = Poblacion(tPobla,tCromo)
    """
    poblacion = Poblacion()
    poblacion.instancioPoblacion(10,30)
    poblacion.calculoValorPoblacion()
    poblacion.muestroValoresPoblacion()

#Main

Dominio=2**30-1  #Dominio es una variable global
programaPrincipal()
