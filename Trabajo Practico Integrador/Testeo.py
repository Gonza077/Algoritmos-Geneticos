import random
import numpy as np
from Generacion import *
from Poblacion import *
from ParqueEolico import *
#from OperadoresGeneticos import *

Corridas=[1]   
generaciones=[]
#Parametros del Parque
ParqueEolico.cantAerogeneradores=25
#Parametros de la Poblacion
Poblacion.TamañoCelda=180  #Distancia Minima de 4*R, donde R es 45 m
Poblacion.CantParques=5

"""
#Testeo de la construccion de la matriz
for x in Corridas:
    generacion=Generacion()
    for _ in range(x):        
        generacion.creoGeneracion()
    Poblacion.reseteoIDPoblacion() #Metodo de clase que vuelve el ID a 1
    generaciones.append(generacion)

for gene in generaciones:
    gene.datosGeneracion()

"""

arr=np.array([[0]*10]*10)
contador=0
while(contador<25):
    contador+=1
    fRandom=random.randrange(len(arr))
    cRandom=random.randrange(len(arr[0]))
    arr[fRandom][cRandom]=1

print()

for fila in arr:
    aeroFilas=np.where(fila==1)[0]#Dado que devuelve una tupla con un arreglo y el tipo de dato, solo tomo el arreglo
    #existeEstela() -> si existen dos generadores en la misma fila devuelve true
    if len(aeroFilas) >=2:
        #calculoDistancia(aeroFilas) -> Se haria un metodo con los indices de la fila, despues se calcula el viento
        for i in range(0,len(aeroFilas)-1):
            print(f"La distancia entre AeroGenerador N° {aeroFilas[i] +1} y {aeroFilas[i+1] +1} es {aeroFilas[i+1]-aeroFilas[i]} de la fila \t {fila}")

print()
for fila in arr:
    print(fila)

velViento=17
velocidadesViento=[[0, 0],[1, 0],[2, 0],[3, 10],[4, 46],[5, 170],[6, 355],[7, 580],[8, 874],[9, 1219],[10, 1544],[11, 1740],[12, 1789],[13, 1800],[14, 1800],[15, 1800],[16, 1800],[17, 1800],[18, 1800],[19, 1800],[20, 1800],[21, 1800],[22, 1800],[23, 1800],[24, 1800],[25, 1800],[26, 0]]
for i in range(len(velocidadesViento)-1):
    if velocidadesViento[i][0]<=velViento and velocidadesViento[i+1][0]>velViento:
        print(f"La potencia asociada esa velocidad es {velocidadesViento[i][1]}")
        break