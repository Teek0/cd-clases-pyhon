# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))
# import random
# print(random.randint(2,5)) # proporciona un número aleatorio entre 2 y 5

# print("Mi numero favorito es", 31)

# name = "Zen"
# print("Mi nombre es " + name) #no se puede usar + para concatenar un número

# #print("Hola " + 42)			# salida: TypeError
# print("Hola " + str(42))		# salida: Hola 42

#interpolacion de cadenas
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"Mi nombre es {first_name} {last_name} y tengo {age} años de edad.")

# #string.format()
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("Mi nombre es {} {} y tengo {} años de edad.".format(first_name, last_name, age))
# # salida: Mi nombres es Zen Coder y tengo 27 años de edad.
# print("Mi nombre es {} {} y tengo {} años de edad.".format(age, first_name, last_name))
# # salida: Mi nombre es 27 Zen y tengo Coder años de edad.

# #%-formatting   -------  %s para una cadena y %d para un número
# hw = "Hola %s" % "mundo" 	# con valores literales
# py = "Me encanta Python %d" % 3 
# print(hw, py)
# # salida: Hola mundo Me encanta Python 3
# name = "Zen"
# age = 27
# print("Mi nombre es %s y tengo %d" % (name, age))		# o con variables
# # salida: Mi nombre es Zen y tengo 27

# x = "hola mundo"
# print(x.title())
# # salida: "Hola Mundo"

capitales = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# otra forma de iterar a través de las claves
for key in capitales.keys():
     print(key)
# salida: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# para iterar a través de los valores
for val in capitales.values():
     print(val)
# salida: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# para iterar a través de las claves y valores
for key, val in capitales.items():
     print(key, " = ", val)
# salida: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

