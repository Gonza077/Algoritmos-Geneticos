class Ciudad():

    def __init__(self):
        self._nombre=None
        self._distancia=None
        self._ciudades=[]

    def agregarCiudad(self,nomb,dist):
        ciudad= Ciudad()
        ciudad.agregarNombre(nomb)
        ciudad.agregarDistancia(dist)
        if self._nombre==nomb:  #Esto por que lo asigna como nan, un formato de Pandas para que no dificulte posteriormente
            ciudad.agregarDistancia(0)
        self._ciudades.append(ciudad)
    
    def agregarNombre(self,nomb):
        self._nombre=nomb

    def getCiudadMasCercana(self, ruta):
        """ Devuelve la ciudad mas cercana que no este incluida en la ruta pasada como parametro.
                Ordena las ciudad por distancia y verifica que la mas proxima no este en la ruta actual.
        """
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
        # self._ciudades.pop(ciudadSiguiente)
        
        for c in self._ciudades:
            if (c.getNombre() == ciudadSiguiente.getNombre()):
                return c.getDistancia()

    def getNombre(self):
        return self._nombre

    def getDistancia(self):
        return self._distancia

    def agregarDistancia(self,dist):
        self._distancia=dist
    
    def datosCiudad(self):
        print("-------------------------------------------------")
        print(f"Ciudad {self._nombre}, distancias a otras ciudades: \n")
        for ciudad in self._ciudades:
            print(f"{ciudad._nombre} a una distancia --> {ciudad._distancia} Km")
        print("-------------------------------------------------")