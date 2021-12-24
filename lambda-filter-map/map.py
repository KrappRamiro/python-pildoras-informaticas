class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
	
	def __str__(self):
		return "{} que trabaja como {} que tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)


lista_empleados=[
	Empleado("Juan", 	"Empleado", 	45000),
	Empleado("Pepe", 	"Jefe de area", 75000),
	Empleado("Agustin", "Secretario", 	40000),
	Empleado("Benjamin","CEO", 			150000)
]

def calcular_comision(empleado):
	if empleado.salario < 50000: empleado.salario = empleado.salario*1.20
	return empleado

lista_empleados_comision=map(calcular_comision, lista_empleados)	

for empleado in lista_empleados_comision:
	print(empleado)