class Areas:
	"""Esta clase calcula el area de distintas figuras geometricas"""

	def areaCuadrado(lado):
		"""Calcula el area de un cuadrado elevando al cuadrado el lado pasado por parametro"""
		return "El area del cuadrado es: " + str(lado*lado)

	def areaTriangulo(base,altura):
		"""Calcula el area de un triangulo multiplicando la base y la altura, y dividiendo el resultado por dos"""
		return "El area del triangulo es: " + str((base*altura)/2)

help(Areas)