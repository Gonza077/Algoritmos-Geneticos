from Ciudad import *
import pandas as pd

def cargarCiudades():
    ciudades=[]
    hojaExcel = pd.read_excel('./TablaCapitales.xlsx')
    for fila in hojaExcel.values:
        ciudad=Ciudad()
        ciudad.agregarNombre(fila[0])
        for j in range(1,len(fila)):
            ciudad.agregarCiudad(hojaExcel.columns[j], fila[j])
        ciudades.append(ciudad)
    return ciudades

ciudades=cargarCiudades()

for ciudad in ciudades:
    ciudad.datosCiudad()

