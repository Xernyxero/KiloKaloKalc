import numpy as np

def cherni_function(tipo_comida, matriz_macros, lista_kcal_alimentos, proporciones_programa, objetivo_kcal):

	# Transformar los datos en formato array
	A = np.array(matriz_macros)

	# Numero de ingredientes
	n = A.shape[0]

	# Proporciones de la receta segun el programa elegido
	P = np.array(proporciones_programa)

	# Inicializo una matriz de ceros
	B = np.zeros((3,n))

	# Transformo la matriz de datos en la matriz de trabajo
	for i in [0,1]:
	    for j in  np.arange(n):
	        suma = 0
	        for k in  np.arange(3):
	            suma += A[j,k]
	        B[i,j] = A[j,i] - P[i]*suma

	for m,l in enumerate(lista_kcal_alimentos):
	    B[2,m] = l

	# Definir el vector de términos independientes b (3x1)
	b = np.array([0, 0, objetivo_kcal*tipo_comida])

	# Calcular las cantidades utilizando el método de mínimos cuadrados
	x = np.linalg.lstsq(B, b, rcond=None)[0]*100 #[g]

	return(x)