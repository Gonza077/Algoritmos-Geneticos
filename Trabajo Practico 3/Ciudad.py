class Ciudad():
    

    def __init__(self):
        self._nombre = ""
        self._ciudades = []

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setCiudad(self, ciudad):
        self._ciudades.append(ciudad)

    def getCiudades(self):
        return self._ciudades