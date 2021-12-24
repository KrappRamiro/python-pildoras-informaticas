class Coche():
    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo usando 6 ruedas")

# Version ineficiente:
## miVehiculo = Moto()
## miVehiculo.desplazamiento()
## 
## miVehiculo2 = Coche()
## miVehiculo2.desplazamiento()
## 
## miVehiculo3 = Camion()
## miVehiculo3.desplazamiento()

# Version eficiente de polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)
