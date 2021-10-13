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

        for pobla in self._arrPoblaciones:
            arrPromedios.append(pobla.getMediaPoblacion())
            arrMaximos.append(pobla.getMaxCromosoma().getFuncObjetivo())
            arrMinimos.append(pobla.getMinCromosoma().getFuncObjetivo())

        plt.plot( arrPromedios, color='r', label='Medias', linewidth=1)
        plt.plot( arrMaximos, color='g', label='Maximos', linewidth=1,alpha=0.5)
        plt.plot( arrMinimos, color='y', label='Minimos', linewidth=1,alpha=0.5)
        
        # Se pone nombre a los ejes X e Y 
        plt.title(f"Grafico de {len(self._arrPoblaciones)} corridas")
        plt.xlabel("Numero de población")
        plt.ylabel("Valor")
        # Se agrega la leyenda para poder diferenciar cada color
        plt.legend()
        plt.savefig(f"./Salidas/Grafica Generacion N°{self._ID}")
        #plt.show()
                              
    def datosGeneracion(self,wb):
        hojaExcel=wb.create_sheet(f"Generacion {self._ID}")
        tuplas=[]    
        cabecera=["Poblacion","Min. Func. Objetivo","Max. Func. Objetivo","Media Func. Objetivo"]  
        hojaExcel.append(cabecera)
        for poblacion in self._arrPoblaciones:
            tuplas.append(poblacion.ATupla())
            #Se insertan los datos de cada poblacion al Excel
            hojaExcel.append(poblacion.ATupla()) 
        #Se muestran los datos por consola      
        print(tabulate(tuplas, headers=cabecera, stralign='center',tablefmt="simple",numalign="center"))
        #Se guardan los datos de cada generacion en una hoja de Excel
        wb.save("./Salidas/Datos.xlsx")
        self.dibujoGrafica()
    
