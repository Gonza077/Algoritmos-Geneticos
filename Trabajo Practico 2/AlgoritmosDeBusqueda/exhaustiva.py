import copy
class Exhaustiva():
    
    def __init__(self):
        """Tipo de busqueda exhaustiva"""
        pass
    
    def devolverSolucion(self,elementos):
        """Se envia una lista de objetos Elementos y devuelve la mejor solucion de los mismos"""
        self.backtraking(elementos)
        pass
    
    def esSolucion(self,elementos):

        return True        

    def valorSolucion(self,soluciones):
        valor=0
        for elemen in soluciones:
            valor+=elemen.valor
        return 

    def backtracking(self,elementos):
        mejorSolucion = []
        if  self.esSolucion(elementos):
            mejorSolucion.append(elementos)
        else:
            mejorSolucion=None
        for elemen in Expandir(elementos):
            if  EsFactible(elemen):
                ms = self.backtracking(elemen)
                if mejorSolucion==None or  self.valorSolucion(ms) > self.valorSolucion(mejorSolucion):
                    mejorSolucion = copy.deepcopy(ms)
        return  mejorSolucion
