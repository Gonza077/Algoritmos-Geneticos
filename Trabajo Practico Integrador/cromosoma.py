import random as rnd

class Cromosoma(object):
    
    IDCromosoma=1
    Dominio = None
    tCromo=None

    #Atributos
    def __init__(self):         
        self.funcFitness=0
        self.funcObjetivo=0
        self.valorDecimal=0
        self.arrGenes=[]
    
    #Operadores logicos, ya que Python no permite comparar obejtos 
    def __gt__(self, cromosoma):
        return self.valorDecimal > cromosoma.valorDecimal

    def __lt__(self, cromosoma):
        return self.valorDecimal < cromosoma.valorDecimal

    def __ge__(self, cromosoma):
        return self.valorDecimal >= cromosoma.valorDecimal

    def __le__(self, cromosoma):
        return self.valorDecimal <= cromosoma.valorDecimal

    def __eq__(self, cromosoma):
        return self.valorDecimal == cromosoma.valorDecimal

    def __ne__(self, cromosoma):
        return self.valorDecimal != cromosoma.valorDecimal

    #Metodos de instancia
    def calculoDatosCromosoma(self):
        """Se calcula el valor de cada cromosoma"""     
        cadena = "".join([ str(gen) for gen in self.arrGenes])  #Hace la conversion del arreglo a una cadena por ejemplo[1,0,1] a '101'
        self.valorDecimal = int(cadena, 2) #Se transofrma la cadena de genes en un valor en decimal
        self.funcObjetivo = None #Dominio se define en el cuerpo principal      

    def calculoFitness(self,sumaPoblacion): 
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada cromosoma"""
        self.funcFitness = self.funcObjetivo / sumaPoblacion

    def mutoGen(self):
        numRandom=rnd.randint(0,Cromosoma.tCromo-1)
        if(self.arrGenes[numRandom]==0):
            self.arrGenes[numRandom]=1
        else:
            self.arrGenes[numRandom]=0

    def instancioGenes(self):
        for _ in range(0,Cromosoma.tCromo):
            self.arrGenes.append(rnd.randint(0, 1))
    
    def insertoGen(self,gen):
        """Se envia el gen a insertar en el arreglo del cromosoma"""
        self.arrGenes.append(gen)

    def datosCromosoma(self):
        cadena = "".join([ str(gen) for gen in self.arrGenes])
        print(f"Func Fitness: {self.funcFitness}, Valor decimal: {self.valorDecimal}, Func Objetivo: {self.funcObjetivo}, Genes {cadena}")
 
    def ATupla(self):
        cadena="".join([str(gen) for gen in self.arrGenes])
        return [self.funcObjetivo,self.funcFitness,self.valorDecimal,cadena]