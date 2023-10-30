
"""
NOTA_MINIMA = 1
NOTA_MAXIMA = 10

mensaje = f"¿Tu nota de examen (entre {NOTA_MINIMA} y {NOTA_MAXIMA})?"
nota = int(input(f"{mensaje} "))
while nota < NOTA_MINIMA or nota > NOTA_MAXIMA: 
    nota = int(input(f"ERROR. {mensaje} "))
print("Genial, su nota es válida...")
"""

for i in range(10):
    print(i,end=" ")
print()
for i in range(1,11):
    print(i,end=" ")
print()
for i in range(1,11,2):
    print(i,end=" ")