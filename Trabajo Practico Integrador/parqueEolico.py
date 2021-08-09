import random as rnd
import numpy as np

class ParqueEolico(object):
    
    IDParque=1
    cantAerogeneradores=None

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
        """Se calcula el valor de cada parque"""  
        #FALTA CALCULAR LOS VALORES DEL PARQUE
        
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
        while(contador<ParqueEolico.cantAerogeneradores):
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