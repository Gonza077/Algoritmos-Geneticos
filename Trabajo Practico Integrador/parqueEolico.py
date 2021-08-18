import random as rnd
import numpy as np
import math

class ParqueEolico(object):
    
    IDParque=1
    CantAeroGeneradores=None
    TamañoCelda=None
    VelocidadViento=None

    #Atributos
    def __init__(self):   
        self.ID = ParqueEolico.IDParque
        ParqueEolico.IDParque +=1  
        self.fitnessParque=0
        self.potenciaParque=0
        self.terrenoParque=np.array([[0]*10]*10) #Definira una matriz de 10*10

    @staticmethod
    def reseteoIDParques():
         ParqueEolico.IDParque=1
    
    #Operadores logicos, ya que Python no permite comparar obejtos 
    def __gt__(self, parque):
        return self.potenciaParque > parque.potenciaParque

    def __lt__(self, parque):
        return self.potenciaParque < parque.potenciaParque

    def __ge__(self, parque):
        return self.potenciaParque >= parque.potenciaParque

    def __le__(self, parque):
        return self.potenciaParque <= parque.potenciaParque

    def __eq__(self, parque):
        return self.potenciaParque == parque.potenciaParque

    def __ne__(self, parque):
        return self.potenciaParque != parque.potenciaParque

    #Metodos de instancia
    def calculoPotenciaParque(self):
        """Se calcula la potencia total de cada parque"""  
        for fila in self.terrenoParque:
            velViento=ParqueEolico.VelocidadViento #Se inicializa la velocidad inicial del viento proveniente de la Izquierda hacia la Derecha
            aeroFilas=np.where(fila==1)[0] #Devuelve una tupla con un arreglo y el tipo de dato, solo tomo el arreglo
            if(len(aeroFilas)>=2):  #Si existen al menos dos generadores en una fila existira el efecto estela
                #Efecto estela simpe
                for i in range(len(aeroFilas)-1):
                    velViento = self.efectoEstela(velViento,aeroFilas[i+1]-aeroFilas[i]) #Distancia en indices entre cada aerogenerador
                    self.calculoPotenciaAerogenerador(velViento)
            else:
                self.calculoPotenciaAerogenerador(velViento)   

    def efectoEstela(self,velViento,distanciaCasillas):
        a=0.3333
        radioAero=45
        coefDeArrastre= round(( 1 / (2 * math.log(80/0.05))),4) #Aproximadamente 0.0678
        return velViento * ( 1 - ( 2 * a / (1 + (coefDeArrastre * distanciaCasillas * ParqueEolico.TamañoCelda) / radioAero )**2) ) 

    def calculoPotenciaAerogenerador(self,velViento):  
        #Cada indice de la lista contiene una lista donde el primer indice indica la velocidad del viento y el segundo la potencia asociada  
        velocidadesViento=[[0, 0],[1, 0],[2, 0],[3, 10],[4, 46],[5, 170],[6, 355],[7, 580],[8, 874],[9, 1219],[10, 1544],[11, 1740],[12, 1789],[13, 1800],[14, 1800],[15, 1800],[16, 1800],[17, 1800],[18, 1800],[19, 1800],[20, 1800],[21, 1800],[22, 1800],[23, 1800],[24, 1800],[25, 1800],[26, 0]]
        for i in range(len(velocidadesViento)-1):
            if velocidadesViento[i][0]<=velViento and velocidadesViento[i+1][0]>velViento:
                self.potenciaParque += velocidadesViento[i][1]
                break
        
    def calculoFitness(self,sumaPoblacion): 
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada parque"""
        self.fitnessParque = self.potenciaParque / sumaPoblacion

    def mutoGen(self):
        #FALTA DEFINIR
        pass

    def insertoGen(self,gen):
        """Se envia el gen a insertar en el arreglo del parque"""
        #FALTA DEFINIR 
        pass

    def intancioAerogeneradores(self):
        contador=0
        while(contador<ParqueEolico.CantAeroGeneradores):
            contador+=1
            #Se toma un indice de fila al azar
            filRnd=rnd.randrange(len(self.terrenoParque))
            #Se toma un indice de columna al azar
            colRnd=rnd.randrange(len(self.terrenoParque[0]))
            self.terrenoParque[filRnd,colRnd]=1
    
    def datosParque(self):
        print(f"Fitness: {self.fitnessParque}, Potencia Parque: {self.potenciaParque}")
        for fila in self.terrenoParque:
            print(fila)
        print()
 
        