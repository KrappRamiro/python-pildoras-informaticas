# Ejemplo 1:
# En vez de hacer el calculo del area de un triangulo con una funcion, se puede hacer con un lambda:
'''
def calcular_area_triangulo(base,altura):
	return (base*altura)/2
'''
# Esto se puede pasar a lambda de esta forma
# <nombre_de_la_funcion> = lambda <parametros> : <lo que retorna>
area_triangulo = lambda base,altura: (base*altura)/2

print(area_triangulo(9,6 ))
print(area_triangulo(4,26))
print(area_triangulo(3,5 ))

# ---------------------------------- #
# Ejemplo 2:
# <nombre_de_la_funcion> = lambda <parametros> : <lo que retorna>
al_cubo = lambda numero : pow(numero,3)
print(al_cubo(5))

# ---------------------------------- #
#Ejemplo 3:
# quiero printear la comision de juan de esta forma:		¡$56000!
destacar_valor = lambda comision: "¡${}!".format(comision) 	#aca lo importante son los {}, format lo que hace es usar los {} para dar formato,
															# es como cuando se usa print(f.....);		comision ----> {}
comision_juan = 56000
print(comision_juan)
print(destacar_valor(comision_juan))





















