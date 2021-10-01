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

# Se podría meter todo esto en una función
def menuConsola():
    print(f"--------------------------------------------------------")
    print(f"Que desea hacer:")
    print(f"1- Buscar ruta mínima desde una ciudad:")
    print(f"2- Buscar ruta mínima total usando una Heuristica")
    print(f"3- Buscar ruta mínima total usando un Algoritmo Genético")
    print(f"--------------------------------------------------------")

    opc1 = int(input('Ingrese su opción: '))

    if opc1 == 1:
        print(f"Ingrese su ciudad de origen:")
        ciudad_origen = input()
        ruta = buscarRuta(ciudad_origen)
        print(f"La ruta encontrada es:")
        print(f'{list(map(lambda x:x.getNombre(), ruta))}')
        # for c in ruta:
        #     print(f"Ciudad: {c.getNombre()} - Distancia {c.getDistancia()}")
        ciudades_filtradas = list(filter(condicionFiltro, ruta))
        # print(f"Lista de ciudades filtradas: {ciudades_filtradas}")
        arreglo_distancias = list(map(lambda x:x.getDistancia(), ciudades_filtradas))
        # print(f"Lista de ciudades mapeadas: {arreglo_distancias}")
        print(f"Total de ciudades: {len(arreglo_distancias)}")
        print(f"La distancia total es: {np.sum(arreglo_distancias)}")

    if opc1 == 2:
        ruta = buscarRutaMinima()
        print("La ruta minima encontrada es:")
        print(f'{list(map(lambda x:x.getNombre(), ruta))}')
        ciudades_filtradas = list(filter(condicionFiltro, ruta))
        # print(f"Lista de ciudades filtradas: {ciudades_filtradas}")
        arreglo_distancias = list(map(lambda x:x.getDistancia(), ciudades_filtradas))
        # print(f"Lista de ciudades mapeadas: {arreglo_distancias}")
        print(f"Total de ciudades: {len(arreglo_distancias)}")
        print(f"La distancia total es: {np.sum(arreglo_distancias)}")

    if opc1 == 3:
        #Se definen todos los parametros del AG
        Corridas=[200]   
        generaciones=[]
        Cromosoma.tCromo=24
        Poblacion.tPobla=50
        #Poblacion.tipoSeleccion=operadoresGeneticos.Ruleta()
        #Poblacion.tipoCrossover=operadoresGeneticos.CrossOverUnPunto(0.75)
        #Poblacion.tipoMutacion=operadoresGeneticos.MutacionInvertida(0.05)
        Poblacion.elitismo=False 
        #Se genera cada generacion
        for x in Corridas:
            generacion=Generacion()
            for _ in range(x):        
                generacion.creoGeneracion()
            Poblacion.reseteoIDPoblacion() #Se vuelve a setear el ID a 1
            generaciones.append(generacion)
        print("\n")
        for generacion in generaciones:
            generacion.datosGeneracion()
            print("\n")