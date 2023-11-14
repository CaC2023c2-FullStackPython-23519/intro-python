class Persona:

    def __init__(self, DNI, nombre, apellido, telefono, mail):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"