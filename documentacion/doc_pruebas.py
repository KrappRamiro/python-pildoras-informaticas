def areaTriangulo(base,altura):
	"""Calcula el area de un triangulo multiplicando la base y la altura, y dividiendo el resultado por dos
	# A continuacion, va un ejemplo de llamada a funcion y luego el return esperado.

	>>> areaTriangulo(3,6)
	9.0

	# Si eso fuera 9.1, el doctest tiraria error
	# Tambien se pueden hacer multiples pruebas

	>>> areaTriangulo(4,5)
	10.0

	"""
	return (base*altura)/2

import doctest
doctest.testmod()



def comprueba_mail(mail_usuario):
	"""La funcion evalua un mail recibido por parametro, en busca de si tiene
	una sola @ y si la misma no esta al final
	
	>>> comprueba_mail('juan@cursos.es')
	True
	
	>>> comprueba_mail('juancursos.es')
	False
	
	>>> comprueba_mail('juan@cursos@excelentes.es')
	False

	>>> comprueba_mail('juancursos.es@')
	False
	"""

	arroba=mail_usuario.count('@')

	if arroba!=1 or mail_usuario.rfind('@')==(len(mail_usuario)-1): #Lo que va despues del == es basicamente
		# si lo que encontro esta en la posicion final del mail del usuario
		# rfind retorna el indice de la ultima ocurrencia del '@'
		return False
	else: return True

doctest.testmod()