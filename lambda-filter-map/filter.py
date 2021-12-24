'''
def es_par(num):
	return num%2==0
'''
numeros=[1,2,3,4,5,6,7,8]
print(list(filter(lambda num:num%2==0, numeros)))


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

salario_superior_to_50k=filter(lambda empleado:empleado.salario>50000, lista_empleados)

for empleado_salario in salario_superior_to_50k:
	print(empleado_salario)