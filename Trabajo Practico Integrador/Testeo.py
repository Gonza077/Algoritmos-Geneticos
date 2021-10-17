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

def prueba_crossover():

    def contar_unos(parque, corte, orden_inverso = False):
        """
            Busca en un aerogenerador los primeros "corte" bits en uno y devuelve la posición desde 0 a 
            la cantidad de genes del parque 99 (10 x 10 en este caso).
           
            El tercer parametro indica el orden en que se recorre la matriz. Por default de principio a fin.             
        """

        contadorPosiciones = 0
        contador = 0

        if orden_inverso:
            contadorPosiciones = 99 # Inicia en 99 porque incluye el cero
            for i in range(9, -1, -1):
                for j in range(9, -1, -1):
                    contadorPosiciones -= 1
                    if parque.terrenoParque[i, j] == 1:
                        contador += 1
                    if contador == corte:
                        return contadorPosiciones
        else:
            for fila in parque.terrenoParque:
                for gen in fila:
                    # print(f'Fila: {fila}')
                    # print(f'Gen: {gen}')
                    # print(f'Posicion 1 1: {parque}')
                    contadorPosiciones += 1
                    if gen == 1:
                        contador += 1
                    if contador == corte:
                        return contadorPosiciones
    
    def copiar_genes(padre, hijo, posicion, orden_inverso = False):
        """
            Revertir las posiciones de la matriz. 
            Tener en cuenta que el paso de variables NO BÁSICAS en python es por referencia, osea, modifica la variable original
        """
        
        def get_index(num):
            """ 
                Pasa un numero entero de 0 a 99 a los indices de una matriz 
                Ejemplo:  0,0 - 0,1 - 0.2 ... 9,7 - 9,8 - 9,9
            """
            from math import floor
            return floor(num / 10), (num - (floor(num / 10)) * 10 )

        if orden_inverso:
            for i in range(posicion, 100):
            # Se podria buscar una manera de cambiar ese 100 por una variable para 
            #     hacer el programa mas adaptable.
                # print(f'I en orden inverso: {i}')
                pos1, pos2 = get_index(i)
                hijo.terrenoParque[pos1, pos2] = padre.terrenoParque[get_index(i)]
        else:
            for i in range(0, posicion + 1):
                # print(f'I en orden: {i}')
                pos1, pos2 = get_index(i)
                hijo.terrenoParque[ pos1, pos2] = padre.terrenoParque[get_index(i)]
            

    ParqueEolico.CantAeroGeneradores=25

    padre = ParqueEolico()
    padre.intancioAerogeneradores()
    madre = ParqueEolico()
    madre.intancioAerogeneradores()

    # Tomo un numero al azar entre 1 y la cantidad de Aerogeneradores
    cantGenesPadre = padre.getCantGenesEnUno()
    cantGenesMadre = madre.getCantGenesEnUno()
    
    maxGenes = 0

    # Tomo el que tiene menos cantidad de genes para que funcione el corte.
    #     Ejemplo: Si un parque tiene 20 genes y sale un random de 22, el programa falla.
    if cantGenesPadre < cantGenesMadre:
        maxGenes = cantGenesPadre
    else:
        maxGenes = cantGenesMadre

    corte = random.randint(1, maxGenes) 
    corte2 = maxGenes - corte

    posicion1 = contar_unos(padre, corte)
    posicion1Inversa = contar_unos(padre, corte2, orden_inverso=True)
    posicion2 = contar_unos(madre, corte)
    posicion2Inversa = contar_unos(madre, corte2, orden_inverso=True)
    #Tomo los primeros 'n' bits en 1 del padre y los paso al hijo, lo mismo con la madre y el segundo hijo

    print(' --------------------- Datos del crossover')
    print(f'El corte es en los primeros {corte} genes en 1')
    print(f'El corte dos es {corte2} ')
    print(f'En padre los primeros {corte} genes estan en las primeras : {posicion1} posiciones')
    print(f'En madre los primeros {corte} genes estan en las primeras : {posicion2} posiciones')
    print(f'En padre inverso los  {corte2} genes estan desde la posición : {posicion1Inversa} hasta la 99')
    print(f'En madre inversa los  {corte2} genes estan desde la posición : {posicion2Inversa} hasta la 99')

    hijo = ParqueEolico()
    hija = ParqueEolico()

    if posicion1 >= posicion2Inversa:
        # Si es mayor, copio hasta la posicion 1 y luego relleno con los demas genes de la madre
        #     en este caso, el parque va a tener menos de 25 aerogeneradores
        copiar_genes(padre, hijo, posicion1)
        copiar_genes(madre, hijo, posicion1 + 1, orden_inverso=True)
    else:
        copiar_genes(padre, hijo, posicion1)
        copiar_genes(madre, hijo, posicion2Inversa, orden_inverso=True)

    if posicion2 >= posicion1Inversa:
        copiar_genes(madre, hija, posicion2)
        copiar_genes(padre, hija, posicion2 + 1, orden_inverso=True)
    else:
        copiar_genes(madre, hija, posicion2)
        copiar_genes(padre, hija, posicion1Inversa, orden_inverso=True)

    padre.datosParque()
    madre.datosParque()
    hijo.datosParque()
    hija.datosParque()

prueba_crossover()

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

# arr=np.array([[0]*10]*10)
# contador=0
# while(contador<25):
#     contador+=1
#     fRandom=random.randrange(len(arr))
#     cRandom=random.randrange(len(arr[0]))
#     arr[fRandom][cRandom]=1

# print()

# for fila in arr:
#     aeroFilas=np.where(fila==1)[0]#Dado que devuelve una tupla con un arreglo y el tipo de dato, solo tomo el arreglo
#     #existeEstela() -> si existen dos generadores en la misma fila devuelve true
#     if len(aeroFilas) >=2:
#         #calculoDistancia(aeroFilas) -> Se haria un metodo con los indices de la fila, despues se calcula el viento
#         for i in range(0,len(aeroFilas)-1):
#             print(f"La distancia entre AeroGenerador N° {aeroFilas[i] +1} y {aeroFilas[i+1] +1} es {aeroFilas[i+1]-aeroFilas[i]} de la fila \t {fila}")

# print()
# for fila in arr:
#     print(fila)

# velViento=17
# velocidadesViento=[[0, 0],[1, 0],[2, 0],[3, 10],[4, 46],[5, 170],[6, 355],[7, 580],[8, 874],[9, 1219],[10, 1544],[11, 1740],[12, 1789],[13, 1800],[14, 1800],[15, 1800],[16, 1800],[17, 1800],[18, 1800],[19, 1800],[20, 1800],[21, 1800],[22, 1800],[23, 1800],[24, 1800],[25, 1800],[26, 0]]
# for i in range(len(velocidadesViento)-1):
#     if velocidadesViento[i][0]<=velViento and velocidadesViento[i+1][0]>velViento:
#         print(f"La potencia asociada esa velocidad es {velocidadesViento[i][1]}")
#         break