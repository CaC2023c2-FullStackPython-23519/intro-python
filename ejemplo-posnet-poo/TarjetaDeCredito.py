class TarjetaDeCredito:
    
    def __init__(self, entidad_bancaria, numero, titular):
        self.__entidad_bancaria = entidad_bancaria
        self.__numero = numero
        self.__saldo = 0
        self.__titular = titular

    def descontar_saldo(self, cuanto):
        if (cuanto > 0 and self.saldo_suficiente(cuanto)):
            self.__saldo -= cuanto

    def recargar_saldo(self, cuanto):
        self.__saldo += cuanto

    def saldo_suficiente(self, monto):
        return self.__saldo >= monto
    
    def nombre_completo_del_titular(self):
        return self.__titular.nombre_completo()