def dividir(num, deno):
    if deno == 0:
        deno = 1
    return num / deno

def saludar(nombre = "desconocido"):
    print(f"Hola {nombre}")

def saludar_entusiasmado(nombre, el_entusiasmo = "!!!"):
    print(f"Hola {nombre} {el_entusiasmo}")

# Programa principal
print( dividir(80,20) )
print( dividir(80,19) )
print( dividir(80,0) )

saludar("Juan")
saludar("María")
saludar()

saludar_entusiasmado("Pedro")
saludar_entusiasmado("Pedro", ":D:D:D:D:D:D:D")