import math
import random as rnd

class Cromosoma(object):

    gen=[]
    fitness=0  

    def __init__(self,tamaño):
        for x in range(0,tamaño-1):
            self.gen.append(rnd.randint(0,1))

    def calculoFitness(self):
        """Se calcula el valor de cada cromosoma"""
        for i in range((len(self.gen)) - 1, 0, -1):    
            self.fitness = self.fitness + 2 ** i * self.gen[i]     

crom = Cromosoma(30)


