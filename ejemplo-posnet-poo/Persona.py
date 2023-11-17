class Persona:

    def __init__(self, DNI, nombre, apellido, telefono, mail):
        self.__DNI = DNI
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__mail = mail

    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self, nuevo_telefono):
        if nuevo_telefono != "":
            self.__telefono = nuevo_telefono
        
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"