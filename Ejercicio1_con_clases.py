import math
import random as rnd
import numpy as npm

# ----------------------------------------------------------------------------------------------------
class Cromosoma(object):
    
    IDCromosoma=1
    #Atributos
    def __init__(self):
        if(Cromosoma.IDCromosoma > tPobla):
            Cromosoma.IDCromosoma = 1
        else:
            self.ID=Cromosoma.IDCromosoma
            Cromosoma.IDCromosoma+=1
        self.funcFitness=0
        self.funcObjetivo=0
        self.valorDecimal=0
        self.arrGenes=[]
    
    def calculoDatosCromosoma(self):
        """Se calcula el valor de cada cromosoma"""      
        cadena = "".join([ str(gen) for gen in self.arrGenes])
        self.valorDecimal = int(cadena, 2) #Se transofrma la cadena de genes en un valor en decimal
        self.funcObjetivo = round( ((self.valorDecimal / Dominio) ** 2) ,5) #Dominio se define en el cuerpo principal      

    def calculoFitness(self,sumaPoblacion):
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada cromosoma"""
        self.funcFitness = round(self.funcObjetivo / sumaPoblacion,5)

    def mutoGen(self):
        for i in range(0,len(self.arrGenes)):
            if self.arrGenes[i] == 0:
                self.arrGenes[i] = 1
            else:
                self.arrGenes[i]= 0

    def instancioGenes(self):
        for x in range(0,tCromo):
            self.arrGenes.append(rnd.randint(0, 1))
    
    def insertoGen(self,gen):
        """Se envia el gen a insertar en el arreglo del cromosoma"""
        self.arrGenes.append(gen)

    def datosCromosoma(self):
        print(f"Cromosoma ID: {self.ID}, Func Fitness: {self.funcFitness}, Valor decimal {self.valorDecimal}")
        print(f"Sus genes son: {self.arrGenes}")


 # -----------------------------------------------------------------------------------------------------------     

class Poblacion(object):

    """Poblacion genetica del algoritmo"""
    IDPoblacion = 1
    
    #Metodos
    def __init__(self):
        if(Poblacion.IDPoblacion > cantCorridas):
            Poblacion.IDPoblacion = 1
        else:
            self.ID = Poblacion.IDPoblacion
            Poblacion.IDPoblacion +=1       
        self.arrCromosomas=[]
        self.sumaPoblacion=0
        self.mediaPoblacionFO=0   
        
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
        self.mediaPoblacionFO = round(self.sumaPoblacion / len(self.arrCromosomas),5)

    def buscoMenorYMayorCromosoma(self):
        self.maxCromosoma=self.arrCromosomas[0] #Para poder tener como base el primer cromosoma y comparar el resto
        self.minCromosoma=self.arrCromosomas[0]
        for cromosoma in self.arrCromosomas:
            if (self.maxCromosoma.valorDecimal < cromosoma.valorDecimal):
                self.maxCromosoma = cromosoma
            if (self.minCromosoma.valorDecimal > cromosoma.valorDecimal):
                self.minCromosoma = cromosoma               

    def calculoDatosPoblacion(self):
        for cromosoma in self.arrCromosomas:
            cromosoma.calculoDatosCromosoma()
        self.calculoSumaPobla()
        for cromosoma in self.arrCromosomas:        
            cromosoma.calculoFitness(self.sumaPoblacion)
        self.calculoMediaFO()
        self.buscoMenorYMayorCromosoma()
    
    def datosPoblacion(self):      
        print("-----------------------------------------------------") 
        print(f"Poblacion ID: {self.ID}, media de la FO fue: {self.mediaPoblacionFO}")
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
        if(len(self.arrPoblaciones) == 0 ): #Por si es la poblacion inicial
            poblacion.instancioCromosomas()
            poblacion.calculoDatosPoblacion()
            self.arrPoblaciones.append(poblacion)
        else:
            paresPadres=self.aplicoSeleccionRuleta()     #Devuevle los cromosomas seleccionados en la ruleta      
            poblacion=self.aplicoOperadorCrossover(paresPadres,poblacion) #A los cromosomas seleccionados se les aplica crossover
            #poblacion=self.aplicoOperadorMutacion(poblacion)      #Una vez aplicado el crossover, se les aplica la mutacion    
            poblacion.calculoDatosPoblacion()
            self.arrPoblaciones.append(poblacion)

    def aplicoSeleccionRuleta(self):
        ruleta=[]
        valor=0     
        paresPadres=[]
        poblacionASeleccionar=self.arrPoblaciones[0] #Devuelve la ultima poblacion           
        for cromosoma in poblacionASeleccionar.arrCromosomas:
            valor+=cromosoma.funcFitness
            ruleta.append(round(valor,10)) #Se redondea a 10 digitos por errores de coma flotante de python                                           
        """
        #CUIDADO, ACA PUEDE HABER ALGUN PAR QUE SEA EL MISMO OBJETO, HAY QUE CONSULTAR CON LOS PROFESORES        
        for i in range(0,int(tPobla/2)): #Se debe armar 5 pares de longitud 2, tengo que castearlo a entero pro que tira error
            pares=[]
            while ( len(pares) < 2 ): #Se debe armar el par, esto garantiza que siempre se forme
                numAleatorio = rnd.random()       
                for j in range(0,tPobla-1):  #Esto es ya que se debe recorrer toda la ruleta hasta encontrar el intervalo
                    if (numAleatorio >= ruleta[j] and numAleatorio <= ruleta[j+1]):
                        pares.append(poblacionASeleccionar.arrCromosomas[j])
            paresPadres.append(pares)  
        """
        for i in range(0,int(tPobla/2)):
            pares=[]
            while ( len(pares) < 2 ):
                pares.append(rnd.choice(poblacionASeleccionar.arrCromosomas))
            paresPadres.append(pares)  
        
        return paresPadres
          
    def aplicoOperadorCrossover(self,padres,poblacion):      
        for i in range(0,int(tPobla/2)):
            padre=padres[i][0] #Padres viene de a pares
            madre=padres[i][1]
            if(rnd.random() <= self.probCrossover):     #Se aplica crossover si el numero generado es mayor a la prob.  
                hijo1=Cromosoma()
                hijo2=Cromosoma() 
                posicionCorte=rnd.randint(1, 28)
                #Se instnacia los primeros N genes de cada padre hasta la posicion de corte en cada hijo
                for j in range(0,posicionCorte):
                    hijo1.insertoGen(padre.arrGenes[j])
                    hijo2.insertoGen(madre.arrGenes[j])
                #Posteriormente se intercambian los genes de cada padre en los hijos, luego de la posicion del corte
                for k in range(posicionCorte,tCromo):
                    hijo1.insertoGen(madre.arrGenes[k])
                    hijo2.insertoGen(padre.arrGenes[k])
                poblacion.arrCromosomas.append(hijo1)
                poblacion.arrCromosomas.append(hijo2)
            else: #Si no se aplica, los padres vuelven a ser los hijos
                poblacion.arrCromosomas.append(padre)
                poblacion.arrCromosomas.append(madre)
        return poblacion
            
    def aplicoOperadorMutacion(self,poblacion):      
        if(rnd.random() <= self.probMutacion):
            for cromosoma in poblacion.arrCromosomas:             
                cromosoma.mutoGen()
        return poblacion
# -----------------------------------------------------------------------------------------        

#Main
tCromo=30
tPobla=10
cantCorridas=20
Dominio=((2**tCromo) - 1)  #Dominio es una variable global
#cantCorridas=int(input("Ingrese la cantidad de corridas"))    
#tPobla=int(input("Ingrese el tamaño de la poblacion"))
#tCromo=int(input("Ingrese el tamaño del cromosoma"))
#Dominio=((2**tCromo) - 1)  #Dominio es una variable global
generacion=Generacion()

for i in range(0,cantCorridas):  
    generacion.creoGeneracion()


for poblacion in generacion.arrPoblaciones:  
    poblacion.datosPoblacion()
    """
    for cromosoma in poblacion.arrCromosomas:
        cromosoma.datosCromosoma()
    """