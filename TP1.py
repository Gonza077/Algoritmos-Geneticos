import math
import random as rnd


# ----------------------------------------------------------------------------------------------------
class Cromosoma(object):

    #Atributos
    def __init__(self, genes = []):
        self.funcFitness=0
        self.funcObjetivo=0
        self.valorDecimal=0
        self.arrGenes= []

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
        self.funcObjetivo = ( (self.valorDecimal / Dominio) ** 2 )  #Dominio se define en el cuerpo principal

    def calculoFitness(self,sumaPoblacion):
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada cormosoma"""
        fitness = (self.funcObjetivo / sumaPoblacion ) * 100
        self.funcFitness = round(fitness, 6)
            #Redondeo a 2 decimales

    def setArrGenes(self, genes):
        self.arrGenes = genes

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
        for x in range(0,tPobla):
            cromosoma = Cromosoma()        
            self.arrGenes.append(cromosoma)

                
        Poblacion.ID+=1

    def setArrGenes(self, genes):
        self.arrGenes = genes

    def calculoSumaPobla(self):
        """Se calcula la suma de la poblacion a partir del valor de cada cromosoma"""
        for cromosoma in self.arrGenes:
            self.sumaPoblacion += cromosoma.funcObjetivo
    
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

        # Creo el arreglo "listaSumaFit" con la suma de las funciones Fitness de todos los cromosomas
            # Ej: [0, 4.325, 9.53, 15.0, 21,63, 28.5, 35.0, ...,  1] -> La suma debe ser 100
        
        listaSumaFit.append(0) 
            # Inicializo el arreglo con la posición cero en cero porque despues el for recorre 9 elementos del arreglo
            #     de Cromosomas y debería recorrer los 10.
        
        for cromosoma in self.arrGenes:
            sumaFit += cromosoma.funcFitness
            listaSumaFit.append(sumaFit)
        
        print(f" ++++++++++++++++++++ La suma de fitness es: {sumaFit} y el tamaña de arrGenes es {len(self.arrGenes)}")
        print(f"La lista de sumas tiene {len(listaSumaFit)} elementos y es {listaSumaFit}")
        print("-------------------> La lista de fitness es:")
        for i in self.arrGenes:
            print(f"Cromosoma: {self.arrGenes.index(i)} fintess: {i.funcFitness}")
        
        # Tiro un número random y veo en que posición cae dentro del arreglo anterior (listaSumaFit)
            # numAleatorio = 0.26513 cae en la posición 2 del arreglo -> [0, 0.09, 0.15, 0.31, ... 1] 
        for i in range(0, tPobla):
            numAleatorio = rnd.random() * 100
            print(f"El numero aleatorio fue {numAleatorio}")
            for j in range(0, tPobla):
                if( numAleatorio >= listaSumaFit[j] and numAleatorio < listaSumaFit[j + 1]):
                    print("/////////////////////////////////////////////////////////////////")
                    print(f"En la tirada de la ruleta n: {i} se selecciono al padre en posición {j}")
                    print("/////////////////////////////////////////////////////////////////")
                    padres.append(self.arrGenes[j])
                if( numAleatorio >= listaSumaFit[10]): 
                # Si el seleccionado esta en la ultima posición, solo se debe cumplir que sea mayor al ultimo numero del arreglo
                    padres.append(self.arrGenes[9])

        return padres

    def aplicoCrossover(self, padres):
        """Se crean los hijos (cromosomas) utilizando los genes de los padres."""
        hijos = []
        # Este for devuelve 0, 2, 4, 6, 8
        for i in range(0, tPobla, 2):
            probCrossover = rnd.random()
            if(probCrossover < Poblacion.ProbCrossover):
                padre = self.arrGenes[i]
                madre = self.arrGenes[i + 1]
                print(padre.arrGenes)
                print(madre.arrGenes)
                #La función lista.extend() une las listas en una sola
                hijos.extend(self.aplicoCorte(padre, madre))
            else:
                # Si no hay crossover, los padres pasan a formar parte de la siguiente población
                hijos.append(padres[i])
                hijos.append(padres[i + 1])

        # print("En aplico CROSSOVER**************************************")
        # print(f"Longitud de hijos es {len(hijos)}")
        # for i in range(0,4):
        #     print(padres[i].arrGenes)
        # for i in range(0,4):
        #    print(hijos[i].arrGenes)
    
        return hijos
    
    def aplicoCorte(self, padre, madre):
        """Se crean dos nuevos hijos con los genes de los padres"""
        hijos = []
        genesHijo = []
        genesHija = []

        posicionCorte = rnd.randint(1, tCromo)
        for i in range(0, posicionCorte):
            genesHijo.insert(i, padre.arrGenes[i])
            genesHija.insert(i, madre.arrGenes[i])
        for i in range(posicionCorte, tCromo):
            genesHijo.insert(i, madre.arrGenes[i])
            genesHija.insert(i, padre.arrGenes[i])
        
        # Creo los dos nuevos hijos y les paso sus arreglos de genes
        #    Si bien el constructo de genes va a crear un conjunto de genes, estos los sobreescritos por el método setArrGenes()
        hijo = Cromosoma()
        hijo.setArrGenes(genesHijo)
        hija = Cromosoma()
        hija.setArrGenes(genesHija)

        hijos.append(hijo)
        hijos.append(hija)

        return hijos

    def aplicoMutacion(self, hijos):
        """Se aplica a cada hijo la mutuación, alterando de forma aleatoria pero con una probabilidad pequeña cada gen."""
        tempHijos = []
        for cromosoma in hijos:
            for i in range(0, tCromo):
                probMutacion = rnd.random()
                if probMutacion < Poblacion.ProbMutacion:
                    if (cromosoma.arrGenes[i] == 0): cromosoma.arrGenes[i] = 1
                    else: cromosoma.arrGenes[i] = 0
            tempHijos.append(cromosoma)

        return tempHijos

    def aplicoFaseReproduciva(self):
        """Se seleccionan los individuos de la población que se cruzaran y se producen los descendientes."""
        padres = []
        hijos = []
        nuevosHijos = []
        padres = self.seleccionoPadres()
        hijos = self.aplicoCrossover(padres)
        nuevosHijos = self.aplicoMutacion(hijos)

        nuevaPoblacion = Poblacion()
        nuevaPoblacion.setArrGenes(nuevosHijos)
        nuevaPoblacion.calculoValorPoblacion()
        return nuevaPoblacion
        
    def muestroValoresPoblacion(self):       
        print(f"Media de la Población {self.ID} fue: {self.mediaPoblacion}")
        print(f"La suma de la población es {self.sumaPoblacion}")
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
        nuevaPoblacion = None
        nuevaPoblacion = self.poblacion.aplicoFaseReproduciva()
        self.arrPoblaciones.append(nuevaPoblacion)
        # Aca iria lo de la mutacion
        # self.poblacion=Poblacion() --> Aca no se crea aleatoriamente la poblacion, sino que el AG comienza a generar poblaciones
        # self.poblacion.calculoValorPoblacion()
        # self.arrPoblaciones.append(self.poblacion)

# -----------------------------------------------------------------------------------------        

#Main
tCromo=20
tPobla=10
cantCorridas=15
Dominio=2**tCromo-1  #Dominio es una variable global
#cantCorridas=int(input("Ingrese la cantidad de corridas"))    
#tPobla=int(input("Ingrese el tamaño de la poblacion"))
#tCromo=int(input("Ingrese el tamaño del cromosoma"))
generacion=Generacion()
for i in range(0,cantCorridas):
    generacion.creoGeneracion()

for poblacion in generacion.arrPoblaciones:
    print("-----------------------------------------------------")
    print(f"Los valores de la poblacion {poblacion.ID}:")
    poblacion.muestroValoresPoblacion()
    print("-----------------------------------------------------")


