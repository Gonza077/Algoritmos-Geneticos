import random
import numpy as np

#Testeo de la construccion de la matriz
arr=np.array([[0]*12]*10)

for fila in arr:
    print(fila)

print()
cont=0
while cont<25:
    cont+=1
    #Se toma un indice de fila al azar
    filRnd=random.randrange(len(arr))
    #Se toma un indice de columna al azar
    colRnd=random.randrange(len(arr[0]))
    arr[filRnd,colRnd]=1

for fila in arr:
    print(fila)
print(cont)


    

