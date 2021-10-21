from enum import Enum
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
        t = 2
        paresPadres = []
        for _ in range ((len(poblacionAnterior.getCromosomas())- cantCromosomasPobla) // 2):
            pares = []
            for _ in range(0, t):
                # Elijo aleatoriamente 2 cromosomas
                crom1 = rnd.choice(poblacionAnterior._arrCromosomas)
                crom2 = rnd.choice(poblacionAnterior._arrCromosomas)
                if crom1 >= crom2: # Elijo el mejor de ambos
                    pares.append(crom1)
                else:
                    pares.append(crom2)
            paresPadres.append(pares)
        return paresPadres

class CrossOverUnPunto():

    def __init__(self,probCross):
        self.probCrossover=probCross

    def aplicoCrossover(self,padres):
        nuevosCromosomas=[]
        for par in padres:  #Padres viene de a pares
            padre=par[0] 
            madre=par[1]
            if(rnd.random() <= self.probCrossover):      
                hijo1=Cromosoma()
                hijo2=Cromosoma()
                posicionCorte=rnd.randint(0,Cromosoma.tCromo-1)   
                   
                #Tipo de Cruce por fila y columna        
                for fila in range(Cromosoma.tCromo):
                    for col in range(0,posicionCorte):
                        #Habria que pensar si es posible hacer que la fila y col se saquen por defecto
                        hijo1.insertoGen(padre._genes[fila][col],fila,col)
                        hijo2.insertoGen(madre._genes[fila][col],fila,col)
                        #Posteriormente se intercambian los genes de cada padre en los hijos, luego de la posicion del corte
                    for col in range(posicionCorte,Cromosoma.tCromo):
                        hijo1.insertoGen(madre._genes[fila][col],fila,col)
                        hijo2.insertoGen(padre._genes[fila][col],fila,col)   
                      
                #Se guarda cada cromosoma en la nueva poblacion
                nuevosCromosomas.append(hijo1)
                nuevosCromosomas.append(hijo2)          
            else:
                #Se guarda cada cromosoma en la nueva poblacion
                nuevosCromosomas.append(padre)
                nuevosCromosomas.append(madre)       
        return nuevosCromosomas

    def aplicoCrossoverNico(self,padres):
        """ 
            Recibe un arreglo con arreglos de dos elementos: [[p,m], [p2, m2] ... ], donde cada uno es un padre.
            Luego, en función de la probabilidad de crossover, puede aplicarlo o no.
        """

        def contar_unos(parque, corte, orden_inverso = False):
            """
                Busca en un aerogenerador los primeros "corte" bits en uno y devuelve la posición desde 0 a 
                la cantidad de genes del parque 99 (10 x 10 en este caso).
            
                El tercer parametro indica el orden en que se recorre la matriz. Por default de principio a fin.             
            """

            contadorPosiciones = 0
            contador = 0

            if orden_inverso:
                contadorPosiciones = 99 # Inicia en 99 porque incluye el cero
                for i in range(9, -1, -1):
                    for j in range(9, -1, -1):
                        contadorPosiciones -= 1
                        if parque._genes[i, j] == 1:
                            contador += 1
                        if contador == corte:
                            return contadorPosiciones
            else:
                for fila in parque._genes:
                    for gen in fila:
                        # print(f'Fila: {fila}')
                        # print(f'Gen: {gen}')
                        # print(f'Posicion 1 1: {parque}')
                        contadorPosiciones += 1
                        if gen == 1:
                            contador += 1
                        if contador == corte:
                            return contadorPosiciones
        
        def copiar_genes(padre, hijo, posicion, orden_inverso = False):
            """
                Revertir las posiciones de la matriz. 
                Tener en cuenta que el paso de variables NO BÁSICAS en python es por referencia, osea, modifica la variable original
            """
            
            def get_index(num):
                """ 
                    Pasa un numero entero de 0 a 99 a los indices de una matriz 
                    Ejemplo:  0,0 - 0,1 - 0.2 ... 9,7 - 9,8 - 9,9
                """
                from math import floor
                return floor(num / 10), (num - (floor(num / 10)) * 10 )

            if orden_inverso:
                for i in range(posicion, 100):
                # Se podria buscar una manera de cambiar ese 100 por una variable para 
                #     hacer el programa mas adaptable.
                    # print(f'I en orden inverso: {i}')
                    pos1, pos2 = get_index(i)
                    hijo._genes[pos1, pos2] = padre._genes[get_index(i)]
            else:
                for i in range(0, posicion + 1):
                    # print(f'I en orden: {i}')
                    pos1, pos2 = get_index(i)
                    hijo._genes[ pos1, pos2] = padre._genes[get_index(i)]
                
        nuevosParques=[]

        for par in padres:  #Padres viene de a pares
            padre=par[0] 
            madre=par[1]
            if(rnd.random() <= self.probCrossover):      
                hijo = Cromosoma()
                hija = Cromosoma()

                # Tomo un numero al azar entre 1 y la cantidad de Aerogeneradores
                cantGenesPadre = padre.getCantGenesEnUno()
                cantGenesMadre = madre.getCantGenesEnUno()
                
                maxGenes = 0

                # Tomo el que tiene menos cantidad de genes para que funcione el corte.
                #     Ejemplo: Si un parque tiene 20 genes y sale un random de 22, el programa falla.
                if cantGenesPadre < cantGenesMadre:
                    maxGenes = cantGenesPadre
                else:
                    maxGenes = cantGenesMadre

                corte = rnd.randint(1, maxGenes) 
                corte2 = maxGenes - corte

                #Tomo los primeros 'n' bits en 1 del padre y los paso al hijo, lo mismo con la madre y el segundo hijo
                posicion1 = contar_unos(padre, corte)
                posicion1Inversa = contar_unos(padre, corte2, orden_inverso=True)
                posicion2 = contar_unos(madre, corte)
                posicion2Inversa = contar_unos(madre, corte2, orden_inverso=True)

                # print(' --------------------- Datos del crossover')
                # print(f'El corte es en los primeros {corte} genes en 1')
                # print(f'El corte dos es {corte2} ')
                # print(f'En padre los primeros {corte} genes estan en las primeras : {posicion1} posiciones')
                # print(f'En madre los primeros {corte} genes estan en las primeras : {posicion2} posiciones')
                # print(f'En padre inverso los  {corte2} genes estan desde la posición : {posicion1Inversa} hasta la 99')
                # print(f'En madre inversa los  {corte2} genes estan desde la posición : {posicion2Inversa} hasta la 99')

                if posicion1 >= posicion2Inversa:
                    # Si es mayor, copio hasta la posicion 1 y luego relleno con los demas genes de la madre
                    #     en este caso, el parque va a tener menos de 25 aerogeneradores
                    copiar_genes(padre, hijo, posicion1)
                    copiar_genes(madre, hijo, posicion1 + 1, orden_inverso=True)
                else:
                    copiar_genes(padre, hijo, posicion1)
                    copiar_genes(madre, hijo, posicion2Inversa, orden_inverso=True)

                if posicion2 >= posicion1Inversa:
                    copiar_genes(madre, hija, posicion2)
                    copiar_genes(padre, hija, posicion2 + 1, orden_inverso=True)
                else:
                    copiar_genes(madre, hija, posicion2)
                    copiar_genes(padre, hija, posicion1Inversa, orden_inverso=True)

                nuevosParques.append(hija)
                nuevosParques.append(hijo)
            else:
                #Se guarda cada cromosoma en la nueva poblacion
                nuevosParques.append(padre)
                nuevosParques.append(madre)  
        
        return nuevosParques

        # padre.datosParque()
        # madre.datosParque()
        # hijo.datosParque()
        # hija.datosParque()
        
        # nuevosCromosomas=[]
        # for par in padres:  #Padres viene de a pares
        #     padre=par[0] 
        #     madre=par[1]
        #     if(rnd.random() <= self.probCrossover):      
        #         hijo1=cr.Cromosoma()
        #         hijo2=cr.Cromosoma()
        #         posicionCorte=rnd.randint(0,cr.Cromosoma.tCromo-1)
        #         #Se instancia los primeros N genes de cada padre hasta la posicion de corte en cada hijo
        #         for j in range(0,posicionCorte):
        #             hijo1.insertoGen(padre.arrGenes[j])
        #             hijo2.insertoGen(madre.arrGenes[j])
        #             #Posteriormente se intercambian los genes de cada padre en los hijos, luego de la posicion del corte
        #         for k in range(posicionCorte,cr.Cromosoma.tCromo):
        #             hijo1.insertoGen(madre.arrGenes[k])
        #             hijo2.insertoGen(padre.arrGenes[k])             
        #         #Se guarda cada cromosoma en la nueva poblacion
        #         nuevosCromosomas.append(hijo1)
        #         nuevosCromosomas.append(hijo2)          
        #     else:
        #         #Se guarda cada cromosoma en la nueva poblacion
        #         nuevosCromosomas.append(padre)
        #         nuevosCromosomas.append(madre)       
        # return nuevosCromosomas

class MutacionInvertida():

    def __init__(self,probMuta):
        self.probMutacion=probMuta

    def aplicoMutacion(self,cromosomas):
        for cromosoma in cromosomas:          
            if(rnd.random() <= self.probMutacion):   
                cromosoma.mutoGen()




