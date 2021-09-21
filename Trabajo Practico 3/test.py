from AlgoritmoGenetico.operadoresGeneticos import *
from AlgoritmoGenetico.cromosoma import *

Cromosoma.tCromo = 24
padres = []
for _ in range(0, 2):
    cromo = Cromosoma()
    cromo.instancioGenes()
    print(cromo.getGenes())
    padres.append(cromo)

crosover = CrossOverCiclico(0.99)

hijos = crosover.aplicoCrossover(padres)

print(hijos[0].getGenes())