from generacion import Generacion
from poblacion import Poblacion
from cromosoma import Cromosoma
import operadoresGeneticos
import openpyxl as opyxl

Corridas=[1500]   
generaciones=[]
Cromosoma.tCromo=50
Cromosoma.Dominio=((2**30)-1)
Poblacion.tParque=50
Poblacion.tipoSeleccion=operadoresGeneticos.Ruleta()
Poblacion.tipoCrossover=operadoresGeneticos.CrossOverUnPunto(0.75)
Poblacion.tipoMutacion=operadoresGeneticos.MutacionInvertida(0.20)
Poblacion.TamañoCelda= 90
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
    
"""
wb = opyxl.Workbook()    
for generacion in generaciones:
    generacion.cargoDatosExcel(wb)
"""

