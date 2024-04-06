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

Resultados_Posibles[2,3,4,5,6,7,8,9,10,11,12]

'''
    conosiendo los resultados posibles tenemos que calcular la probablidad de cada uno dadas las probabilidades
    de los dos dados ideales y los dos dados trucados
'''
Probabilidades_Ideales[]
probabilidades_trucadas[]




plt.show()

