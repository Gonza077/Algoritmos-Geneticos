from poblacion import Poblacion
from cromosoma import Cromosoma
import generacion

Cromosoma.tCromo=10
Cromosoma.Dominio=((2**10)-1)
Poblacion.tPobla=10
Poblacion.probCrossover=0.75
Poblacion.probMutacion=0.05

pobla=Poblacion()

pobla.instancioCromosomas()

for cromosoma in pobla.arrCromosomas:
    print(cromosoma.arrGenes)
pobla.calculoDatosPoblacion()
pares = pobla.aplicoSeleccionRuleta(pobla)

for x in pares:
    print(x)
pobla.creoNuevaPoblacion(pobla)

print("---------------------------------------")
for cromosoma in pobla.arrCromosomas:
    print(cromosoma.arrGenes)
pobla.calculoDatosPoblacion()
pares = pobla.aplicoSeleccionRuleta(pobla)

for x in pares:
    print(x)
par1=pares[0]
print(par1[0])
print(par1[1])