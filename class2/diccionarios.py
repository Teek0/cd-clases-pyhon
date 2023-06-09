#DICCIONARIOS

"""js
let estudiante={
nombre:"Alex",
apellido:"Gonzalez",
edad: 25
};
console.log(estudiante.nombre);"""

estudiante={
    'nombre':'Alex',
    'apellido':'Gonzalez',
    'edad': 25,
    'diplomas': ['Yelow Belt', 'Black Belt']
}

print(estudiante['apellido'])

estudiante['nombre']='Alejandro'

print(estudiante)

estudiante['calificacion'] = 9.7
estudiante.pop('edad')

print(estudiante)
print(estudiante['diplomas'][1])