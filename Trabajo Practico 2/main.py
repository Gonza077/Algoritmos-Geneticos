from AlgoritmosDeBusqueda import *
from Elementos import *
from Mochila import *
from AlgoritmosDeBusqueda import *

#Definicion de parametros 
Mochila.volMaximo=4200
elementos=[]
valores=[20,40,50,36,25,64,54,18,46,28]
volumenes=[150,325,600,805,430,1200,70,60,930,353]
funcObjetivo=0

#Instanciacion de los elementos
mochila = Mochila()
#busqueda= Exhaustiva()

#Se crean los elementos sobre los cuales se van a realizar las busquedas
for i in range(0,10):
    elementos.append(Elemento().setValor(valores[i]).setVolumen(volumenes[i]))

#Realizar las busquedas a partir de aca
#
