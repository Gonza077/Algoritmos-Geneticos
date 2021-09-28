from AlgoritmoGenetico.Cromosoma import *
from AlgoritmoGenetico.Poblacion import *
from AlgoritmoGenetico.OperadoresGeneticos import *
from AlgoritmoGenetico.Generacion import *
import openpyxl as opyxl

Corridas = 200
Cromosoma.tCromo = 24
Cromosoma.ciudadesDAO = CiudadesDAO()
Cromosoma.ciudadesDAO.cargarCiudades()
Poblacion.tPobla = 50
Poblacion.tipoSeleccion = Ruleta()
Poblacion.tipoCrossover = CrossOverCiclico(0.75)
Poblacion.tipoMutacion = MutacionAdjointSwap(0.05)
Poblacion.elitismo = False
generacion = Generacion()
for i in range(0, Corridas):
    generacion.creoGeneracion()
generacion.datosGeneracion()

wb = opyxl.Workbook()
generacion.cargoDatosExcel(wb)