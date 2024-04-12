# Proyecto #2
# Creado por: Felipe Sánchez Segura 2023083272 
#             Axel Dimitri Castillo Collao 2023154988 
#             Yair González Núñez 2023048047 

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
plt.stem(Cara_Dado,probabilidad_Dado1, 'bo', basefmt=' ')
plt.title('Dado ideal 1')
plt.xlabel('Caras del dado')
plt.ylabel('Probabilidad')
plt.yticks([0,1/6,1],['0','1/6','1'])
#Dado 2
plt.figure()
plt.stem(Cara_Dado,probabilidad_Dado2, 'bo', basefmt=' ')
plt.title('Dado ideal 2')
plt.xlabel('Caras del dado')
plt.ylabel('Probabilidad')
plt.yticks([0,1/6,1],['0','1/6','1'])

#Dado trucado 1
plt.figure()
plt.stem(Cara_Dado,probabilidad_DadoTrucado1, 'bo', basefmt=' ')
plt.title('Dado trucado 1')
plt.xlabel('Caras del dado')
plt.ylabel('Probabilidad')
plt.yticks([0,0.06,0.7,1],['0','0.06','0.7','1'])
#Dado trucado 2
plt.figure()
plt.stem(Cara_Dado,probabilidad_DadoTrucado2, 'bo',basefmt=' ')
plt.title('Dado trucado 2')
plt.xlabel('Caras del dado')
plt.ylabel('Probabilidad')
plt.yticks([0,0.06,0.7,1],['0','0.06','0.7','1'])

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

    "Saque cada probabilidad a mano"
    la suma no da uno 
    
'''

Probabilidades_Ideales=[1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36]

Probabilidades_Trucadas=np.convolve(probabilidad_DadoTrucado1,probabilidad_DadoTrucado2)

# Tabla para la fmp
def tabularFuncion(px,pfx):
	"""
	Definición: Función que tabula listas en forma de tabla.
	Parámetros: px = lista de valores posibles de v.a.d
				pfx = lista de valores de función masa de probabilidad
				      para la v.a.d
	"""
	if len(px) != len(pfx):
		raise ValueError("Las listas x y f(X) deben tener el mismo tamaño")
	#impresión de encabezado	
	print("x\tf(x)")
	print("-"*12)
	for i in range(len(px)):
		print(f"{px[i]}\t{pfx[i]}")
		print(" ")

#Dados ideales
print("fmp dado ideal 1")
tabularFuncion(Cara_Dado,probabilidad_Dado1)
print("fmp dado ideal 2")
tabularFuncion(Cara_Dado,probabilidad_Dado2)
print("fmp suma ambos dados ideales")
tabularFuncion(Resultados_Posibles,Probabilidades_Ideales)
#Dados trucados
print("fmp dado trucado 1")
tabularFuncion(Cara_Dado,probabilidad_DadoTrucado1)
print("fmp dado trucado 2")
tabularFuncion(Cara_Dado,probabilidad_DadoTrucado2)
print("fmd suma de dados trucados")
tabularFuncion(Resultados_Posibles,Probabilidades_Trucadas)

#Grafica de probabilidad de los dados ideales
plt.figure()
plt.stem(Resultados_Posibles,Probabilidades_Ideales, 'bo', basefmt=' ')
plt.title('Dados Ideales')
plt.xlabel('Suma de los dados')
plt.ylabel('Probabilidad')
plt.yticks([0,1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36,1],['0','1/36','1/18','1/12','1/9','5/36','1/6','5/36','1/9','1/12','1/18','1/36','1'])
plt.xticks([2,3,4,5,6,7,8,9,10,11,12])

#Grafica de probabilidad de los dados trucados
plt.figure()
plt.stem(Resultados_Posibles,Probabilidades_Trucadas, 'bo', basefmt=' ')
plt.title('Dados Trucados')
plt.xlabel('Suma de los dados')
plt.ylabel('Probabilidad')
plt.yticks([0, 0.0036, 0.0072, 0.0492, 0.0912, 0.0948, 0.508,  0.0948, 0.0912, 0.0492, 0.0072, 0.0036, 1],['0','0.0036','0.0072','0.0492','0.0912','0.0948','0.508','0.0036','0.0072','0.0492','0.0912','0.0948','1'])
plt.xticks([2,3,4,5,6,7,8,9,10,11,12])

probas_binegativa=[0.1311,0.1935,0.1904,0.1561,0.1152,0.07937,0.05206,0.03293]
x_binegativa=[3,4,5,6,7,8,9,10]

Probas_Para3_7_Ideal=[0.00463, 0.01157, 0.0193, 0.0268, 0.0335, 0.039, 0.0434, 0.0465]

#Grafica de la funcion de masa de probabilidad para x natural y 3<x<11 con los dados ideales 
plt.figure()
plt.stem(x_binegativa,Probas_Para3_7_Ideal, 'bo', basefmt=' ')
plt.title('Probabilidad de obtener tres 7 con dados ideales')
plt.xlabel('Cantidad de ensayos')
plt.ylabel('Probabilidad')
plt.yticks(Probas_Para3_7_Ideal)
plt.xticks(x_binegativa)

#Grafica de la funcion de masa de probabilidad para x natural y 3<x<11 con los dados trucados
plt.figure()
plt.stem(x_binegativa,probas_binegativa, 'bo', basefmt=' ')
plt.title('Probabilidad de obtener tres 7')
plt.xlabel('Cantidad de ensayos')
plt.ylabel('Probabilidad')
plt.yticks(probas_binegativa)
plt.xticks(x_binegativa)

#Mostramos las graficas
plt.show()
