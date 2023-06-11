'''
Básico: imprime todos los números enteros del 0 al 150.
Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. 
Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 
'''

for num in range(151):
    print(num)

for num in range(0,1001,5):
    print(num)

for num in range(0,101):
    if (num%5==0 and num%2==0):
        print("Coding Dojo")
    elif (num%5==0):
        print("Coding")
    else:
        print(num)

suma=0
for num in range(0,500001):
    if(num%2!=0):
        suma+=num
        print(num)
print(suma)

for num in range(2018,-1,-4):
    print(num)

lowNum=2
highNum=9
mult=3

for num in range(lowNum,highNum+1):
    if (num%mult==0):
        print(num)
