from Generacion import *
from Poblacion import *
from Cromosoma import *
from OperadoresGeneticos import *
import openpyxl as opyxl

CantPoblaciones=[1]   
generaciones=[]
#Parametros del Parque 
Cromosoma.tCromo=25
Cromosoma.VelocidadViento=25 #Velocidad del viento
Cromosoma.TamañoCelda=180 #Distancia Minima de 4*R, donde R es 45 m
#Parametros de la Poblacion
Poblacion.tPobla=5 #Cantidad de parques x Poblacion
Poblacion.tipoSeleccion=Ruleta()
Poblacion.tipoCrossover=CrossOverUnPunto(0.75)
Poblacion.tipoMutacion=MutacionInvertida(0.20)
Poblacion.elitismo=False

for x in CantPoblaciones:
    generacion=Generacion()
    for _ in range(x):        
        generacion.creoPoblacion()
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
