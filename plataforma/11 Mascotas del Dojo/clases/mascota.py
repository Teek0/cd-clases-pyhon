class Mascota:
    def __init__( self, name , tipo , golosinas , salud , energia ):
        self.name=name
        self.tipo=tipo
        self.golosinas=golosinas
        self.salud=salud
        self.energia=energia

    def dormir(self):
        print(f"{self.name} se ha dormido. Los puntos de energía de tu mascota han aumentado en +25. Ahora tiene {self.energia}!")
        return self

    def comer(self):
        self.energia+=5
        self.salud+=10
        print(f"Has aumentado los puntos de energía de tu mascota en +5! Ahora tiene {self.energia}!")
        print(f"Has aumentado los puntos de salud de tu mascota en +10! Ahora tiene {self.salud}!")
        return self

    def jugar(self):
        self.salud+=5
        print(f"Has aumentado los puntos de salud de tu mascota en +5! Ahora tiene {self.salud}!")
        return self

    def sonido(self):
        if(self.tipo=="Perro"):
            print(f"Tu mascota te ha ladrado en agradecimiento!")
        elif(self.tipo=="Gato"):
            print(f"Tu mascota ha maullado enojado!")
        else:
            print("Tu mascota ha gemido de una forma muy extraña!")
        return self