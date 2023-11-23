from Bicicleta import Bicicleta

class Bicicleta_Electrica(Bicicleta):

    def __init__(self, marca, tiene_canasto, color, motor, bateria):
        Bicicleta.__init__(self, marca, tiene_canasto, color)
        self.__motor = motor
        self.__bateria = bateria

    def cumple_requisitos(self):
        return self.motor == "Super"