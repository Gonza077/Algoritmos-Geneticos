from generacion import Generacion
from poblacion import Poblacion
from cromosoma import Cromosoma
import operadoresGeneticos
import openpyxl as opyxl

#cantCorridas=int(input("Ingrese la cantidad de corridas"))    
#tPobla=int(input("Ingrese el tamaño de la poblacion"))
#tCromo=int(input("Ingrese el tamaño del cromosoma"))
#Dominio=((2**tCromo) - 1)  #Dominio es una variable global

Corridas=[20,100,200]   
generaciones=[]
Cromosoma.tCromo=30
Cromosoma.Dominio=((2**30)-1)
Poblacion.tPobla=10
Poblacion.tipoSeleccion=operadoresGeneticos.Torneo()
Poblacion.tipoCrossover=operadoresGeneticos.CrossOverUnPunto(0.75)
Poblacion.tipoMutacion=operadoresGeneticos.MutacionInvertida(0.05)
Poblacion.elitismo=True 

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
    
"""
wb = opyxl.Workbook()    
for generacion in generaciones:
    generacion.cargoDatosExcel(wb)
"""

