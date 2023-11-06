# Definición de funciones
def es_multiplo(a, b):
    return a % b == 0

def cant_divisores(num):
    cantDiv = 1
    for i in range(2,num + 1):
        if es_multiplo(num, i):
            cantDiv += 1 # cantDiv = cantDiv + 1
    return cantDiv

def es_primo(num):
    return cant_divisores(num) == 2
    
# Programa principal
numero = int(input("Ingrese un entero:"))
print("El número ",end="")
if not es_primo(numero):
    print("NO ",end="")
print("es PRIMO")