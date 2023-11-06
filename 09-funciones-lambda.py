"""
    def doble(n):
        return n * 2
"""

lista = [1,2,3,4]
nombres = ["juan", "pedro", "maria"]

print( list(map( lambda x : x * 2 , lista)) )
print( list(map( lambda nom : nom.upper() , nombres)) )