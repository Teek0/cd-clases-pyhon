edad=25
nombre="Nicole"
apellido='saez'

resultado=f"hola como estas {nombre} {apellido}. ¡Hoy cumples {edad} años!"
resultado2="hola como estas "+nombre+" "+apellido+". ¡Hoy cumples "+str(edad)+" años!"
resultado3="hola como estas {} {}. ¡Hoy cumples {} años!".format(nombre,apellido,edad)
print(resultado)
print(resultado2)
print(resultado3)

print( nombre.upper(), len( nombre ) )