#clase
class Fraccion:
    #constructor
    def __init__(self,numerador=1,denominador=1): #puedo asignarle valores por defecto
        #asignamos los -atributos de instancia- que estarán disponibles en toda la clase
        self.numerador=numerador
        self.denominador=denominador
        self.mensaje="Esta es una fracción"
    #metodos de instancia
    def imprimir(self):
        print(f"{self.numerador}/{self.denominador}")
        return self
    
    def suma (self, fraccion_adicional):
        num_resultante=(self.numerador*fraccion_adicional.denominador+fraccion_adicional.numerador*self.denominador)
        den_resultante=(self.denominador*fraccion_adicional.denominador)
        resultado = Fraccion(num_resultante,den_resultante)
        return resultado
    
    def imprime_hola(self):
        print("Hola")
        return self


fraccion_uno=Fraccion(1,2)
print(fraccion_uno)
print(fraccion_uno.numerador)
print(fraccion_uno.denominador)
print(fraccion_uno.mensaje)

fraccion_uno.mensaje="Estamos aprendiendo POO"
print(f"{fraccion_uno.mensaje} superduper",20)

print("*---------------------*")
fraccion_uno.imprimir()
print("+")
fraccion_dos=Fraccion(3,4)
fraccion_dos.imprimir()
fraccion_resultante=fraccion_uno.suma(fraccion_dos)
fraccion_resultante.imprimir()
print("*---------------------*")

fraccion_uno.imprimir().imprime_hola().suma(fraccion_dos)