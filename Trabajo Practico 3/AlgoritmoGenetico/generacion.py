from AlgoritmoGenetico.poblacion import *

class Generacion(object):
    
    #Atributos de instancia
    def __init__(self):    
        self.arrPoblaciones=[]

    #Metodos
    def creoGeneracion(self):
        """Si se ejecuta por primera vez, generara una poblacion, si no, a la ultima existente se le aplicara algun operador genetico"""
        poblacion=Poblacion()
        if(self.arrPoblaciones == [] ): 
            poblacion.instancioCromosomas()       
        else:              
            poblacion.creoNuevaPoblacion(self.arrPoblaciones[-1])      
        poblacion.calculoDatosPoblacion()                     
        self.arrPoblaciones.append(poblacion)