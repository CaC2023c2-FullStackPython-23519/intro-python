class Bicicleta:

    def __init__(self, marca, tiene_canasto, color):
        self.__marca = marca
        self.__tiene_canasto = tiene_canasto
        self.__color = color

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color

    def cumple_requisitos(self):
        return self.kms < 300