"""
    El usuario ingresa su año de nacimiento, la máquina muestra cuál es su edad (aproximada)
"""

anio_actual = 2023

# Entrada
anio_de_nacimiento = int(input("¿En qué año naciste? "))

# Proceso
edad = anio_actual - anio_de_nacimiento

# Salida
# Concatenar con varios argumentos en el print
print("Tu edad es",edad,"ó",(edad-1),"años")
# Concatenar usando el + (todos deben ser de tipo string)
print("Tu edad es " + str(edad) + " ó " + str(edad-1) + " años")
# Concatenar interpolación de strings (f-string)
print(f"Tu edad es {edad} ó {edad-1} años")