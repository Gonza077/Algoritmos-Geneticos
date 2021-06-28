class Solucion:

    lista_binaria = []

    def __init__(self, lista_binaria, elementos):
        self.lista_binaria = lista_binaria
        self.elementos = elementos

    def getVolumen(self):
        volumen = 0
        for i in range(0, len(self.lista_binaria) - 1):
            if(self.lista_binaria[i] == 1):
                volumen += self.elementos[i].getVolumen()
        return volumen

    def getValor(self):
        valor = 0
        for i in range(0, len(self.lista_binaria) - 1):
            if(self.lista_binaria[i] == 1):
                valor += self.elementos[i].getValor()
        return valor

    def getElementos(self):
        mis_elementos = []
        for i in range(0, len(self.lista_binaria) - 1):
            if(self.lista_binaria[i] == 1):
                mis_elementos.append(i)
        return mis_elementos
