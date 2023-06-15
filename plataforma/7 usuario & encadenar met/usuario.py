class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    
    def hacer_deposito(self, amount):	
        self.balance_cuenta += amount
        return self	
    
    def hacer_retiro(self, amount):	
        self.balance_cuenta -= amount
        return self

    def mostrar_balance_usuario(self):
        print(self.balance_cuenta)

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

print("*--------*")
vicente.transfer_dinero(nicole,200).mostrar_balance_usuario()
nicole.mostrar_balance_usuario()