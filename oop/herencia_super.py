class Persona():
    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre=nombre
        self.edad=edad
        self.lugarResidencia=lugarResidencia
    
    def imprimirDescripcion(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nLugar de residencia:", self.lugarResidencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        #super llama al metodo de la clase padre
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad

    def imprimirDescripcion(self):
        super().imprimirDescripcion()
        print("Salario:", self.salario, "\nAntiguedad: ", self.antiguedad)




Antonio = Empleado(1500, 55, "Antonio", 78, "Francia")

Antonio.imprimirDescripcion()

print("Antonio es un/a persona?: ", isinstance(Antonio, Persona))
print("Antonio es un/a empleado?: ", isinstance(Antonio, Empleado))

Juana = Persona("Juana", 29, "Argentina")

print("Juana es un/a persona?: ", isinstance(Juana, Persona))
print("Juana es un/a empleado?: ", isinstance(Juana, Empleado))
