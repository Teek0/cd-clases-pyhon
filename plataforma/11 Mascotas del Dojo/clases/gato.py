from clases.mascota import Mascota

class Gato(Mascota):
    def __init__(self, name , tipo , golosinas , salud , energia, vidas=7):
        super().__init__(name , tipo , golosinas , salud , energia)
        self.vidas=vidas

    def cuantas_vidas_tiene_el_gato(self):
        print(f"{self.name} tiene {self.vidas} vidas")
        return self