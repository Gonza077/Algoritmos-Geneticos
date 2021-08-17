import random as rnd
import numpy as np
import math

class ParqueEolico(object):
    
    IDParque=1
    CantAeroGeneradores=None
    TamañoCelda=None
    velViento=None

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

    def calculoDatosParque(self):
        """Se calcula la potencia total de cada parque"""  
        for fila in self.terrenoParque:
            velViento=ParqueEolico.velViento #Se inicializa la velocidad inicial del viento proveniente de la Izquierda hacia la Derecha
            aeroFilas=np.where(fila==1)[0] #Devuelve una tupla con un arreglo y el tipo de dato, solo tomo el arreglo
            if(len(aeroFilas)>=2):  #Si existen al menos dos generadores en una fila existira el efecto estela
                #Efecto estela simpe
                for i in range(0,len(aeroFilas)-1):
                    velViento = self.efectoEstela(velViento,aeroFilas[i+1]-aeroFilas[i]) #Distancia en indices entre cada aerogenerador
                    #print(f"La distancia entre AeroGenerador N° {aeroFilas[i] +1} y {aeroFilas[i+1] +1} es {aeroFilas[i+1]-aeroFilas[i]} de la fila {fila}")
                    
                    self.calculoPotenciaAerogenerador(velViento)
            else:
                self.calculoPotenciaAerogenerador(velViento)    

    def efectoEstela(self,velViento,disIndices):
        a=0.3333
        radioAero=45
        coefDeArrastre= round(( 1 / (2 * math.log(80/0.05))),4) #Aproximadamente 0.0678
        return velViento * ( 1 - ( 2 * a / (1 + (coefDeArrastre * disIndices*ParqueEolico.TamañoCelda) / radioAero )**2) ) 

    def calculoPotenciaAerogenerador(self,velViento):
        #Aca deberia calcularse la potencia que cada aerogenerador generaria dependiendo de la velocidad del viento
        #Habria que definir un arreglo que contenga las velocidades y la potencia que se genera
        #Cada potencia se puede tomar de la pagina donde encontramos los aerogeneradores, esa que aparece en el grafico
        pass

        
    def calculoFitness(self,sumaPoblacion): 
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada parque"""
        self.funcFitness = self.potenciaParque / sumaPoblacion

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
        print(f"Func Fitness: {self.fitnessParque}, Potencia Parque: {self.potenciaParque}")
        for fila in self.terrenoParque:
            print(fila)
 
    def distribucionParque(self):
        for fila in self.terrenoParque:
            print(fila)
        print()