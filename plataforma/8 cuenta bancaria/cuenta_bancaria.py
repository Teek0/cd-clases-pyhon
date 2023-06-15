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
        print("total balance: "+str(self.balance)+"\ntasa de interés: "+str(self.tasa_interes)+"\n_______________")
        return self

    def generar_interes(self):
        print("usted ha obtenido {} por intereses".format(self.balance*self.tasa_interes))
        self.balance+=self.balance*self.tasa_interes
        return self
    @classmethod
    def mostrar_info_todas_las_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            print("******************")
            print(f"cuenta numero: {cls.todas_las_cuentas.index(cuenta)+1}")
            print(cuenta.balance)
            print(cuenta.tasa_interes)

cuenta1=CuentaBancaria(0.01,1000)
cuenta2=CuentaBancaria(0.02,500)
cuenta1.deposito(100).deposito(200).deposito(150).retiro(50).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(1000).deposito(2000).retiro(150).retiro(50).retiro(250).retiro(150).generar_interes().mostrar_info_cuenta()
CuentaBancaria.mostrar_info_todas_las_cuentas()