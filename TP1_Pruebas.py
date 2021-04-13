import TP1 as tp

def pruebaAplicoCorte():
    c1 = tp.Cromosoma()
    c2 = tp.Cromosoma()

    p = tp.Poblacion()
    h1 = p.aplicoCorte(c1,c2)

    print("Padres")
    print(c1.arrGenes)
    print(c2.arrGenes)
    print("Hijos")
    for i in h1:
        print(i.arrGenes)

def pruebaSeleccionoPadres():
    p = tp.Poblacion()
    p.calculoValorPoblacion()

    padres = p.seleccionoPadres()

    print(f"Len de padres es {len(padres)}")

    return padres

def pruebaSumaFitness():
    p = tp.Poblacion()
    p.calculoValorPoblacion()
    listaSumaFit = []

    sumaFit = 0
    sumaObj = 0
    # Inicializo el arreglo con la posición uno en cero porque despues el for recorre 9 elementos del arreglo
    #     de Cromosomas y son 10.
    listaSumaFit.append(0) 

    for cromo in p.arrGenes:
        sumaFit += cromo.funcFitness
        sumaObj += cromo.funcObjetivo
        listaSumaFit.append(sumaFit)

    print(f"La suma de funciones objetivos calculadas es {sumaObj}")
    print(f"La suma de funciones objetivos de la clase es {p.sumaPoblacion}")
    print(f"La suma de fitness es {sumaFit}")
    # if (p.sumaPoblacion == sumaObj) and sumaFit == 100:
    #     print("Test correcto")
    # else:
    #     print("Hubo un error al ejecutar el test")
    # print(f"La suma de los fitness es {sumaFit} y la lista  es {listaSumaFit}")
    # print("-------------------> La lista de fitness es:")
    # for i in p.arrGenes:
    #     print(f"Cromosoma: {p.arrGenes.index(i)} fintess: {i.funcFitness}")

def pruebaAplicoCrossover():
    p = tp.Poblacion()
    p.calculoValorPoblacion()

    # print("Padres desde Principal")
    padres = p.seleccionoPadres()

    hijos = p.aplicoCrossover(padres)

    # print(padres)
    # print(hijos)

    # print("Padres desde prueba")
    # print(padres[0].arrGenes)
    # print(padres[1].arrGenes)

    # print(hijos[0].arrGenes)
    # print(hijos[1].arrGenes)

def pruebaAplicoMutacion():

    p = tp.Poblacion()
    p.calculoValorPoblacion()


    print("Población original -------------------------------------------------------------")
    for i in p.arrGenes:
        print(i.arrGenes)

    hijosMutados = p.aplicoMutacion(p.arrGenes)
    
    print("Población mutada ---------------------------------------------------------------")
    for i in hijosMutados:
        print(i.arrGenes)
  

# -------------  Ejecución de funciones de Testing ----------------

# pruebaAplicoCorte()
# pruebaSeleccionoPadres()
pruebaSumaFitness()
# pruebaAplicoCrossover()
# pruebaAplicoMutacion()

