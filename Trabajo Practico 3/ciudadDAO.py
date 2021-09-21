from ciudad import *
import pandas as pd

class CiudadesDAO():

    _ciudades=[]

    @classmethod
    def cargarCiudades(self):
        hojaExcel = pd.read_excel('./TablaCapitales.xlsx')
        for fila in hojaExcel.values:
            ciudad=Ciudad()
            ciudad._idCiudad=Ciudad.IDCiudad
            Ciudad.IDCiudad+=1
            ciudad.agregarNombre(fila[0])
            for j in range(1,len(fila)):
                ciudad.agregarCiudad(hojaExcel.columns[j], fila[j])
            self._ciudades.append(ciudad)
  
    @classmethod
    def retornarCiudades(self):
        return self._ciudades

    def getCiudad(nombre):
        for ciu in CiudadesDAO.retornarCiudades():
            if ciu.getNombre().lower() == nombre.lower():
                return ciu