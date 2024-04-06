'''
    En este programa se van a calcular la probabilidades de los dadas y las funciones de masa de probabilidad


'''
import math
import numpy as np
from matplotlib import pyplot as plt

'''
    Primero graficamos la probabilidad de cada dado de forma individula
'''

Cara_Dado=[1,2,3,4,5,6]

#Probabilidades del dado 1
probabilidad_Dado1=[1/6,1/6,1/6,1/6,1/6,1/6]
#Probabilidades del dado 2
probabilidad_Dado2=[1/6,1/6,1/6,1/6,1/6,1/6]

#Probabilidades del dado trucado 1
probabilidad_DadoTrucado1=[0.06,0.06,0.7,0.06,0.06,0.06]
#Probabilidades del dado trucado 2
probabilidad_DadoTrucado2=[0.06,0.06,0.06,0.7,0.06,0.06]

#Dado 1
plt.figure()
plt.plot(Cara_Dado,probabilidad_Dado1, 'bo')
plt.title('Dado ideal 1')
plt.xlabel('Caras de dado')
plt.ylabel('Probabilidad')
plt.yticks([1/6,1/6,1/6,1/6,1/6,1/6],['1/6','1/6','1/6','1/6','1/6','1/6'])
#Dado 2
plt.figure()
plt.plot(Cara_Dado,probabilidad_Dado2, 'bo')
plt.title('Dado ideal 2')
plt.xlabel('Caras de dado')
plt.ylabel('Probabilidad')
plt.yticks([1/6,1/6,1/6,1/6,1/6,1/6],['1/6','1/6','1/6','1/6','1/6','1/6'])

#Dado trucado 1
plt.figure()
plt.plot(Cara_Dado,probabilidad_DadoTrucado1, 'bo')
plt.title('Dado trucado 1')
plt.xlabel('Caras de dado')
plt.ylabel('Probabilidad')
plt.yticks([0.06,0.06,0.7,0.06,0.06,0.06],['0.06','0.06','0.7','0.06','0.06','0.06'])
#Dado trucado 2
plt.figure()
plt.plot(Cara_Dado,probabilidad_DadoTrucado2, 'bo')
plt.title('Dado trucado 2')
plt.xlabel('Caras de dado')
plt.ylabel('Probabilidad')
plt.yticks([0.06,0.06,0.06,0.7,0.06,0.06],['0.06','0.06','0.06','0.7','0.06','0.06'])

'''
    Ahora graficamos las resultados posibles tirando los dos dados y dadas las probabilidades
    en este caso hay que anailisar todos los posibles resultados que se pueden obtener con dos
    dados ideales y dos dados trucados
'''

Resultados_Posibles=[2,3,4,5,6,7,8,9,10,11,12]

'''
    conociendo los resultados posibles tenemos que calcular la probablidad de cada uno dadas las probabilidades
    de los dos dados ideales y los dos dados trucados
    Entonces
    Para conseguir un:
    2  tenemos 1:1, una forma
    3  tenemos 1:2, 2:1, dos formas
    4  tenemos 1:3, 3:1, 2:2, tres formas
    5  tenemos 1:4, 4:1, 2:3, 3:2, cuatro formas
    6  tenemos 1:5, 5:1, 2:4, 4:2, 3:3, cinco formas
    7  tenemos 1:6, 6:1, 2:5, 5:2, 3:4, 4:7, seis formas
    8  tenemos 2:6, 6:2, 3:5, 5:3, 4:4, cinco formas
    9  tenemos 3:6, 6:3, 4:5, 5:4, cuatro formas
    10 tenemos 4:6, 6:4, 5:5 tres formas
    11 tenemos 5:6, 6:5, dos formos
    12 tenemos 6:6 una forma

    Lo que nos da un total de 36 diferentes posibilidades
'''

Probabilidades_Ideales=[1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36]
Probabilidades_Trucadas=[9/2500,9/1250,219/2500,21/125,1453/2500,1243/1250,1453/2500,21/125,219/2500,9/1250,9/2500]

#Grafica de probabilidad de los dados ideales
plt.figure()
plt.plot(Resultados_Posibles,Probabilidades_Ideales, 'bo')
plt.title('Dados Ideales')
plt.xlabel('Suma de los dados')
plt.ylabel('Probabilidad')
plt.yticks([1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36],['1/36','1/18','1/12','1/9','5/36','1/6','5/36','1/9','1/12','1/18','1/36'])
plt.xticks([2,3,4,5,6,7,8,9,10,11,12])

#Grafica de probabilidad de los dados trucados
plt.figure()
plt.plot(Resultados_Posibles,Probabilidades_Trucadas, 'bo')
plt.title('Dados Trucados')
plt.xlabel('Suma de los dados')
plt.ylabel('Probabilidad')
plt.yticks([9/2500,9/1250,219/2500,21/125,1453/2500,1243/1250,1453/2500,21/125,219/2500,9/1250,9/2500],['9/2500','9/1250','219/2500','21/125','1453/2500','1243/1250','1453/2500','21/125','219/2500','9/1250','9/2500'])
plt.xticks([2,3,4,5,6,7,8,9,10,11,12])



plt.show()

