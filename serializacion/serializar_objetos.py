import pickle
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

persona1=Persona("Juan", "23", "Espana")
persona2=Persona("Ramiro", "17", "Argentina")
persona3=Persona("Pedro", "90", "Peru")

personas = [persona1, persona2, persona3]

miFichero = open("lasPersonas", "wb")
pickle.dump(personas, miFichero)
miFichero.close()
del(miFichero) #deletea de la memoria

ficheroApertura=open("lasPersonas", "rb")
misPersonas = pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misPersonas:
    print(c.imprimirDescripcion())
    print("---")