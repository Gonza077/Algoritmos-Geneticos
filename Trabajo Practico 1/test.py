from poblacion import Poblacion
from cromosoma import Cromosoma
import copy
import generacion

Cromosoma.tCromo=10
Cromosoma.Dominio=((2**10)-1)
Poblacion.tPobla=10
Poblacion.probCrossover=0.75
Poblacion.probMutacion=0.05

cr=Cromosoma()
cr2=Cromosoma()
cr2.valorDecimal=35
cr1=copy.deepcopy(cr)

cr1.valorDecimal=257

lista=[cr,cr2,cr1]

lista.sort(reverse=True)

