# Programa principal

#from nombre_del_modulo import lo_que_queres_del_modulo
from Persona import Persona
from TarjetaDeCredito import TarjetaDeCredito

juan = Persona("1234", "Juan", "Gomez", "23123", "juan@fake.com")
la_tarjeta = TarjetaDeCredito("Banco Fake", "1231233242345", juan)

print( juan.nombre_completo() )
print( la_tarjeta.titular.nombre_completo() )