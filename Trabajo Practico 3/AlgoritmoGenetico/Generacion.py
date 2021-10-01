from AlgoritmoGenetico.Poblacion import *
import matplotlib.pyplot as plt
import openpyxl as opyxl
from tabulate import tabulate


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

    def datosGeneracion(self):
        tuplas=[]
        for poblacion in self.arrPoblaciones:
            #if (poblacion.ID % ((len(self.arrPoblaciones)/20)) == 0): #Dependiendo del tamaño de la poblacion, y la cantidad de registros que se quieran mostrar, en este caso 20
            tuplas.append(poblacion.ATupla())
        cabecera=["Poblacion","Min. FO","Genes cromosoma menor","Max. FO","Genes cromosoma Mayor","Media FO"]
        print(tabulate(tuplas, headers=cabecera, stralign='center',tablefmt="simple",numalign="center"))
        self.dibujoGrafica()

    def menorCromosoma(self):
        for poblacion in self.arrPoblaciones:
            if(float("inf") > poblacion.minCromosoma.getFuncObjetivo()):
                cr = poblacion.minCromosoma
        return cr