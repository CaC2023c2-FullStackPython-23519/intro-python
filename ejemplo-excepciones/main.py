from super_matematica import factorial

try:
    a = int(input("Colocá un número natural: "))
    b = int(input("Colocá otro número natural: "))
    print(f"El numero es {a/b}")
    print(f"El factorial de {a} es { factorial(a) }")
    print(f"El factorial de {b} es { factorial(b) }")
except ValueError as e:
    print("Se introdujo una cadena donde se esperaba un entero")
except ZeroDivisionError as e:
    print("Se quiso dividir por cero")
except Exception as e:
    print("ERROR:",e)