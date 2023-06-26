class CuentaBancaria:
    todas_las_cuentas = []

    def __init__(self, tasa_interes, balance=0):
        self.balance = balance
        self.tasa_interes = tasa_interes
        CuentaBancaria.todas_las_cuentas.append(self)

    def deposito(self, amount):
        print("Usted ha depositado " + str(amount))
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance >= amount:
            print("Usted ha retirado " + str(amount))
            self.balance -= amount
        else:
            print("Saldo insuficiente para realizar el retiro.")
        return self

    def mostrar_info_cuenta(self):
        print("Total balance: " + str(self.balance) + "\nTasa de interés: " + str(self.tasa_interes))
        print("********************")
        return self

    def generar_interes(self):
        interes = self.balance * self.tasa_interes
        self.balance += interes
        print("Usted ha obtenido {} por intereses".format(interes))
        print("********************")
        return self

    @classmethod
    def mostrar_info_todas_las_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            print(f"Cuenta número: {cls.todas_las_cuentas.index(cuenta) + 1}")
            print("Balance:", cuenta.balance)
            print("Tasa de interés:", cuenta.tasa_interes)
            print("********************")


class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuentas = []

    def crear_cuenta(self, tasa_interes, balance=0):
        nueva_cuenta = CuentaBancaria(tasa_interes, balance)
        self.cuentas.append(nueva_cuenta)
        return self

    def hacer_deposito(self, num_cuenta, amount):
        cuenta = self.cuentas[num_cuenta - 1]
        cuenta.deposito(amount)
        return self

    def hacer_retiro(self, num_cuenta, amount):
        cuenta = self.cuentas[num_cuenta - 1]
        cuenta.retiro(amount)
        return self

    def mostrar_balance_usuario(self, num_cuenta):
        print(f"Cuenta {num_cuenta} de {self.name}")
        cuenta = self.cuentas[num_cuenta - 1]
        cuenta.mostrar_info_cuenta()

    def transfer_dinero(self, num_cuenta_origen, destino, num_cuenta_destino, amount):
        cuenta_origen = self.cuentas[num_cuenta_origen - 1]
        cuenta_destino = destino.cuentas[num_cuenta_destino - 1]
        cuenta_origen.retiro(amount)
        print(f"desde la cuenta {num_cuenta_origen} de {self.name}")
        cuenta_destino.deposito(amount)
        print(f"a la cuenta {num_cuenta_destino} de {destino.name}")
        print("********************")
        return self

    def mostrar_cuentas(self):
        for cuenta in self.cuentas:
            print(self.cuentas.index(cuenta)+1)
        return self

vicente = Usuario("vicente", "vicente@mail.com")
rodrigo = Usuario("rodrigo", "rodrigo@mail.com")
nicole = Usuario("nicole", "nicole@mail.com")

cuenta_vicente_1 = vicente.crear_cuenta(tasa_interes=0.02, balance=0)
cuenta_vicente_2 = vicente.crear_cuenta(tasa_interes=0.03, balance=500)

cuenta_rodrigo_1 = rodrigo.crear_cuenta(tasa_interes=0.01, balance=1000)

cuenta_nicole_1 = nicole.crear_cuenta(tasa_interes=0.02, balance=200)


vicente.hacer_deposito(1, 300).hacer_deposito(1, 200).hacer_deposito(1,600).hacer_retiro(1, 100).mostrar_balance_usuario(1)
vicente.hacer_deposito(2, 1000).hacer_retiro(2, 200).mostrar_balance_usuario(2)

rodrigo.hacer_deposito(1, 300).hacer_deposito(1, 200).hacer_retiro(1,100).hacer_retiro(1, 150).mostrar_balance_usuario(1)

nicole.hacer_deposito(1, 1000).hacer_retiro(1, 100).hacer_retiro(1,200).hacer_retiro(1, 300).mostrar_balance_usuario(1)

vicente.transfer_dinero(1, vicente, 2, 200).mostrar_balance_usuario(1)
vicente.mostrar_balance_usuario(2)

vicente.transfer_dinero(1, nicole, 1, 200).mostrar_balance_usuario(1)
nicole.mostrar_balance_usuario(1)