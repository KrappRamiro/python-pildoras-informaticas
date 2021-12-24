#Definicion de func decoradora
def funcion_decoradora(funcion_parametro):
	def funcion_interior(*args, **kwargs):
		print("Vamos a realizar un calculo")
		funcion_parametro(*args, **kwargs)
		print("Terminamos de realizar el calculo")
	return funcion_interior

@funcion_decoradora
def suma(n1,n2):
	print(n1+n2)

@funcion_decoradora
def resta(n1,n2):
	print(n1-n2)

@funcion_decoradora
def potencia(base, exponente):
	print(pow(base,exponente))

suma(7,2)
resta(6,28)
potencia(base=3, exponente=5)