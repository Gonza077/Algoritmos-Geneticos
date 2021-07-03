from tabulate import tabulate

class Mochila:
    
    volMaximo=None
    pesoMaximo=None

    def __init__(self):
        self._elementosMochila=[]
        self._volumenMochila=0
        self._valorMochila=0
        self._pesoMochila=0
        #Aca podriamos definir con un boleano si agregamos elementos, asi el funcionamiento no cambia
    
    def getVolumen(self):
        return self._volumenMochila

    def getValor(self):
        return self._valorMochila
    
    def getPeso(self):
        return self._pesoMochila

    def guardoElemento(self,elemen):
        self._elementosMochila.append(elemen)
        self._volumenMochila+=elemen.getVolumen()
        self._valorMochila+=elemen.getValor()
        self._pesoMochila+=elemen.getPeso()

    def datosMochila(self):
        tuplas=[]
        for elem in self._elementosMochila:
            tuplas.append(elem.datosATupla())
        tuplas.append(["Total",self._volumenMochila,self._valorMochila,self._pesoMochila])
        cabecera=["ID","Volumen","Valor","Peso"]       
        print(tabulate(tuplas, headers=cabecera, stralign='center',tablefmt="github",numalign="center"))


    