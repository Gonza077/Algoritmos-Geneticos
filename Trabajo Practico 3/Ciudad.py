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
        """Ordena las ciudad por distancia y verifica que la mas proxima no este en la ruta actual."""
        self._ciudades.sort(key = lambda c: c.getDistancia())
        for i in self._ciudades:
            print(f'Ciudad: {i.getNombre()} distancia: {i.getDistancia()}')
        for c in self._ciudades:
            if (c not in ruta and c.getDistancia() != 0):
                return c
        return None
        
    
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
    
    

