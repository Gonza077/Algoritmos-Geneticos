import CiudadesDAO
from AlgoritmoGenetico.Poblacion import Poblacion
from AlgoritmoGenetico.Generacion import Generacion
from AlgoritmoGenetico.OperadoresGeneticos import *

# cromo = Cromosoma()

# cromo.mostrarGenes()
# cromo.mutoGen()
# cromo.mostrarGenes()

def prueba_getCiudadById():

    CiudadesDAO.cargarCiudades()
    # for c in ciudades.retornarCiudades():
    #     print(c.getNombre())

    c = CiudadesDAO.getCiudadById(1)
    c2 = CiudadesDAO.getCiudadById(24)
    print(f"La ciudad es {c.getNombre()}")
    print(f"La ciudad es {c2.getNombre()}")

    c3 = CiudadesDAO.getCiudadById(24231)

def probar_genetico(numCromosomas, cantCiclos, probCrossover, probMutacion):
    Poblacion.tPobla = numCromosomas
    Poblacion.tipoSeleccion=Ruleta()
    Poblacion.tipoCrossover=CrossOverCiclico(probCrossover)
    Poblacion.tipoMutacion=Mutacion(probMutacion)
    generacion=Generacion()
    for _ in range(cantCiclos):        
        generacion.creoGeneracion()
        
    generacion.datosGeneracion()

# probar_genetico(200, 50, 0.75, 0.05)
prueba_getCiudadById()


