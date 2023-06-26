class Ninja:
    def __init__( self, nombre, apellido, mascota , premios, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premios = premios
        self.comida_mascota = comida_mascota

    def caminar(self,Mascota):
        print(f"Saliste a caminar con {Mascota.name}")
        Mascota.jugar()        
        return self

    def alimentar(self, Mascota):
        print(f"Empezaste a alimentar a {Mascota.name}")
        Mascota.comer()
        return self

    def bañar(self, Mascota):
        print(f"Empezaste a bañar a {Mascota.name}")
        Mascota.sonido()
        return self