import copy
from Elementos import *
from Mochila import *

class Exhaustiva():
    
    def aplicoBusqueda(self,elementos,mochila):
        for elem in elementos:
            #Se verifica que la mochila tenga espacio suficiente para el objeto
            if  (mochila.getVolumenActual() + elem.getVolumen() <= mochila.volMaximo):
                #Se agrega el elemento a la mochila
                mochila.guardoElemento(copy.deepcopy(elem))

    #Este formato lo vi en internet, pero no se como apliarlo con respecto a la recursividad
    def mochila_d_bt (x,r,p,b) :
        k = len(x)
        n = len(p)
        if k == n:
         return x , 0
        max_b = 0
        mejor_sol = x[:] + [0]*(n-k)
        for i in range (k,n) :
            if p[i] <= r:
                x_new = x[:] + [0]*(i-k) + [1]
                ms , b_ms = mochila_d_bt (x_new ,r-p[i] ,p,b)
                if b[i] + b_ms > max_b :
                    max_b = b[i] + b_ms
                    mejor_sol = ms
        return mejor_sol , max_b