
class Busqueda:

    def __init__(self) -> None:
        self._mejorSolucion=None

    @staticmethod
    def entero_a_binario(num, size):
        """
            Recibe un número entero positivo y devuelve su representación binaria en una lista de dimension 10.
            Se puede cambiar el tamaño del arreglo devuelto modificando el parametro "size".
        """
        lista = [] 
        # 53    - 1 1 0 1 0 1 - 32 16 8 4 2 1
        for i in range(size, 0, -1):
            if (num < 2**(i - 1)):
                lista.append(0)
            else:
                lista.append(1)
                num -= 2** (i - 1)
        return lista