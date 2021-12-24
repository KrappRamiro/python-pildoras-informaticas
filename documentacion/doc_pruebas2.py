import math
def raiz_cuadrada(lista_numeros):
	"""La funcion devuelve una lista con la raiz cuadrada de los numeros que
	habia dentro de la lista pasada x parametro
	##### Esto es de ejemplo de como hacer fors en el doctest, no es la mejor forma de hacerlo :/

	>>> lista=[]
	>>> for i in [4, 9, 16]:
	...		lista.append(i)
	>>> raiz_cuadrada(lista)
	[2.0, 3.0, 4.0]

	## Error handling
	## No se puede hacer sqrt de numeros negativos
	>>> lista=[]
	>>> for i in [-4, -9, -16]:
	...		lista.append(i)
	>>> raiz_cuadrada(lista)
	Traceback (most recent call last):
		...
	ValueError: math domain error

	### En este caso, los ... sirven para decir "cualquier cosa en medio"
	"""

	return [math.sqrt(n) for n in lista_numeros]

print(raiz_cuadrada([9,16,25,36]))


import doctest
doctest.testmod()