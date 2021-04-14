import math
import random as rnd
import numpy as npm
import copy 

# ----------------------------------------------------------------------------------------------------
class Cromosoma(object):
    
    IDCromosoma=1

    #Atributos
    def __init__(self):
        self.ID=0
        if(Cromosoma.IDCromosoma >= tPobla):
            Cromosoma.IDCromosoma = 1
        else:
            self.ID=Cromosoma.IDCromosoma
            Cromosoma.IDCromosoma+=1
        self.funcFitness=0
        self.funcObjetivo=0
        self.valorDecimal=0
        self.arrGenes=[]

    def instancioGenes(self):
        for x in range(0,tCromo):
            self.arrGenes.append(rnd.randint(0, 1))
        self.calculaFuncObjetivo()
    
    def datosCromosoma(self):
        print(f"Cromosoma ID: {self.ID}, Func Fitness: {self.funcFitness}, Valor decimal {self.valorDecimal}")
        print(f"Sus genes son: {self.arrGenes}")
    
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

    def mutoGen(self):
        for i in range(0,len(self.arrGenes)):
            if self.arrGenes[i] == 0:
                self.arrGenes[i] = 1
            else:
                self.arrGenes[i]= 0
 # -----------------------------------------------------------------------------------------------------------     

class Poblacion(object):

    """Poblacion genetica del algoritmo"""
    IDPoblacion = 1
    
    #Metodos
    def __init__(self):
        if(Cromosoma.IDCromosoma >= tPobla):
            Poblacion.IDPoblacion = 1
        else:
            self.ID = Poblacion.IDPoblacion
            Poblacion.IDPoblacion +=1       
        self.arrCromosomas=[]
        self.sumaPoblacion=0
        self.mediaPoblacion=0      
        
    def instancioCromosomas(self):
        for x in range(0,tPobla):
            cromosoma = Cromosoma() 
            cromosoma.instancioGenes()      
            self.arrCromosomas.append(cromosoma)

    def calculoSumaPobla(self):
        """Se calcula la suma de la poblacion a partir del valor de cada cromosoma"""
        for cromosoma in self.arrCromosomas:
            self.sumaPoblacion += cromosoma.funcObjetivo
    
    def calculoMediaFO(self):
        """Se calcula la media poblacional"""
        for cromosoma in self.arrCromosomas:
            self.mediaPoblacion += cromosoma.funcObjetivo / len(self.arrCromosomas)

    def buscoMenorYMayorCromosoma(self):
        self.maxCromosoma=self.arrCromosomas[0] #Para poder tener como base el primer cromosoma y comparar el resto
        self.minCromosoma=self.arrCromosomas[0]
        for cromosoma in self.arrCromosomas:
            if (self.maxCromosoma.valorDecimal < cromosoma.valorDecimal):
                self.maxCromosoma = cromosoma
            if (self.minCromosoma.valorDecimal > cromosoma.valorDecimal):
                self.minCromosoma = cromosoma               

    def calcularFitness(self):
        for cromosoma in self.arrCromosomas:        
            cromosoma.calculoFitness(self.sumaPoblacion)

    def calculoValorPoblacion(self):
        self.calculoSumaPobla()
        self.calculoMediaFO()
        self.buscoMenorYMayorCromosoma()
        self.calcularFitness()
    
    def datosPoblacion(self):      
        print("-----------------------------------------------------") 
        print(f"Poblacion ID: {self.ID}, media de la FO fue: {self.mediaPoblacion}")
        """
        for cromosoma in self.arrCromosomas:
                print("-----------------------------------------------------")
                cromosoma.datosCromosoma()
                print("-----------------------------------------------------")
        """
        print(f"El cromosoma {self.maxCromosoma.arrGenes} fue el mas grande y su valor en decimal es {self.maxCromosoma.valorDecimal}")
        print(f"El cromosoma {self.minCromosoma.arrGenes} fue el mas chico y su valor en decimal es {self.minCromosoma.valorDecimal}")
        print("-----------------------------------------------------")
        
# -----------------------------------------------------------------------------------------       

