from tabulate import tabulate

class Mochila:
    
    volMaximo=None

    def __init__(self):
        self._arrElementos=[]
        self._volActual=0
        self._valor=0
    
    def getVolumenActual(self):
        return self._volActual

    def getValorActual(self):
        return self._valor

    def guardoElemento(self,elemen):
        self._arrElementos.append(elemen)
        self._volActual+=elemen.getVolumen()
            
    def datosMochila(self):
        tuplas=[]
        for elem in self._arrElementos:
            self._valor+=elem.getValor()
            tuplas.append(elem.datosATupla())
        tuplas.append(["Total",self._volActual,self._valor])
        cabecera=["ID","Volumen","Valor"]       
        print(tabulate(tuplas, headers=cabecera, stralign='center',tablefmt="github",numalign="center"))


    