import random
import numpy as np
from Generacion import *
from Poblacion import *
from ParqueEolico import *
#from OperadoresGeneticos import *

Corridas=[2]   
generaciones=[]
#Parametros del Parque
ParqueEolico.cantAerogeneradores=25
#Parametros de la Poblacion
Poblacion.TamañoCelda=90
Poblacion.CantParques=2

#Testeo de la construccion de la matriz
for x in Corridas:
    generacion=Generacion()
    for _ in range(x):        
        generacion.creoGeneracion()
    Poblacion.reseteoIDPoblacion() #Metodo de clase que vuelve el ID a 1
    generaciones.append(generacion)

for gene in generaciones:
    gene.datosGeneracion()


    

