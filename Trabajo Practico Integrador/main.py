from Generacion import *
from Poblacion import *
from ParqueEolico import *
from OperadoresGeneticos import *
import openpyxl as opyxl


Corridas=[1500]   
generaciones=[]
#Parametros del Parque
ParqueEolico.cantAerogeneradores=25
#Parametros de la Poblacion
Poblacion.TamañoCelda=90
Poblacion.CantParques=50
Poblacion.tipoSeleccion=Ruleta()
Poblacion.tipoCrossover=CrossOverUnPunto(0.75)
Poblacion.tipoMutacion=MutacionInvertida(0.20)
#Parametos de los parques

#Poblacion.elitismo=False 

for x in Corridas:
    generacion=Generacion()
    for _ in range(x):        
        generacion.creoGeneracion()
    Poblacion.reseteoIDPoblacion() #Metodo de clase que vuelve el ID a 1
    generaciones.append(generacion)

print("\n")
for generacion in generaciones:
    generacion.datosGeneracion()
    print("\n")

#Esto es para registrar los datos en el excel
"""
wb = opyxl.Workbook()    
for generacion in generaciones:
    generacion.cargoDatosExcel(wb)
"""

