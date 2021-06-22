from Exhaustiva import *
from Elementos import *
from Mochila import *

#Definicion de parametros 
Mochila.volMaximo=4200
elementos=[]
valores=[20,40,50,36,25,64,54,18,46,28]
volumenes=[150,325,600,805,430,1200,770,60,930,353]

#Se instancian los elementos
for i in range(0,10):
    elementos.append(Elemento().setValor(valores[i]).setVolumen(volumenes[i]))

mochila = Mochila()
busqueda= Exhaustiva()
busqueda.aplicoBusqueda(elementos,mochila)
#Realizar las busquedas a partir de aca

mochila.datosMochila()

