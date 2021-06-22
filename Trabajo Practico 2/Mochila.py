
class Mochila:
    
    volMaximo=None
    algoritmoDeBusqueda=None

    def __init__(self):
        self._arrElementos=[]
        self._volActual=None
    
    def guardoElemento(self,elemen):
        self._arrElementos.append(elemen)
            
    def devolverElementos(self):
        return self._arrElementos

    def llenarMochila(self,elementos,r,p,b):
        k = len(elementos)
        n = len(p)
        if k == n:
            return elementos,0
        maxFO = 0
        mejorSolucion = elementos[:] + [0]*(n-k)
        for i in range (k,n) :
            if p[i] <= r:
                 = elementos[:] + [0]*(i-k) + [1]
                mejSol , b_ms = self.llenarMochila(nuevaSolucion ,r-p[i] ,p,b)
                if b[i] + b_ms > maxFO :
                    maxFO = b[i] + b_ms
                    mejorSolucion = mejSol
        return mejorSolucion , maxFO

    def mochila_d_bt (x,r,p,b):
        k = len(x)
        n = len(p)
        if k == n:
            return x ,0
        max_b = 0
        mejor_sol = x[:] + [0]*(n-k)
        for i in range (k,n):
            if p[i] <= r:
                x_new = x[:] + [0]*(i-k) + [1]
                ms , b_ms = mochila_d_bt (x_new ,r-p[i] ,p,b)
                if b[i] + b_ms > max_b :
                    max_b = b[i] + b_ms
                    mejor_sol = ms
        return mejor_sol , max_b
    