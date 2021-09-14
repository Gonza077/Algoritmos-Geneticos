import pandas as pd

class Ciudad():
    def __init__(self, nombre = ''):
        self._nombre = nombre
        self._ciudades = []
        # Ejemplo de como sería ese arreglo de cada ciudad
        #     _ciudades = [(‘cordoba’, 646), (‘corrientes’, 792), (‘formosa’, 933 ), ...]

    def get_nombre(self):
        return self._nombre

    def add_ciudad(self, ciudad, distancia):
        self._ciudades.append((ciudad, distancia))

    def get_ciudad_mas_cercana(self):
        """
            Devuelve la tupla con la ciudad mas.
        """
        self._ciudades.sort(key = lambda x: x[1])
        print(self._ciudades[0])
        
        return self._ciudades[0]

    def mostrar_ciudades(self):
        print()
        print(f"Lista de ciudades de {self._nombre}")
        print("------------------------------------")
        for c in self._ciudades:
            print(f"Ciudad {c[0]} a {c[1]} kilometros")

def cargar_ciudades():
    """
    Retorna un arreglo con las ciudades cargadas desde el archivo externo.
    Se podría crear otra función que permita seleccionar el archivo por pantalla
    """
    # Leer archivo excel usando Pandas        
    hojaExcel = pd.read_excel('./TablaCapitales.xlsx')

    # Recorrer los valores. Descarta automaticamente la primera columna del excel.
    for ciudad in hojaExcel.values:
        # Crear cada ciudad y asignar el nombre que esta en la primera posición del arreglo
        c = Ciudad(ciudad[0])

        # Recorro las demas ciudades enumerando cada posición para descartar la primera
        #     posición de cada fila y los valores 'nan'.
        for j, dis in enumerate(ciudad):
            if j != 0 and str(dis) != 'nan':
                c.add_ciudad(hojaExcel.columns[j], ciudad[j])
        lista_ciudades.append(c)
    
    return lista_ciudades

def get_ciudad(lista, nombre):
    """
        Recibe un nombre de una ciudad y devuelve el objeto ciudad.
    """
    for c in lista:
        if c.get_nombre().lower() == nombre.lower():
            return c


def buscar_ruta(lista_ciudades, nombre_ciudad):
    ruta = []
    ciudad = Ciudad()

    for ciu in lista_ciudades:
        if ciu.get_nombre().lower() == nombre_ciudad.lower():
            ciudad = ciu

    # Buscar ciudad mas proxima
    tupla = ciudad.get_ciudad_mas_cercana()
    ruta.append(tupla)
    # TODO https://realpython.com/python-type-checking/#type-systems
    #   Tengo que ir descartando de la busqueda las ciudades que ya estan en el arreglo de rutas.
    #       Creo que va a hacer el arreglo de ciudades con objetos y no con tuplas.
    while tupla[0].lower() != nombre_ciudad.lower():
        ciudad = get_ciudad(lista_ciudades, tupla[0])
        tupla = ciudad.get_ciudad_mas_cercana()
        ruta.append(tupla)

    return ruta

lista_ciudades = []

# Cargar las ciudades del archivo excel
lista_ciudades = cargar_ciudades()

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
    ruta = buscar_ruta(lista_ciudades, ciudad_origen)
    print(f"La ruta encontrada es: {ruta}")

