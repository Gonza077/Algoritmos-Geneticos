class Elemento():

    ID=1

    def __init__(self):
        self._ID=Elemento.ID
        self._valor=0
        self._volumen=0
        self._peso=0
        Elemento.ID+=1

    def setValor(self,val):
        self._valor=val
        return self
    
    def setVolumen(self,val):
        self._volumen=val
        return self
    
    def setPeso(self,val):
        self._peso=val
        return self

    def getValor(self):
        return self._valor
    
    def getVolumen(self):
        return self._volumen
    
    def getPeso(self):
        return self._peso
    
    def getValorSobreVolumen(self):
        return self._valor / self._volumen
    
    def getValorSobrePeso(self):
        return self._valor / self._peso

    def datosATupla(self):
        return [self._ID,self._volumen,self._valor,self._peso]



    


