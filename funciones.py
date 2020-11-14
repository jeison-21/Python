def miFunsion():
    print('Mi Primera Funcion')

miFunsion()

def imprimirDato(*nombre):
    print('El Nombre Completo es: ',nombre)
imprimirDato('chanchitofeliz','feliz','lala','lele')

def nombeCompleto(apellido, nombre):
    print(nombre,apellido)

nombeCompleto(nombre='chanchito',apellido='feliz')

def nombeCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

nombeCompleto2(nombre='chanchito',apellido='feliz')