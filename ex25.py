class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # privado

    def depositar(self, valor):
        self.__saldo += valor
        print("Depósito realizado.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado.")
        else:
            print("Saldo insuficiente.")

    def ver_saldo(self):
        print(f"Saldo atual: {self.__saldo}")

conta1 = ContaBancaria("Lucas", 1000)
conta1.depositar(200)
conta1.sacar(300)
conta1.ver_saldo()


