class Persona:
    def __init__(self, nombre, apellido, numero, club):
        self.nombre = nombre # Atributos de instancia
        self.apellido = apellido
        self.numero = numero
        self.club = club

    def saludar(self):
        print(f"Hola soy {self.nombre_completo()} y juego en {self.club.nombre}")

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"nombre: {self.nombre}, apellido: {self.apellido}"

class ClubDeFutbol:
    def __init__(self, nombre, color_camiseta):
        self.nombre = nombre
        self.color_camiseta = color_camiseta


# Test de la clase Persona

inter_de_miami = ClubDeFutbol("Inter de Miami", "Rosa")
benfica = ClubDeFutbol("Benfica", "Rojo")
leo = Persona("Lionel", "Messi", 10, inter_de_miami)
fideo = Persona("Angel", "Di María", 7, benfica)
otamendi = Persona("Nicolás", "Otamendi", 2, benfica)

leo.saludar()
fideo.saludar()
otamendi.saludar()

benfica.nombre = "El Inter de Portugal"

leo.saludar()
fideo.saludar()
otamendi.saludar()

#print(leo)
#print(fideo)