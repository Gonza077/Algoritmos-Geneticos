import pandas as pd
from Ciudad import *

hojaExcel = pd.read_excel('./TablaCapitales.xlsx')

#print(hojaExcel.values[0][1])
#print(hojaExcel.columns[1])

arrCiudades = []

for i in range(1, len(hojaExcel.columns)):
    c = Ciudad()
    c.setNombre(hojaExcel.columns[i])
    for j in range(1, len(hojaExcel.values[i-1])):
        tupla = (hojaExcel.columns[j], hojaExcel.values[i-1][j])
        c.setCiudad(tupla)
    arrCiudades.append(c)

for c in arrCiudades[23].getCiudades():
    print(c)