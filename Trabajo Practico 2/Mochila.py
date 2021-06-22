
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

    def llenarMochila(self,elemen):
        pass


