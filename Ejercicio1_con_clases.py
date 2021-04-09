import math
import random as rnd


# ----------------------------------------------------------------------------------------------------
class Cromosoma(object):

    #Atributos
    def __init__(self, genes = []):
        self.funcFitness=0
        self.funcObjetivo=0
        self.valorDecimal=0
        self.arrGenes= genes

        if(len(genes) == 0):
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
    
    #Atributos de clase  
    ID = 1
    ProbCrossover = 0.75
    ProbMutacion = 0.05

    #Metodos
    def __init__(self, arrGenes = []):
        self.ID = Poblacion.ID
        
        self.sumaPoblacion=0
        self.mediaPoblacion=0
        self.maxCromosoma = Cromosoma()
        self.minCromosoma=Cromosoma()
        #Esto es por que no puedo instanciar el objeto con el valor
        self.minCromosoma.valorDecimal=5**99
        self.arrGenes = []
        
        # Si arrGenes es vacio es porque es la primera población, sino, es una generación creada a partir de una anterior.
        if(len(arrGenes) == 0):
            for x in range(0,tPobla):
                cromosoma = Cromosoma()        
                self.arrGenes.append(cromosoma)
        else:
            #Si creo una nueva generación a partir de la inicial, cada cromosoma debe crearse a partir de los valores
            #    obtenidos de la fase de reproducción
            for x in range(0, tPobla):
                cromosoma = Cromosoma( genes = arrGenes[i])
                self.arrGenes.append(cromosoma)
                
        Poblacion.ID+=1

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
            if ( self.maxCromosoma.valorDecimal < cromosoma.valorDecimal):
                self.maxCromosoma = cromosoma
            if ( self.minCromosoma.valorDecimal > cromosoma.valorDecimal):
                self.minCromosoma = cromosoma
    
    def calcularFitness(self):
        for cromosoma in self.arrGenes:        
            cromosoma.calculoFitness(self.sumaPoblacion)

    def calculoValorPoblacion(self):
        self.calculoSumaPobla()
        self.calculoMediaFO()
        self.buscoMayorCromosoma()
        self.calcularFitness()

    def seleccionoPadres(self):
        """Se seleccionan los padres teniendo en cuenta su fitness, favoreciendo a los individuos mejores adaptados."""
        padres = []
        listaSumaFit = []
        sumaFit = 0

        # Creo un arreglo con la suma de las funciones Fitness de todos los cromosomas
            # Ej: [0, 0.09, 0.015, ... 1] -> La suma debe ser 1
        for i in range(0, tPobla):
            listaSumaFit.append(sumaFit)
            sumaFit += self.arrGenes[i].funcFitness
    
        # Tiro un número random y veo si en que posición cae dentro del arreglo anterior (listaSumaFit)
            # numAleatorio = 0.26513 cae en la posición 2 del arreglo -> [0, 0.09, 0.15, 0.31, ... 1] 
        for j in range(0, tPobla - 1):
            numAleatorio = rnd.random()
            if( numAleatorio >= listaSumaFit[j] and numAleatorio < listaSumaFit[j + 1]):
                padres.append(j)

        return padres

    def aplicoCrossover(self, padres):
        """Se crean los hijos(cromosomas) utilizando los genes de los padres."""
        hijos = []
        # Este for devuelve 0, 2, 4, 6, 8
        for i in range(0, tPobla, 2):
            probCrossover = rnd.random()
            if(probCrossover < Poblacion.ProbCrossover):
                padre = self.arrGenes[i]
                madre = self.arrGenes[i + 1]
                #La función lista.extend() une las listas en una sola
                hijos.extend(self.aplicoCorte(padre, madre))

        return hijos
    
    def aplicoCorte(self, padre, madre):
        """Se crean dos nuevos hijos con los genes de los padres"""
        hijos = []
        hijo = []
        hija = []

        posicionCorte = rnd.randint(1, 30)
        for i in range(0, posicionCorte):
            hijo.insert(i, padre.arrGenes[i])
            hija.insert(i, madre.arrGenes[i])
        for i in range(posicionCorte, tCromo):
            hijo.insert(i, madre.arrGenes[i])
            hija.insert(i, padre.arrGenes[i])
        
        hijos.append(hijo)
        hijos.append(hija)

        return hijos

    def aplicoMutacion(self, hijos):
        """Se aplica a cada hijo la mutuación, alterando de forma aleatoria pero con una probabilidad pequeña cada gen."""
        hijos = []

        return hijos

    def aplicoFaseReproduciva(self):
        """Se seleccionan los individuos de la población que se cruzaran y se producen los descendientes."""
        padres = []
        hijos = []
        nuevosHijos = []
        padres = self.seleccionoPadres()
        hijos = self.aplicoCrossover(padres)
        # nuevosHijos = self.aplicoMutacion(hijos)

        return Poblacion(arrGenes=hijos)
        
    def muestroValoresPoblacion(self):       
        print(f"Media de la FO fue: {self.mediaPoblacion}")
        print(f"El cromosoma {self.maxCromosoma.arrGenes} fue el mas grande y su valor en decimal es {self.maxCromosoma.valorDecimal}")
        print(f"El cromosoma  {self.minCromosoma.arrGenes} fue el mas chico y su valor en decimal es {self.minCromosoma.valorDecimal}")
        
# -----------------------------------------------------------------------------------------       

class Generacion(object):
    
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
            self.generoNuevaGeneracion(self.poblacion)


    def generoNuevaGeneracion(self, poblacionActual):
        nuevaPoblacion = []
        nuevaPoblacion = self.poblacion.aplicoFaseReproduciva()
        nuevaPoblacion.calculoValorPoblacion()
        self.arrPoblaciones.append(nuevaPoblacion)
        # Aca iria lo de la mutacion
        # self.poblacion=Poblacion() --> Aca no se crea aleatoriamente la poblacion, sino que el AG comienza a generar poblaciones
        # self.poblacion.calculoValorPoblacion()
        # self.arrPoblaciones.append(self.poblacion)

# -----------------------------------------------------------------------------------------        

#Main

Dominio=2**30-1  #Dominio es una variable global
#cantCorridas=int(input("Ingrese la cantidad de corridas"))    
#tPobla=int(input("Ingrese el tamaño de la poblacion"))
#tCromo=int(input("Ingrese el tamaño del cromosoma"))
tCromo=30
tPobla=10
cantCorridas=5
generacion=Generacion()
for i in range(0,cantCorridas):
    generacion.creoGeneracion()

for poblacion in generacion.arrPoblaciones:
    print("-----------------------------------------------------")
    print(f"Los valores de la poblacion {poblacion.ID}:")
    poblacion.muestroValoresPoblacion()
    print("-----------------------------------------------------")