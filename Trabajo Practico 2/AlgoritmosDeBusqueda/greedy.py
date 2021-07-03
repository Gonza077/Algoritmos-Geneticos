from AlgoritmosDeBusqueda.Busqueda import *
from Elementos import *
from Mochila import *

class Greedy(Busqueda):

    def __init__(self):
        super().__init__()

    def buscoSolucion(self,elementos):
        ''' Esta función devuelve el proximo mejor elemento para agregar a la mochila
            O Falso en caso de que no haya mas elementos para agregar.'''
        mochila= Mochila()
        # Ordeno los elementos segun su valor/volumen
        if (Mochila.volMaximo!=None):
            elementos.sort(reverse = True, key=lambda x: x.getValorSobreVolumen())
        elif(Mochila.pesoMaximo!=None):
            elementos.sort(reverse = True, key=lambda x: x.getValorSobrePeso())
        # Busco cual de los elementos que quedan disponibles pueden agregarse a la mochile y devuelvo
        #    el primero que encuentra. En caso de que no se puede agregar ninguno devuelve False
        for elemen in elementos:
            if Mochila.volMaximo!=None:
                if(mochila.getVolumen() + elemen.getVolumen() <= Mochila.volMaximo ):
                    mochila.guardoElemento(elemen)
                else:
                    break
            elif Mochila.pesoMaximo!=None:
                if(mochila.getPeso() + elemen.getPeso() <= Mochila.pesoMaximo ):
                    mochila.guardoElemento(elemen)
                else:
                    break

        self._mejorSolucion = mochila

    def datosMejorSolucion(self):
        return self._mejorSolucion.datosMochila()