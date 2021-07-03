from AlgoritmosDeBusqueda.Exhaustiva import *
from AlgoritmosDeBusqueda.Greedy import *
from Elementos import *
from Mochila import *
from Solucion import *

#Definicion de parametros para el caso 1
def AplicarCaso1():
    Mochila.volMaximo=4200
    valores=[20,40,50,36,25,64,54,18,46,28]
    volumenes=[150,325,600,805,430,1200,770,60,930,353]
    elementos=[]
    #Se instancian los elementos
    for i in range(0,10):
        elementos.append(Elemento().setValor(valores[i]).setVolumen(volumenes[i]))
    return elementos

#Definicion de parametros para el caso 2
def AplicarCaso2():
    Mochila.pesoMaximo=3000
    valores=[72,32,60]
    pesos=[1800,600,1200]
    elementos=[]
    #Se instancian los elementos
    for i in range(0,3):
        elementos.append(Elemento().setValor(valores[i]).setPeso(pesos[i]))
    return elementos

#elementos = AplicarCaso1()
elementos= AplicarCaso2()
busqueda = Exhaustiva()
# Crear espacio de soluciones, son 1024 posibilidades
# Cada solucion es es una lista de 10 elementos donde un 0 significa que el elemento no esta en la
# mochila y un 1 que esta, de ahi salen la canWtidad de soluciones 2^10.
busqueda.buscoSolucion(elementos)
# Mostrar información
print()
print("--------------------------------------------")
print("Solución hallada con el algoritmo exhaustivo:")
print("--------------------------------------------")
print(f"Se evaluaron {Exhaustiva.cantSoluciones} soluciones.")
print(f"Se descartaron {busqueda.getSolucionesDescartadas()} soluciones por no cumplir con la restricción de volumen.")
print(f"Se consideraron {busqueda.getSolucionesAceptadas()} soluciones")
print("La mejor solucion encontrada es la siguiente")
busqueda.datosMejorSolucion()

#Se cambia el tipo de busqueda
busqueda=Greedy()
busqueda.buscoSolucion(elementos)
print()
print("--------------------------------------------")
print("Solución hallada con el algoritmo Goloso:")
print("--------------------------------------------")
print("La mejor solucion encontrada es la siguiente")
busqueda.datosMejorSolucion()








