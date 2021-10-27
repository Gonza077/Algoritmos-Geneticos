import random as rnd
from Cromosoma import Cromosoma

class Ruleta():

    def aplicarSeleccion(self,poblacionAnterior,cantCromosomasPobla):
        ruleta=[0]
        valor=0     
        paresPadres=[]         
        for cromosoma in poblacionAnterior.getCromosomas():       
            valor+=cromosoma.getFuncFitness()
            ruleta.append(valor)
        for _ in range ((len(poblacionAnterior.getCromosomas())- cantCromosomasPobla) // 2):
                pares=[]
                while ( len(pares) < 2 ): #Se debe armar el par, esto garantiza que siempre se forme
                    numAleatorio = rnd.random()     
                    for j in range(len(poblacionAnterior.getCromosomas())-1):  
                        if (numAleatorio >= ruleta[j] and numAleatorio < ruleta[j+1]):
                            pares.append(poblacionAnterior._arrCromosomas[j])
                paresPadres.append(pares)          
        return paresPadres

class Torneo():

    def aplicarSeleccion(self, poblacionAnterior,cantCromosomasPobla):
        paresPadres = []
        for _ in range ((len(poblacionAnterior.getCromosomas())- cantCromosomasPobla) // 2):
            pares = []
            for _ in range(0, 2):
                # Elijo aleatoriamente 2 cromosomas
                crom1 = rnd.choice(poblacionAnterior.getCromosomas())
                crom2 = rnd.choice(poblacionAnterior.getCromosomas())
                if crom1 >= crom2: # Elijo el mejor de ambos
                    pares.append(crom1)
                else:
                    pares.append(crom2)
            paresPadres.append(pares)
        return paresPadres

class CrossOverUnPunto():

    def __init__(self,probCross,num):
        self.probCrossover=probCross
        self.tipoDeCruce=num

    def aplicoCrossover(self,padres):
        nuevosCromosomas=[]
        for par in padres:  #Padres viene de a pares
            padre=par[0] 
            madre=par[1]
            if(rnd.random() <= self.probCrossover):      
                hijo1=None
                hijo2=None
                if self.tipoDeCruce==0:
                    hijo1,hijo2 = self.crucePorFila(padre,madre)
                else:
                    hijo1,hijo2 = self.crucePorColumna(padre,madre)                                                 
                #Se guarda cada cromosoma en la nueva poblacion
                hijo1.limitarAerogeneradores()
                hijo2.limitarAerogeneradores()
                nuevosCromosomas.append(hijo1)
                nuevosCromosomas.append(hijo2)          
            else:
                #Se guarda cada cromosoma en la nueva poblacion
                nuevosCromosomas.append(padre)
                nuevosCromosomas.append(madre)       
        return nuevosCromosomas

    def crucePorFila(self,padre,madre):
        hijo1=Cromosoma()
        hijo2=Cromosoma()
        posicionCorte=rnd.randint(0,Cromosoma.tCromo-1)                  
        #Tipo de Cruce por fila         
        for fila in range(0,posicionCorte):
            hijo1.insertoGenes(padre._genes[fila],fila)
            hijo2.insertoGenes(madre._genes[fila],fila)
        for fila in range(posicionCorte,Cromosoma.tCromo):
            hijo1.insertoGenes(madre._genes[fila],fila)
            hijo2.insertoGenes(padre._genes[fila],fila) 
        return hijo1,hijo2
    
    def crucePorColumna(self,padre,madre):
        hijo1=Cromosoma()
        hijo2=Cromosoma()
        posicionCorte=rnd.randint(0,Cromosoma.tCromo-1)      
        for fila in range(Cromosoma.tCromo):
            for col in range(0,posicionCorte):
                #Habria que pensar si es posible hacer que la fila y col se saquen por defecto
                hijo1.insertoGen(padre._genes[fila][col],fila,col)
                hijo2.insertoGen(madre._genes[fila][col],fila,col)
                #Posteriormente se intercambian los genes de cada padre en los hijos, luego de la posicion del corte
            for col in range(posicionCorte,Cromosoma.tCromo):
                hijo1.insertoGen(madre._genes[fila][col],fila,col)
                hijo2.insertoGen(padre._genes[fila][col],fila,col)  
        return hijo1,hijo2

class MutacionInvertida():

    def __init__(self,probMuta):
        self.probMutacion=probMuta

    def aplicoMutacion(self,cromosomas):
        for cromosoma in cromosomas:          
            if(rnd.random() <= self.probMutacion):   
                cromosoma.MutacionInvertida()
                cromosoma.limitarAerogeneradores()

class MutacionSwap():

    def __init__(self,probMuta):
        self.probMutacion=probMuta

    def aplicoMutacion(self,cromosomas):
        for cromosoma in cromosomas:          
            if(rnd.random() <= self.probMutacion):   
                cromosoma.MutacionSwap()




