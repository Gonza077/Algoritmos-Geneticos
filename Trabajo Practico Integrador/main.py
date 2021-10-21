from Generacion import *
from Poblacion import *
from Cromosoma import *
from OperadoresGeneticos import *
import openpyxl as opyxl

CantPoblaciones=[50]   
generaciones=[]
#Parametros del Parque 
Cromosoma.tCromo=10  #Sera una matriz de 10x10
Cromosoma.CantAerogeneradores=25
Cromosoma.VelocidadViento=8 #Velocidad del viento [m/s]
Cromosoma.TamañoCelda=180 #Distancia Minima de 4*R, donde R es 45 m [m]
#Parametros de la Poblacion
Poblacion.tPobla=50 #Cantidad de cromosomas x Poblacion
Poblacion.tipoSeleccion=Ruleta()
Poblacion.tipoCrossover=CrossOverUnPunto(0.8)
Poblacion.tipoMutacion=MutacionInvertida(0.05)
Poblacion.elitismo=True

for x in CantPoblaciones:
    generacion=Generacion()
    for _ in range(x):        
        generacion.creoPoblacion()
    Poblacion.reseteoIDPoblacion() #Metodo de clase que vuelve el ID a 1
    generaciones.append(generacion)

#Se crea una archivo XLSX y se elimina la primer pagina
wb = opyxl.Workbook() 
wb.remove(wb.active) 
print("\n")
for generacion in generaciones:
    generacion.datosGeneracion(wb)
    print("\n")


