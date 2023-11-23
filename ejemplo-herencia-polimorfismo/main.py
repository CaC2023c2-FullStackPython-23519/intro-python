from Bicicleta import Bicicleta
from Bicicleta_Electrica import Bicicleta_Electrica

una_bici = Bicicleta("Acme", True, "Rojo")
otra_bici = Bicicleta_Electrica("Super", False, "Azul", "12312312345", "bateria super")

taller = [una_bici, otra_bici, bici2, bici3, bici4]

for bici in taller:
    if bici.cumple_requisitos():
        print(bici)