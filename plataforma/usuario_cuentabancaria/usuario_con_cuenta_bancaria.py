class CuentaBancaria:
    todas_las_cuentas=[]
    def __init__(self, tasa_interes, balance=0): 
        self.balance=balance
        self.tasa_interes=tasa_interes
        CuentaBancaria.todas_las_cuentas.append(self)

    def deposito(self, amount):
        print("ud ha depositado "+str(amount))
        self.balance+=amount
        return self

    def retiro(self, amount):
        print("ud ha retirado "+str(amount))
        self.balance-=amount
        return self

    def mostrar_info_cuenta(self):
        print("total balance: "+str(self.balance)+"\ntasa de interés: "+str(self.tasa_interes)+"\n********************")
        return self

    def generar_interes(self):
        print("usted ha obtenido {} por intereses".format(self.balance*self.tasa_interes))
        self.balance+=self.balance*self.tasa_interes
        return self
    @classmethod
    def mostrar_info_todas_las_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            print("********************")
            print(f"cuenta numero: {cls.todas_las_cuentas.index(cuenta)+1}")
            print(cuenta.balance)
            print(cuenta.tasa_interes)

class Usuario:
    
    def __init__(self, name, email):
        
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(tasa_interes=0.02,balance=0)
        
    def hacer_deposito(self, amount):	
        self.cuenta.deposito(amount)
        return self	
    
    def hacer_retiro(self, amount):	
        self.cuenta.retiro(amount)
        return self

    def mostrar_balance_usuario(self):
        self.cuenta.mostrar_info_cuenta()

    def transfer_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)
        return self

vicente=Usuario("vicente","vicente@mail.com")
rodrigo=Usuario("rodrigo","rodrigo@mail.com")
nicole=Usuario("nicole","nicole@mail.com")

vicente.hacer_deposito(300).hacer_deposito(200).hacer_deposito(600).hacer_retiro(100).mostrar_balance_usuario()

rodrigo.hacer_deposito(300).hacer_deposito(200).hacer_retiro(100).hacer_retiro(150).mostrar_balance_usuario()

nicole.hacer_deposito(1000).hacer_retiro(100).hacer_retiro(200).hacer_retiro(300).mostrar_balance_usuario()

vicente.transfer_dinero(nicole,200).mostrar_balance_usuario()
nicole.mostrar_balance_usuario()