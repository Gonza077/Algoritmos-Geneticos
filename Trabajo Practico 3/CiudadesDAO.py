from Ciudad import *
import pandas as pd
import numpy as np

class CiudadesDAO():

    _ciudades=[]

    @classmethod
    def cargarCiudades(self):
        hojaExcel = pd.read_excel('./TablaCapitales.xlsx')
        for fila in hojaExcel.values:
            ciudad=Ciudad()
            ciudad.agregarNombre(fila[0])
            ciudad._idCiudad=Ciudad.IDCiudad
            Ciudad.IDCiudad+=1            
            for j in range(1,len(fila)):
                DistanciaCiudad=Ciudad()
                DistanciaCiudad.agregarNombre(hojaExcel.columns[j])
                DistanciaCiudad.agregarDistancia(fila[j])
                if ciudad._nombre==DistanciaCiudad.getNombre():  
                    DistanciaCiudad.agregarDistancia(0)
                ciudad.agregarCiudad(DistanciaCiudad)
            self._ciudades.append(ciudad)
  
    @classmethod
    def retornarCiudades(self):
        return self._ciudades

    @classmethod
    def getCiudad(self,nombre):
        for ciu in self._ciudades:
            if ciu.getNombre().lower() == nombre.lower():
                return ciu
    
    @classmethod
    def buscarRuta(self,nombreCiudad):
        ruta = []
        ciudad = self.getCiudad(nombreCiudad)
        ruta.append(ciudad)
        proxCiudad = ciudad.getCiudadMasCercana(ruta)  
        while len(ruta) <= 23:
            ruta.append(proxCiudad)
            # Le tengo que pedir a la lista de ciudades que cargamos desde Pandas
            #     donde esta la proxima mas cercana.
            ciudad = self.getCiudad(proxCiudad.getNombre())
            proxCiudad = ciudad.getCiudadMasCercana(ruta)
        # Saco la ciudad inicial, ya que luego la agregamos al final
        ruta.pop(0)
        # Agrego la distancia de la ciudad final a la incial, nos dijo Victor en clase que lo hagamos.
        proxCiudad = ciudad.getCiudadMasCercana(ruta)
        ruta.append(proxCiudad)
        return ruta
        
    @classmethod
    def buscarRutaMinima(self):
        rutaMinima = []
        distanciaMinima = float("inf")
        for ciu in self._ciudades:
            ruta = self.buscarRuta(ciu.getNombre())
            arreglo_distancias = list(map(lambda x:x.getDistancia(), ruta))
            distTotal = np.sum(arreglo_distancias)
            if (distTotal < distanciaMinima):
                distanciaMinima = distTotal
                rutaMinima = ruta
            #print(f"La ruta mínima desde {ciu.getNombre()} es de:{distTotal} Km.")
            #print(f'{list(map(lambda x:x.getNombre(), ruta))}')
        return rutaMinima
    
    