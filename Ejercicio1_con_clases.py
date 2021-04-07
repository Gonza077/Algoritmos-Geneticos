import math
import random as rnd

"""
    Para hacer:
     - Generar la nueva generación: hay que aplicar 
"""
# ----------------------------------------------------------------------------------------------------
class Cromosoma(object):

    #Atributos
    def __init__(self):
        self.funcFitness=0
        self.funcObjetivo=0
        self.valorDecimal=0
        self.arrGenes=[]
        for x in range(0,tCromo):
            self.arrGenes.append(rnd.randint(0, 1))
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

 # -----------------------------------------------------------------------------------------------------------     

class Poblacion(object):
    """Poblacion genetica del algoritmo"""

    #Metodos
    def __init__(self):
        self.arrGenes=[]
        self.sumaPoblacion=0
        self.mediaPoblacion=0
        self.maxGen = Cromosoma()
        self.minGen=Cromosoma()
        #Esto es por que no puedo instanciar el objeto con el valor
        self.minGen.valorDecimal=5**99 
        for x in range(0,tPobla):
            cromosoma = Cromosoma()        
            self.arrGenes.append(cromosoma)

    def calculoSumaPobla(self):
        """Se calcula la suma de la poblacion a partir del valor de cada cromosoma"""
        for cromosoma in self.arrGenes:
            self.sumaPoblacion += cromosoma.valorDecimal
    
    def calculoMediaFO(self):
        """Se calcula la media poblacional"""
        for cromosoma in self.arrGenes:
            self.mediaPoblacion += cromosoma.funcObjetivo / len(self.arrGenes)

    def buscoMayorCromosoma(self):     
        for cromosoma in self.arrGenes:
            if ( self.maxGen.valorDecimal < cromosoma.valorDecimal):
                self.maxGen = cromosoma
            if ( self.minGen.valorDecimal > cromosoma.valorDecimal):
                self.minGen = cromosoma
    
    def calcularFitness(self):
        for cromosoma in self.arrGenes:        
            cromosoma.calculoFitness(self.sumaPoblacion)

    def calculoValorPoblacion(self):
        self.calculoSumaPobla()
        self.calculoMediaFO()
        self.buscoMayorCromosoma()
        self.calcularFitness()
        
    def muestroValoresPoblacion(self):
        print("----------------------------------")
        print("Los valores de la poblacion fueron:")
        print("La media de la FO fue: ",self.mediaPoblacion)
        print("El maximo valor de la poblacion fue: ",self.maxGen.valorDecimal)
        print("El minimo valor de la poblacion fue: ",self.minGen.valorDecimal)
        print("----------------------------------")


# -----------------------------------------------------------------------------------------       

class Generacion(object):

    #Atributos de clase  
    probCrossover = 0.75
    probMutacion = 0.5
    
    #Atributos de instancia
    def __init__(self):
        self.poblacion=Poblacion()
        self.arrPoblaciones=[]

    #Metodos
    def creoGeneracion(self):
        """Si se ejecuta por primera vez, generara una poblacion, si no, a la existente ya le aplicara la mutacion"""
        if(len(self.arrPoblaciones) == 0 ):
            self.poblacion.calculoValorPoblacion()
            self.arrPoblaciones.append(self.poblacion)
        else:
            self.generoNuevaGeneracion()


    def generoNuevaGeneracion(self):
        #Aca iria lo de la mutacion
        self.poblacion=Poblacion()
        self.poblacion.calculoValorPoblacion()
        self.arrPoblaciones.append(self.poblacion)
        pass

# -----------------------------------------------------------------------------------------        

#Main

Dominio=2**30-1  #Dominio es una variable global
#cantCorridas=int(input("Ingrese la cantidad de corridas"))    
#tPobla=int(input("Ingrese el tamaño de la poblacion"))
#tCromo=int(input("Ingrese el tamaño del cromosoma"))
tCromo=30
tPobla=10
cantCorridas=1
generacion=Generacion()
for i in range(0,cantCorridas):
    generacion.creoGeneracion()

for poblacion in generacion.arrPoblaciones:
    print(poblacion.muestroValoresPoblacion())