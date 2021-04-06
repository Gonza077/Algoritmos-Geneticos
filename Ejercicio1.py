import math
import random as rnd

class Cromosoma(object):

    #Atributos
    funcObjetivo=0  
    tamGen=[]

    #Metodos
    def __init__(self,tamaño):
        self.tamGen=[]
        for x in range(0,tamaño):
            self.tamGen.append(rnd.randint(0,1))
        self.calculaFuncObjetivo()

    def transformoBinarioAEntero(self):
        """Se calculara el valor genetico del cromosoma en numero entero"""
        valor=0
        #Convierto el arreglo de numeros en una cadena para posterormente pasarla a binario 
        cadena = "".join([str(_) for _ in self.tamGen])
        valor = int(cadena, 2)
        return valor

    def calculaFuncObjetivo(self):
        """Se calcula el valor de cada cromosoma"""       
        self.funcObjetivo = (self.transformoBinarioAEntero() / Dominio) ** 2 #Dominio se define en el cuerpo principal

class Poblacion(object):
    """Poblacion genetica del algoritmo"""

    #Atributos
    tamPoblacion=[]
    sumaPoblacion=0
    mediaPoblacion=0
    maxPoblacion=0

    #Metodos
    def __init__(self,tPoblacion,tCromosoma):
        for x in range(0,tPoblacion):
            cromosoma = Cromosoma(tCromosoma)           
            self.tamPoblacion.append(cromosoma)

    def calculoSumaPobla(self):
        """Se calcula la suma de la poblacion a partir del valor de cada cromosoma"""
        for x in range(0,len(self.tamPoblacion)):
            self.sumaPoblacion += self.tamPoblacion[x].funcObjetivo
    
    def calculoMediaPobla(self):
        """Se calcula la media poblacional"""
        self.mediaPoblacion = self.sumaPoblacion / len(self.tamPoblacion)

    def buscoMayorCromosoma(self):
        for x in range(0,len(self.tamPoblacion)):
            if(self.maxPoblacion < self.tamPoblacion[x].funcObjetivo):
                self.maxPoblacion = self.tamPoblacion[x].funcObjetivo
    
    def calculoValorPoblacion(self):
        self.calculoSumaPobla()
        self.calculoMediaPobla()
        self.buscoMayorCromosoma()
        
    def muestroValoresPoblacion(self):
        print("Los valores de la poblacion fueron:")
        print("Suma de la poblacion: ",self.sumaPoblacion)
        print("La media poblacional fue: ",self.mediaPoblacion)
        print("El maximo valor de la poblacion fue: ",self.maxPoblacion)


def programaPrincipal():
    """
    tCromo=int(input("Ingrese el tamaño del cromosoma"))
    tPobla=int(input("Ingrese el tamaño de la poblacion"))
    poblacion = Poblacion(tPobla,tCromo)
    """
    poblacion = Poblacion(10,30)
    poblacion.calculoValorPoblacion()
    poblacion.muestroValoresPoblacion()

#Main

Dominio=2**30-1  #Dominio es una variable global
programaPrincipal()


"""
Dominio= 5
poblacion = Poblacion(10,5)
#poblacion.calculoValorPoblacion()
#poblacion.muestroValoresPoblacion()
print("Datos primer cromosoma",poblacion.tamPoblacion[0].tamGen)
print("Valor Genetico: ",poblacion.tamPoblacion[0].transformoBinarioAEntero())"""


