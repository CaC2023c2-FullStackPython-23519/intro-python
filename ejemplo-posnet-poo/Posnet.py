class Posnet:

    def efectuar_pago(self, tarjeta, monto, cant_cuotas):
        el_ticket = None
        if (datos_validos(tarjeta, monto, cant_cuotas)):
            monto_total = monto + monto * recargo_segun_cuotas(cant_cuotas)
            #if ( tarjeta.saldo >= monto_total ):
            if ( tarjeta.saldo_suficiente(monto_total) ):
                

        
        return el_ticket
    
    def datos_validos(self, tarjeta, monto, cant_cuotas):
        # Pendiente...

    def recargo_segun_cuotas(cant_cuotas):
        # Pendiente...