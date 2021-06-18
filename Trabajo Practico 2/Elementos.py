class Elemento():

    ID=1

    def __init__(self):
        self._ID=Elemento.ID
        self._valor=None
        self._volumen=None
        Elemento.ID+=1

    def setValor(self,val):
        self._valor=val
        return self
    
    def setVolumen(self,val):
        self._volumen=val
        return self

    def getValor(self):
        return self._valor
    
    def getVolumen(self):
        return self._volumen

    def datos(self):
        print(f"ID {self._ID} -> Volumen {self._volumen} - Valor {self._valor} ")



    


