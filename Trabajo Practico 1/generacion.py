import random as rnd
import matplotlib.pyplot as plt
import openpyxl as opyxl
from tabulate import tabulate
from poblacion import Poblacion

class Generacion(object):
    
    #Atributos de instancia
    def __init__(self):    
        self.arrPoblaciones=[]

    #Metodos
    def creoGeneracion(self):
        """Si se ejecuta por primera vez, generara una poblacion, si no, a la ultima existente se le aplicara algun operador genetico"""
        poblacion=Poblacion()
        if(self.arrPoblaciones == [] ): 
            poblacion.instancioCromosomas()       
        else:              
            poblacion.creoNuevaPoblacion(self.arrPoblaciones[-1])      
        poblacion.calculoDatosPoblacion()                     
        self.arrPoblaciones.append(poblacion)
    
    def dibujoGrafica(self):
        arrPromedios = []
        arrMaximos = []
        arrMinimos = []

        for pobla in self.arrPoblaciones:
            arrPromedios.append(pobla.mediaPoblacionFO)
            arrMaximos.append(pobla.maxCromosoma.funcObjetivo)
            arrMinimos.append(pobla.minCromosoma.funcObjetivo)

        plt.plot( arrPromedios, color='r', label='Medias',)
        plt.plot( arrMaximos, color='g', label='Maximos', alpha=0.6)
        plt.plot( arrMinimos, color='y', label='Minimos',alpha=0.6)
        
        # Se pone nombre a los ejes X e Y 
        cantPoblacion=len(self.arrPoblaciones)
        plt.title(f"Grafico con {cantPoblacion} corridas")
        plt.xlabel("Numero de población")
        plt.ylabel("Valor")
        plt.ylim(0, 1.1)
        # Se agrega la leyenda para poder diferenciar cada color
        plt.legend()

        plt.show()
        
    def cargoDatosExcel(self,wb):
         #Se crea una instancia de un libro en blanco que NO esta activa
        hoja=wb.create_sheet("Generacion")     
        hoja.append(("Poblacion","Min. FO","Genes cromosoma menor","Max. FO","Genes cromosoma Mayor","Media FO"))
        for poblacion in self.arrPoblaciones:                      
            hoja.append(poblacion.ATupla())  
        wb.save("DatosEjercicio1.xlsx")            
    
    def datosGeneracion(self):
        tuplas=[]
        for poblacion in self.arrPoblaciones:
            #if (poblacion.ID % ((len(self.arrPoblaciones)/20)) == 0): #Dependiendo del tamaño de la poblacion, y la cantidad de registros que se quieran mostrar, en este caso 20
                tuplas.append(poblacion.ATupla())
        cabecera=["Poblacion","Min. FO","Genes cromosoma menor","Max. FO","Genes cromosoma Mayor","Media FO"]
        print(tabulate(tuplas, headers=cabecera, stralign='center',tablefmt="simple",numalign="center"))
        self.dibujoGrafica()