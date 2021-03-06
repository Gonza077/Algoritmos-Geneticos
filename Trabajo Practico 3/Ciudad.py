class Ciudad():
    
    IDCiudad = 1

    def __init__(self):
        self._nombre=None
        self._distancia=None
        self._ciudades=[]

    def agregarCiudad(self,ciudad):
        self._ciudades.append(ciudad)
    
    def agregarNombre(self,nomb):
        self._nombre=nomb

    def getCiudadMasCercana(self, ruta):
        """ Devuelve la ciudad mas cercana que no este incluida en la ruta pasada como parametro. Ordena las ciudad por distancia y verifica que la mas proxima no este en la ruta actual. """
        if len(ruta) == 24:
            return False
        # Ordenar las ciudades por distancia
        self._ciudades.sort(key = lambda c: c.getDistancia())
        # Crear una lista con los nombres de las ciudades.
        #     Se usa porque las ciudades que estan en la ruta no son el mismo objeto que las de
        #     que tiene la ciudad cargadas.
        nombres_ruta = list(map(lambda c: c.getNombre(), ruta))
        for c in self._ciudades:
            if (c.getNombre() not in nombres_ruta and c.getDistancia() != 0):
                return c
    
    def getDistanciaTo(self, ciudadSiguiente):
        for c in self._ciudades:
            if (c.getNombre() == ciudadSiguiente.getNombre()):
                return c.getDistancia()
                break

    def getNombre(self):
        return self._nombre
    
    def getID(self):
        return self._idCiudad

    def getDistancia(self):
        return self._distancia

    def agregarDistancia(self,dist):
        self._distancia=dist
    
    def datosCiudad(self):
        print(f"Ciudad {self._nombre} - ID {self._idCiudad}")
    
    

