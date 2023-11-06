# DEFINICIÓN DE LAS FUNCIONES

def siguiente(n):
    return n + 1

def doble(n):
    return n * 2

def es_vocal(letra):
    return letra in "AEIOUaeiou"

# PROGRAMA PRINCIPAL
el_siguiente_de_5 = siguiente(5)
el_doble = doble(el_siguiente_de_5)
print(el_doble)
print( doble(siguiente(5)) )
print( es_vocal('a') )
print( es_vocal('A') )
print( es_vocal('B') )