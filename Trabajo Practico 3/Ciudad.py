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
    
    def agregarDistancia(self,dist):
        self._distancia=dist
    
    def datosCiudad(self):
        print("-------------------------------------------------")
        print(f"Ciudad {self._nombre}, distancias a otras ciudades: \n")
        for ciudad in self._ciudades:
            print(f"{ciudad._nombre} a una distancia --> {ciudad._distancia} Km")
        print("-------------------------------------------------")
    
    

