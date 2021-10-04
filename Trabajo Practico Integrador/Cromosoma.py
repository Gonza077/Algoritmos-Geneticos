import random as rnd
import numpy as np
import math
import copy 

class Cromosoma(object):
    
    IDParque=1
    tCromo=None
    TamañoCelda=None
    VelocidadViento=None

    #Atributos
    def __init__(self):   
        self.ID = Cromosoma.IDParque  
        self._funcFitness=0
        self._funcObjetivo=0
        self._terrenoParque=np.array([[0]*10]*10) #Definira una matriz de 10*10
        Cromosoma.IDParque +=1

    @staticmethod
    def reseteoIDParques():
         Cromosoma.IDParque=1
    
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
        """Se calcula la potencia total de cada parque""" 
        for fila in self._terrenoParque:
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
        
    def calculoFitness(self,sumaPoblacion): 
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada parque"""
        self._funcFitness = self._funcObjetivo / sumaPoblacion

    def mutoGen(self):
        #FALTA DEFINIR
        pass

    def insertoGen(self,gen):
        """Se envia el gen a insertar en el arreglo del parque"""
        #FALTA DEFINIR 
        pass

    def intancioAerogeneradores(self):
        contador=0
        while(contador<Cromosoma.tCromo):
            #Se toma un indice de fila al azar
            filRnd=rnd.randrange(len(self._terrenoParque))
            colRnd=rnd.randrange(len(self._terrenoParque[0]))
            #Se toma un indice de columna al azar
            if self._terrenoParque[filRnd,colRnd]!=1:
                self._terrenoParque[filRnd,colRnd]=1
                contador+=1
    
    def datosParque(self):
        print(f"Parque N° {self.ID} -- Fitness: {self._funcFitness} -- Potencia Parque: {self._funcObjetivo}")
        for fila in self._terrenoParque:
            print(fila)
        print()

 
        