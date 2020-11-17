#MULTIPLICAR DOS NUMEROS SIN USAR EL SIMBOLO DE MULTIPLICACION
a = 8 
b = 4 
resultado = 0 
for x in range(b):
    resultado += a
print(resultado)

#ingresar nombre apellido y imprimirlo alreves
nombre = 'jeison'
apellido = ' fallas'
concatenacion = nombre + ' ' +apellido

print(concatenacion[::-1])

#encontrar el menor de una lista
lista = [1, 2, 5, 3, -24, -13]
menor = 'init'
for x in lista:
    if menor =='init':
        #primera iteracion
        menor = x
    else:
        menor = x if x < menor else menor
        #quiero que menor sea x siempre y cuando x sea menor que la variable de menor 
print('menor ', menor)


#escribir una funcion que devuelva el valor de una espera por su radio
#4/3 * pt + r ** 3

def calcularVolumen(r):
    return 4/3 * 3.14 * r ** 3

resultado =calcularVolumen(6)
print(resultado)

#escribir una funcion que indique si el  usuario es mayor
def esMayor(usuario):
    return usuario.edad >17
class Usuario:
    def __init__(self, edad):
        self.edad = edad
usuario = Usuario(15)
usuario2 = Usuario(20)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1,resultado2)

#costruir una funcion que indique si un numero es par o impar
def esPar(n):
    return n % 2 == 0
resultado3 = esPar(11)
resultado4 = esPar(10)
resultado5 = (resultado3 + resultado4)
print (resultado5)

#funcion que derermine cuantas vocales tiene una palabra
palabra='chancHItofEliz'
vocales = 0
for x in palabra:
    y= x.lower()

    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0
print(vocales) 

#escribir una  aplicacion que reciba una cantidad infinita de numeros hasta decir basta,
#luejo que reetorne la suma de los numeros ingresados
#lista = []
#print('ingrese numeros y para salir escriba "basta"')
#while True:
#    valor =  input ('ingrese un valor:')
#    if valor == 'basta':
#        break
#    else:
#        try:
#            valor = int(valor)
#            lista.append(valor)
#        except:
#            print('Dato Ingresado Invalido')
#            exit()

#resultado6=0
#for x in lista:
#    resultado6 += x
#print(resultado6)
    

#escriba una funcion que reciba nombre y apellido y valla agregando a un  archivo
def agregarNombreArchivo(nombre,apellido):
    c = open('nombrecompleto.txt','a')
    c.write(nombre+' '+apellido+'\n')
    c.close

agregarNombreArchivo('jeison','fallas')

