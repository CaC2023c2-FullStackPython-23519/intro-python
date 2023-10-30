llueve = True
if llueve:
    print("Usar paraguas")

edad = 14
EDAD_LEGAL = 18

if edad >= EDAD_LEGAL:
    print("Pasa")
    # otra cosa...
else:
    print("No pasa")
print("Adiós, gracias por usar el software")

numeroMarcadoEnTelefono = 6
match numeroMarcadoEnTelefono:
    case 1:
        print("Ventas")
    case 2:
        print("RRHH")
    case _:
        print("Error")

num = 5
if num != 0:
    if num > 0:
        print("Positivo")
    else: 
        print("Negativo")
else: 
    print("Neutro")

if num == 0:
    print("Neutro")
elif num > 0:
    print("Positivo")
else:
    print("Negativo")