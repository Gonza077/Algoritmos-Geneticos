import random as rnd
import numpy as np
import math
import copy 

class Cromosoma(object):
    
    IDCromosoma=1
    tCromo=None
    CantAerogeneradores=None
    TamañoCelda=None
    VelocidadViento=None

    #Atributos
    def __init__(self):   
        self._ID = Cromosoma.IDCromosoma  
        self._funcFitness=0
        self._funcObjetivo=0
        self._genes = np.array([ [0] * Cromosoma.tCromo] * Cromosoma.tCromo) #Definira una matriz de 10*10
        Cromosoma.IDCromosoma +=1

    @staticmethod
    def reseteoIDCromosoma():
         Cromosoma.IDCromosoma=1
    
    #Operadores logicos, ya que Python no permite comparar obejtos 
    def __gt__(self, parque):
        return self._funcObjetivo > parque._funcObjetivo

    def __lt__(self, parque):
        return self._funcObjetivo < parque._funcObjetivo

    def __ge__(self, parque):
        return self._funcObjetivo >= parque._funcObjetivo

    def __le__(self, parque):
        return self._funcObjetivo <= parque._funcObjetivo

    def __eq__(self, parque):
        return self._funcObjetivo == parque._funcObjetivo

    def __ne__(self, parque):
        return self._funcObjetivo != parque._funcObjetivo

    #Metodos de instancia
    def calculoFuncObjetivo(self):
        self._funcObjetivo=0
        """Se calcula la potencia total de cada parque""" 
        for fila in self._genes:
            velViento=Cromosoma.VelocidadViento 
            aeroFilas=np.where(fila==1)[0] #Devuelve una tupla con un arreglo y el tipo de dato, solo tomo el arreglo
            if(len(aeroFilas)>0):
                self.calculoPotenciaAerogenerador(velViento)
                if(len(aeroFilas)>=2):  #Si existen al menos dos generadores en una fila existira el efecto estela
                    for i in range(1,len(aeroFilas)):
                        velViento = self.efectoEstela(velViento,aeroFilas[i]-aeroFilas[i-1]) #Distancia en indices entre cada aerogenerador
                        self.calculoPotenciaAerogenerador(velViento)

    def efectoEstela(self,velViento,distanciaCasillas):
        a=0.3333
        radioAero=45
        coefDeArrastre= round(( 1 / (2 * math.log(80/0.05))),4) #Aproximadamente 0.0678
        return velViento * ( 1 - ( 2 * a / (1 + (coefDeArrastre * distanciaCasillas * Cromosoma.TamañoCelda) / radioAero )**2) ) 

    def calculoPotenciaAerogenerador(self,velViento):  
        #Cada indice de la lista contiene una lista donde el primer indice indica la velocidad del viento y el segundo la potencia asociada  
        velocidadesViento=[[0, 0],[1, 0],[2, 0],[3, 10],[4, 46],[5, 170],[6, 355],[7, 580],[8, 874],[9, 1219],[10, 1544],[11, 1740],[12, 1789],[13, 1800],[14, 1800],[15, 1800],[16, 1800],[17, 1800],[18, 1800],[19, 1800],[20, 1800],[21, 1800],[22, 1800],[23, 1800],[24, 1800],[25, 1800],[26, 0]]
        for i in range(len(velocidadesViento)-1):
            if velocidadesViento[i][0]<=velViento and velocidadesViento[i+1][0]>velViento:
                self._funcObjetivo += velocidadesViento[i][1]
                break
    
    def getFuncObjetivo(self):
        return self._funcObjetivo
    
    def getFuncFitness(self):
        return self._funcFitness
    
    def getGenes(self):
        return self._genes
        
    def calculoFitness(self,sumaPoblacion): 
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada parque"""
        self._funcFitness = self._funcObjetivo / sumaPoblacion

    def getAerogeneradores(self):
        cantAeros=0
        for fila in self._genes:
            cantAeros += len(np.where(fila==1)[0])
        print(cantAeros)

    def mutoGen(self):
        listaAux=[]
        for fila in self._genes.tolist():
            print(fila)
            while True:
                #Se tomaran dos indices de la fila para hacer el intercambio de los genes
                IndiceGenMutado1 = rnd.randint(0, len(fila)-1)
                IndiceGenMutado2 = rnd.randint(0, len(fila)-1)   
                print(f"Indice N°1: {IndiceGenMutado1} - Valor{fila[IndiceGenMutado1]}")
                print(f"Indice N°2: {IndiceGenMutado2} - Valor{fila[IndiceGenMutado2]}")
                #Se verifica que los indices sean distintos
                if IndiceGenMutado1!=IndiceGenMutado2:
                    #Se copia el valor de los indices
                    aux1=fila[IndiceGenMutado1]
                    aux2=fila[IndiceGenMutado2]
                    fila[IndiceGenMutado1] , fila[IndiceGenMutado2] = aux2 , aux1
                    listaAux.append(fila)
                    break             
        self._genes=np.array(listaAux)

    def insertoGen(self,gen,fila,col):
        self._genes[fila,col]=gen

    def intancioAerogeneradores(self):
        contador=0
        while(contador<Cromosoma.CantAerogeneradores):
            #Se toma un indice de fila al azar
            filRnd=rnd.randrange(len(self._genes))
            colRnd=rnd.randrange(len(self._genes[0]))
            #Se toma un indice de columna al azar
            if self._genes[filRnd,colRnd]!=1:
                self._genes[filRnd,colRnd]=1
                contador+=1
    
    def datosParque(self):
        print(f"Parque N° {self._ID} -- Func.Fitness: {self._funcFitness} -- Func. Objetivo: {self._funcObjetivo} \n")
        print("Diseño del Parque")
        for fila in self._genes:
            print(fila)
        print()

 
        