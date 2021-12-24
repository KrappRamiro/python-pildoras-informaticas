class Coche():
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False

    def arrancar(self, arrancamos):
        self.__enMarcha=arrancamos

        if (self.__enMarcha):
            checkeo = self.__checkCarStatus()
        if (self.__enMarcha and checkeo):
            return("Todo ok! Arrancando auto")
        elif (self.__enMarcha and checkeo == False):
            return "Hubo un problema en el auto, revisa el panel"
        else:
            return("Apagando auto")

    def printInfo(self):
        print("Caracteristicas del coche:",
                "\nLargo del chasis: ", self.__largoChasis,
                "\nAncho del chasis: ", self.__anchoChasis,
                "\nCantidad de ruedas: ", self.__ruedas,
                "\nAuto en marcha: ", self.__enMarcha)

    def __checkCarStatus(self):
        print("Realizando checkeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.printInfo()
