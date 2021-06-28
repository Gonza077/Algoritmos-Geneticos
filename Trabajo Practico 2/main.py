from Exhaustiva import *
from Elementos import *
from Mochila import *
from Solucion import *

def entero_a_binario(num, size = 10):
    """
    	Recibe un número entero positivo y devuelve su representación binaria en una lista de dimension 10.
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

#Definicion de parametros 
Mochila.volMaximo=4200
elementos=[]
valores=[20,40,50,36,25,64,54,18,46,28]
volumenes=[150,325,600,805,430,1200,770,60,930,353]

#Se instancian los elementos
for i in range(0,10):
    elementos.append(Elemento().setValor(valores[i]).setVolumen(volumenes[i]))

# mochila = Mochila()
# busqueda= Exhaustiva()
# busqueda.aplicoBusqueda(elementos,mochila)
# #Realizar las busquedas a partir de aca

# mochila.datosMochila()


# -----------------------------------------------------------------------------------------
# *******************
# -----------------------------------------------------------------------------------------

# Crear espacio de soluciones, son 1024 posibilidades

soluciones = []

# Esto es importante porque el profe nos dijo que se tiene que VER COMO Y CUANDO GENERAMOS LAS
#    1024 POSIBLES SOLUCIONES, sino no estaríamos entendiendo que es una busqueda exhaustiva

# Cada solucion es es una lista de 10 elementos donde un 0 significa que el elemento no esta en la
#    mochila y un 1 que esta.
for i in range(0, 1024):
    num_binario = entero_a_binario(i)
    soluciones.append(Solucion(num_binario, elementos))

soluciones_descartadas = []
soluciones_posibles = []

# Evaluar todas las soluciones
for i in range(0, 1024):
    solucion_actual = soluciones[i]
    if(solucion_actual.getVolumen() > Mochila.volMaximo):
        soluciones_descartadas.append(solucion_actual)
    else:
        soluciones_posibles.append(solucion_actual)

# Buscar la mejor solucion entre las soluciones posibles
mejor_solucion = soluciones_posibles[0]

for sol_actual in soluciones_posibles:
    if(sol_actual.getValor() > mejor_solucion.getValor()):
        mejor_solucion = sol_actual

# Mostrar información

print(f"Se evaluaron {len(soluciones)} soluciones.")
print(f"Se descartaron {len(soluciones_descartadas)} soluciones por no cumplir con la restricción de volumen.")
print(f"Se consideraron {len(soluciones_posibles)} soluciones para encontrar la mejor.")
print(f"La mejor soluciones encontrada fue: {mejor_solucion.getElementos()}")
print(f"   Su valor total es {mejor_solucion.getValor()} y su volumen es {mejor_solucion.getVolumen()}.")








