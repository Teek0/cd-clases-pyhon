#1

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
print("*********************")
print(x)
x[1][0]=15
print(x)
print("*********************")
print(estudiantes)
estudiantes[0]['last_name']='Bryant'
print(estudiantes)
print("*********************")
print(directorio_deportes)
directorio_deportes['fútbol'][0]='Andrés'
print(directorio_deportes)
print("*********************")
print(z)
z[0]['y']=30
print(z)
print("*********************")


#2

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range(0,len(some_list)):
        for key in some_list[i]:
            print(key,"-", some_list[i][key])

iterateDictionary(estudiantes)
print("*********************")

def iterateDictionaryB(some_list):
    lista=[]
    for key in some_list[0]:
        lista.append(key)
    for i in range(0,len(some_list)):
        print(lista[0],"-",some_list[i][lista[0]],", ",lista[1],"-",some_list[i][lista[1]])

iterateDictionaryB(estudiantes)
print("*********************")

#3

def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name', estudiantes)
print("*********************")
iterateDictionary2('last_name', estudiantes)
print("*********************")

#4

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(key, len(some_dict[key]))
        for value in some_dict[key]:
            print(value)
        print("----")

printInfo(dojo)