from Cromosoma import Cromosoma


def prueba_inicializar_cromosoma():
    c = Cromosoma()
    c.mostrarGenes()

def prueba_crear_poblacion_inicial():
    poblacion = []

    for _ in range(0, 50):
        c = Cromosoma()
        poblacion.append(c)

    print(f"Se crearon {len(poblacion)} cromosomas")
    # print(list(map(lambda c: c.mostrarGenes(), poblacion)))

def prueba_calcular_funcion_objetivo():
    # TODO
    """ 
    
    """
    pass



# Pruebas a ejecutar
# prueba_inicializar_cromosoma()
prueba_crear_poblacion_inicial()