class Generacion(object):
    
    #Atributos de instancia
    def __init__(self):
        self.probCrossover=0.75
        self.probMutacion=0.05       
        self.arrPoblaciones=[]

    #Metodos
    def creoGeneracion(self):
        """Si se ejecuta por primera vez, generara una poblacion, si no, a la ultima existente se le aplicara algun operador genetico"""
        poblacion=Poblacion()
        if(len(self.arrPoblaciones) == 0 ):
            poblacion.instancioCromosomas()
            poblacion.calculoValorPoblacion()
            self.arrPoblaciones.append(poblacion)
        else:
            HASTA ACA LLEGUE
            """
            paresPadres=self.aplicoSeleccionRuleta()     #Devuevle los cromosomas seleccionados en la ruleta      
            poblacion=self.aplicoOperadorCrossover(paresPadres,poblacion) #A los cromosomas seleccionados se les aplica crossover
            poblacion=self.aplicoOperadorMutacion(poblacion)      #Una vez aplicado el crossover, se les aplica la mutacion    
            poblacion.calculoValorPoblacion()
            self.arrPoblaciones.append(poblacion) 
            """
    def aplicoSeleccionRuleta(self):
        ruleta=[]
        valor=0     
        paresPadres=[]
        poblacionASeleccionar=self.arrPoblaciones[-1] #Devuelve el ultimo elemento en el arreglo       
        for cromosoma in poblacionASeleccionar.arrCromosomas:
            valor+=cromosoma.funcFitness
            ruleta.append(round(valor,10)) #Se redondea a 10 digitos por errores de coma flotante de python                                           
        #CUIDADO, ACA PUEDE HABER ALGUN PAR QUE SEA EL MISMO OBJETO, HAY QUE CONSULTAR CON LOS PROFESORES
        for i in range(0,int(tPobla/2)): #Se debe armar 5 pares de longitud 2, tengo que castearlo a entero pro que tira error
            pares=[]
            while ( len(pares) < 2 ): #Se debe armar el par, esto garantiza que siempre se forme
                numAleatorio = rnd.random()       
                for j in range(0,tPobla-1):  #Esto es ya que se debe recorrer toda la ruleta hasta encontrar el intervalo
                    if (numAleatorio >= ruleta[j] and numAleatorio <= ruleta[j+1]):
                        pares.append(poblacionASeleccionar.arrCromosomas[j])
            paresPadres.append(pares)  
        return paresPadres
          
    def aplicoOperadorCrossover(self,padres,poblacion):      
        for i in range(0,int(tPobla/2)):
            padre=padres[i][0] #Padres viene de a pares
            madre=padres[i][1]
            if(rnd.random() <= self.probCrossover):     #Se aplica crossover siel numero generado es mayor a la prob.  
                hijo1=Cromosoma()
                hijo2=Cromosoma() 
                posicionCorte=rnd.randint(0,tCromo)
                for j in range(0,posicionCorte):
                    hijo1.arrGenes.insert(j,padre.arrGenes[j])
                    hijo2.arrGenes.insert(j,madre.arrGenes[j])
                for k in range(posicionCorte,tCromo):
                    hijo1.arrGenes.insert(k,padre.arrGenes[k])
                    hijo2.arrGenes.insert(k,madre.arrGenes[k])
                #Una vez creado cada hijo, se calcula su nueva funcion
                hijo1.calculaFuncObjetivo()
                hijo2.calculaFuncObjetivo()
                poblacion.arrCromosomas.append(hijo1)
                poblacion.arrCromosomas.append(hijo2)
            else: #Si no se aplica, los padres vuelven a ser los hijos
                poblacion.arrCromosomas.append(padre)
                poblacion.arrCromosomas.append(madre)
        return poblacion
            
    def aplicoOperadorMutacion(self,poblacion):      
        if(rnd.random() <= self.probMutacion):
            posicionCorte=rnd.randint(0,tCromo)
            for cromosoma in poblacion.arrCromosomas:
                for i in range(posicionCorte):
                cromosoma.mutoGen()
        return poblacion
# -----------------------------------------------------------------------------------------        

#Main

Dominio=2**30-1  #Dominio es una variable global
#cantCorridas=int(input("Ingrese la cantidad de corridas"))    
#tPobla=int(input("Ingrese el tamaño de la poblacion"))
#tCromo=int(input("Ingrese el tamaño del cromosoma"))
tCromo=30
tPobla=10
cantCorridas=40
generacion=Generacion()

for i in range(0,cantCorridas):  
    generacion.creoGeneracion()
"""
for poblacion in generacion.arrPoblaciones:
    poblacion.datosPoblacion()

"""



