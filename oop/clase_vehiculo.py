import time

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha, self.acelera, self.frena = False, False, False
    
    def arrancar(self):
        self.enMarcha=True
        print("Arrancando!")
    
    def acelerar(self):
        self.acelera=True
        print("Acelerando!")
    
    def frenar(self):
        self.frena=True
        print("Frenando!")
    
    def imprimirEstado(self):
        print("\n-----------------\nCaracteristicas del coche:",
                "\nMarca: ",        self.marca,
                "\nModelo: ",       self.modelo,
                "\nEn marcha: ",    self.enMarcha,
                "\nAcelerando: ",   self.acelera,
                "\nFrenando: ",     self.frena,
                "\n-----------------\n")

class Moto(Vehiculos): #Ahora, la clase Moto hereda de la clase vehiculo
    hcaballito=""
    def caballito(self):
        self.hcaballito="voy haciendo el caballito"
    def imprimirEstado(self):
        print("\n-----------------\nCaracteristicas del coche:",
                "\nMarca: ",        self.marca,
                "\nModelo: ",       self.modelo,
                "\nEn marcha: ",    self.enMarcha,
                "\nAcelerando: ",   self.acelera,
                "\nFrenando: ",     self.frena,
                "\nCaballito: ",    self.hcaballito,
                "\n-----------------\n")

class Cuatrimotor(Moto): # Vehiculo --> Moto --> Cuatrimotor
    pass

class Furgoneta(Vehiculos): # Vehiculo -> Furgoneta
    def carga(self, carga):
        self.cargado=carga
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class V_electricos():
    def __init__(self):
        self.autonomiaKM=100
        self.bateria = 20
    def cargarEnergia(self, carga=0):
        self.cargando=True
        self.bateria+=carga
    def imprimirEstado(self):
        print("\n-----------------\nCaracteristicas del coche:",
                "\nAutonomia en KM: ",      self.autonomiaKM,
                "\nCarga de la bateria: ",  self.bateria)



class biciElectrica(V_electricos, Vehiculos): #clase que hereda de dos clases
#cuando hay herencia, siempre se da preferencia a la primera clase
# osea, si python tiene un constructor en V_electricos y en Vehiculos, 
# va a elegir al constructor de V_electricos porque esta primero
    pass


miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.imprimirEstado()

miFurgoneta = Furgoneta ("Renault" , "Kangoo") 

miFurgoneta.arrancar()
miFurgoneta.imprimirEstado()
print(miFurgoneta.carga(True))



