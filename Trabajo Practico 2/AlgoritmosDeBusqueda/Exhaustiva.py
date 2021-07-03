from AlgoritmosDeBusqueda.Busqueda import *
from Mochila import *

class Exhaustiva(Busqueda):

    cantSoluciones=None
    
    def __init__(self):
        super().__init__()
        self._arrSolucionesDescartadas=[]
        self._arrSolucionesAceptadas=[]
        
    def buscoSolucion(self,elementos):
        # Crear espacio de soluciones, son 1024 posibilidades
        # Cada solucion es es una lista de 10 elementos donde un 0 significa que el elemento no esta en la
        # mochila y un 1 que esta, de ahi salen la cantidad de soluciones 2^10.
        Exhaustiva.cantSoluciones = 2 ** len(elementos) #Variable de clase, para saber cuantas soluciones tendriamos
        for i in range(0, Exhaustiva.cantSoluciones):
            mochila= Mochila()
            lista_binaria = self.entero_a_binario(i,len(elementos))
            for i in range (0,len(lista_binaria)):
                if(lista_binaria[i] == 1):
                    #Se guarda los elementos en la mochila
                    mochila.guardoElemento(elementos[i])
            #VER SI TODO ESTO SE PUEDE FILTRAR
            if(Mochila.volMaximo!=None):
                if(mochila.getVolumen() > Mochila.volMaximo):
                    self._arrSolucionesDescartadas.append(mochila)
                else:
                    self._arrSolucionesAceptadas.append(mochila)
            elif(Mochila.pesoMaximo!=None):
                if(mochila.getPeso() > Mochila.pesoMaximo):
                    self._arrSolucionesDescartadas.append(mochila)
                else:
                    self._arrSolucionesAceptadas.append(mochila)
        self.buscoMejorSolucion()
    
    def buscoMejorSolucion(self):
        self._mejorSolucion = self._arrSolucionesAceptadas[0]
        for mochilaActual in self._arrSolucionesAceptadas:
            if(mochilaActual.getValor() > self._mejorSolucion.getValor()):
                self._mejorSolucion = mochilaActual
        return self._mejorSolucion

    def getSolucionesDescartadas(self):
        return len(self._arrSolucionesDescartadas)

    def getSolucionesAceptadas(self):
        return len(self._arrSolucionesAceptadas)
    
    def datosMejorSolucion(self):
        return self._mejorSolucion.datosMochila()