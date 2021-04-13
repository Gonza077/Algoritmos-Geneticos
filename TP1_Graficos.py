import matplotlib.pyplot as plt
import numpy as np

# -------------->  Pruebas de ltrabajo práctico de simulación
def graficarPromediosNumCola(lista = [1,2,3,4,5,6,7,8,9], promedioNumCola = 0.77):
    
    plt.figure().patch.set_facecolor('silver')
    plt.title('Número promedio de clientes en cola')
    plt.plot(lista, color='r')
    plt.xlabel("tiempo")
    plt.ylabel("Número promedio en cola")
    # Banda horizontal de y=0 a y=2 de color azul
    # y 30% de transparencia (alpha=0.3)
    plt.axhspan(promedioNumCola - (promedioNumCola * 0.03), promedioNumCola + promedioNumCola * 0.03, alpha=0.8,
    color='cornflowerblue')
    plt.text(0.3 * len(lista), 0.83*(max(lista) + 1), 'Número promedio de clientes en cola: %.2f' % promedioNumCola, color="r")
    plt.axhline(promedioNumCola, color='r', ls="-.", xmax=3) # Comando para linea horizontal constante
    plt.ylim(0, max(lista) + 1) # Limites para el eje Y
    plt.xlim(0, len(lista)) # Limites para el eje X
    plt.show()

Coeficiente = 12
Dominio=2**Coeficiente-1
def graficarFuncionObjetivo():
    
    def f(t):
        return (t / Dominio) ** 2

    print(f"2**10 es {2**10}, 2**15 es {2**15}, 2**20 es {2**20}, 2**25 es {2**25}")
    print(f"El valor maximo del dominio es {2**30} (Pasando los cien mil millones)")
    t = np.arange(0.0, 2**Coeficiente, 0.02)
    plt.figure()
    plt.xlim(0, 2**Coeficiente)
    plt.ylim(0, 1)
    plt.plot(t, f(t), 'ro')
    plt.show()
    

# graficarPromediosNumCola()
graficarFuncionObjetivo()