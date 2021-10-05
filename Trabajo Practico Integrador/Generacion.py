import random as rnd
import matplotlib.pyplot as plt
import openpyxl as opyxl
from Poblacion import * 
from tabulate import tabulate

class Generacion(object):

    IDGeneracion = 1
    
    #Atributos de instancia
    def __init__(self):    
        self._ID=Generacion.IDGeneracion
        self._arrPoblaciones=[]
        Generacion.IDGeneracion+=1

    #Metodos
    def creoPoblacion(self):
        #TESTEO PARA VER SI CREA LAS DEMAS   
        poblacion=Poblacion()
        poblacion.instacioParques()
        """
        if(self.arrPoblaciones == [] ): 
            poblacion.instacioParques()       
        else:              
            #poblacion.creoNuevoParqueEolico(self.arrPoblaciones[-1]) 
            poblacion.instacioParques() 
        """
        poblacion.calculoDatosPoblacion()                   
        self._arrPoblaciones.append(poblacion)    

    def dibujoGrafica(self):
        arrPromedios = []
        arrMaximos = []
        arrMinimos = []

        for pobla in self.arrPoblaciones:
            arrPromedios.append(pobla.getMediaPoblacion())
            arrMaximos.append(pobla.getMaxCromosoma().getFuncObjetivo())
            arrMinimos.append(pobla.getMinCromosoma().getFuncObjetivo())

        plt.plot( arrPromedios, color='r', label='Medias')
        plt.plot( arrMaximos, color='g', label='Maximos', alpha=0.6)
        plt.plot( arrMinimos, color='y', label='Minimos',alpha=0.6)
        
        # Se pone nombre a los ejes X e Y 
        cantPoblacion=len(self.arrPoblaciones)
        plt.title(f"Grafico con {cantPoblacion} corridas")
        plt.xlabel("Numero de población")
        plt.ylabel("Valor")
        # Se agrega la leyenda para poder diferenciar cada color
        plt.legend()

        plt.show()
           
    def cargoDatosExcel(self,wb):
        hoja=wb.create_sheet(f"Generacion {self._ID}")     
        hoja.append(("Poblacion","Min. Func. Objetivo","Max. Func. Objetivo","Media Func. Objetivo"))
        for poblacion in self._arrPoblaciones:                      
            hoja.append(poblacion.ATupla())  
        wb.save("DatosEjercicio1.xlsx")        
      
    def datosGeneracion(self):
        tuplas=[]    
        for poblacion in self._arrPoblaciones:
            tuplas.append(poblacion.ATupla())
        cabecera=["Poblacion","Min. Func. Objetivo","Max. Func. Objetivo","Media Func. Objetivo"]
        print(tabulate(tuplas, headers=cabecera, stralign='center',tablefmt="simple",numalign="center"))
        #self.dibujoGrafica()
    
