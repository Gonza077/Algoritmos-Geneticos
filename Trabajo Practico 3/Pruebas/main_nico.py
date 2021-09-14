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

    def mostrar_ciudades(self):
        print()
        print(f"Lista de ciudades de {self._nombre}")
        print("------------------------------------")
        for c in self._ciudades:
            print(f"Ciudad {c[0]} a {c[1]} kilometros")


lista_ciudades = []

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

# Mostrar lista de ciudades   
print("Lista de ciudades:")
for c in lista_ciudades:
    print(c)

# Mostrar ciudades cercanas a formosa
print(lista_ciudades[1].mostrar_ciudades())

