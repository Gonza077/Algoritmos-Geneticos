import math
import random as rnd

def binario_a_entero(cromosoma):
    """Recibe un cromosoma en formato de lista de ceros o unos [0,1,1,0 ...] y lo transforma a un valor entero."""

    num = 0
    for i in range(len(cromosoma) - 1, -1, -1):
        num += 2**(len(cromosoma) - 1 - i) * cromosoma[i]
    return num
    
def entero_a_binario(num, size = 30):
    """
    	Recibe un número entero positivo y devuelve su representación binaria en una lista de dimension 30.
    	Se puede cambiar el tamaño del arreglo devuelto modificando el parametro "size".
    """
    lista = [] 
    # 53    - 1 1 0 1 0 1 - 32 16 8 4 2 1
    for i in range(size, 0, -1):
        if (num < 2**(i - 1)):
            lista.append(0)
        else:
            lista.append(1)
            num -= 2** (i - 1)
    return lista

def evaluar_cromosoma(cromosoma):
    """Retornar el valor de la función objetivo de cada cromosoma"""

    valor_entero = binario_a_entero(cromosoma)
    valor_objetivo = ( valor_entero / ( 2**30 - 1)) ** 2
    return valor_objetivo

def evaluar_fitness_cromosoma(cromosoma):
    """Retornar el valor de la función fitness de cada cromosoma"""

    pass
    

def crear_individuo(cant_genes):
    """Dependiendo del tamaño de los genes se retorna una lista de la dimension especificada con 0s y 1s"""

    cromosoma=[]
    for x in range(0,cant_genes):
        cromosoma.append(rnd.randint(0,1))
    return cromosoma

def crear_poblacion(tam_poblacion):
    """Retorna una x cantidad de cromosomas que forman parte de la poblacion especificada"""

    poblacion=[]
    for x in range(0,tam_poblacion-1):
        poblacion.append(crear_individuo(30))
    return poblacion

cromosoma = crear_individuo(30)

# entero = 2057
# print("El entero pasado a binario dio:\n" + str(entero_a_binario(entero)))
# print("El binario pasado a entero dio: " + str(binario_a_entero(entero_a_binario(entero))))
# print("El entero pasado a binario dio:\n" + str(entero_a_binario(entero)))

print(cromosoma)
print(entero_a_binario(binario_a_entero(cromosoma)))
