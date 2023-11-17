# importar la clase Ticket

class Posnet:

    def efectuar_pago(self, tarjeta, monto, cant_cuotas):
        el_ticket = None
        if (self.datos_validos(tarjeta, monto, cant_cuotas)):
            monto_total = monto + monto * self.recargo_segun_cuotas(cant_cuotas)
            if ( tarjeta.saldo_suficiente(monto_total) ):
                tarjeta.descontar_saldo(monto_total)
                el_ticket = Ticket(tarjeta.nombre_completo_del_titular(), monto, monto / cant_cuotas) # Hay que que completar la clase Ticket
        return el_ticket
    
    def datos_validos(self, tarjeta, monto, cant_cuotas):
        # Validar la tarjeta...
        return monto > 0 and cant_cuotas <= 6 and cant_cuotas >= 1

    def recargo_segun_cuotas(cant_cuotas):
        return (cant_cuotas - 1) * 0.03