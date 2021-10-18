import random
import numpy as np
from Generacion import *
from Poblacion import *
from Cromosoma import *
from OperadoresGeneticos import *

Corridas=[1]   
generaciones=[]
#Parametros del Parque 
Cromosoma.tCromo=10
Cromosoma.CantAerogeneradores=25
Cromosoma.VelocidadViento=25 #Velocidad del viento
Cromosoma.TamañoCelda=180 #Distancia Minima de 4*R, donde R es 45 m
#Parametros de la Poblacion
Poblacion.tPobla=5 #Cantidad de parques x Poblacion
Poblacion.tipoSeleccion=Ruleta()
Poblacion.tipoCrossover=CrossOverUnPunto(0.75)
Poblacion.tipoMutacion=MutacionInvertida(0.20)
Poblacion.elitismo=False

#-----Creacion del parque eolico-----
arr=np.array([[0]*10]*10)
contador=0
while(contador<25):
    fRandom=random.randrange(len(arr))
    cRandom=random.randrange(len(arr[0]))    
    if arr[fRandom][cRandom]!=1:
        arr[fRandom][cRandom]=1
        contador+=1

#Verificacion de aerogeneradores
sum=0
for fila in arr:
    sum+= len(np.where(fila==1)[0])

#print(sum)

#-----Creacion del parque eolico-----

#-------Calculo del efecto estela-----
a=0.3333
radioAero=45
distanciaCasillas=1
coefDeArrastre= round(( 1 / (2 * math.log(80/0.05))),4)

#print(( 1 - ( 2 * a / (1 + (coefDeArrastre * distanciaCasillas * 180) / radioAero )**2) ) )
#print(25 * ( 1 - ( 2 * a / (1 + (coefDeArrastre * distanciaCasillas * 180) / radioAero )**2) ) )

#-------Calculo del efecto estela-----
def efectoEstela(velViento,distanciaCasillas):
    a=0.3333
    radioAero=45
    coefDeArrastre= round(( 1 / (2 * math.log(80/0.05))),4) #Aproximadamente 0.0678
    return velViento * ( 1 - ( 2 * a / (1 + (coefDeArrastre * distanciaCasillas * Cromosoma.TamañoCelda) / radioAero )**2) ) 

def calculoPotenciaAerogenerador(velViento):  
    #Cada indice de la lista contiene una lista donde el primer indice indica la velocidad del viento y el segundo la potencia asociada  
    velocidadesViento=[[0, 0],[1, 0],[2, 0],[3, 10],[4, 46],[5, 170],[6, 355],[7, 580],[8, 874],[9, 1219],[10, 1544],[11, 1740],[12, 1789],[13, 1800],[14, 1800],[15, 1800],[16, 1800],[17, 1800],[18, 1800],[19, 1800],[20, 1800],[21, 1800],[22, 1800],[23, 1800],[24, 1800],[25, 1800],[26, 0]]
    for i in range(len(velocidadesViento)-1):
        if velocidadesViento[i][0]<=velViento and velocidadesViento[i+1][0]>velViento:
            return velocidadesViento[i][1]
            break

funcObjetivo=0

for fila in arr:
    velViento=Cromosoma.VelocidadViento 
    aeroFilas=np.where(fila==1)[0] #Devuelve una tupla con un arreglo y el tipo de dato, solo tomo el arreglo
    if(len(aeroFilas)>0):
        funcObjetivo += calculoPotenciaAerogenerador(velViento)
        if(len(aeroFilas)>=2):  #Si existen al menos dos generadores en una fila existira el efecto estela
            for i in range(1,len(aeroFilas)):
                velViento = efectoEstela(velViento,aeroFilas[i]-aeroFilas[i-1]) #Distancia en indices entre cada aerogenerador
                funcObjetivo += calculoPotenciaAerogenerador(velViento)

#print(funcObjetivo)

#-------Calculo del efecto estela-----

#-------Crossover-----

cr1 = Cromosoma()
cr1.intancioAerogeneradores()
cr1.calculoFuncObjetivo()
cr2= Cromosoma()
cr2.intancioAerogeneradores()
cr2.calculoFuncObjetivo()

cr1.datosParque()
cr2.datosParque()

hijo1=Cromosoma()
hijo2=Cromosoma()

#La posicion de corte se mide en horizontal
posicionCorte=random.randint(0,Cromosoma.tCromo-1)
print(f"Posicion de corte en indice N° {posicionCorte}")

""" for fila in range(0,Cromosoma.tCromo):
    for col in range(0,posicionCorte):
        #Habria que pensar si es posible hacer que la fila y col se saquen por defecto
        hijo1.insertoGen(cr1._genes[fila][col],fila,col)
        hijo2.insertoGen(cr2._genes[fila][col],fila,col)
        #Posteriormente se intercambian los genes de cada padre en los hijos, luego de la posicion del corte
    for col in range(posicionCorte,Cromosoma.tCromo):
        hijo1.insertoGen(cr2._genes[fila][col],fila,col)
        hijo2.insertoGen(cr1._genes[fila][col],fila,col)   """
for fila in range(0,posicionCorte):
    hijo1.insertoGenes(cr1._genes[fila],fila)
    hijo2.insertoGenes(cr2._genes[fila],fila)
for fila in range(posicionCorte,Cromosoma.tCromo):
    hijo1.insertoGenes(cr2._genes[fila],fila)
    hijo2.insertoGenes(cr1._genes[fila],fila)


hijo1.calculoFuncObjetivo()
hijo2.calculoFuncObjetivo()

hijo1.datosParque()
hijo2.datosParque()

#EL UNICO PROBLEMA QUE QUEDA ACA ES QUE CUANDO SE APLICA, QUEDAN EN LA MAYORIA
#SUPERANDO LOS 25 MOLINOS POR PARQUE
#hijo1.getAerogeneradores()
#hijo2.getAerogeneradores()

#-------Crossover-----

hijo1.datosParque()
hijo1.mutoGen()
hijo1.calculoFuncObjetivo()
hijo1.datosParque()

hijo1.getAerogeneradores()




