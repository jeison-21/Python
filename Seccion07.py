'''dato = input ('Ingresse datos: ')
#print(dato)
lista=['holo','mundo','chanchito','feliz','dragrones']

if lista.count(dato) > 0:
    print('el dato  existe: ',dato)
else:
    print('el dato no existe: ',dato)
'''

primero = input('ingrese el primer numero: ')
try:
    primero = int(primero)
except:
    primero = 'chanchito felix'
if primero == 'chanchito felix':
    print('El Valor Ingresado No Es Un Entero')
    exit()
segundo = input('ingrese el segndo numero ')
try:
    segundo = int(segundo)
except:
    segundo = 'chanchito felix'
if segundo == 'chanchito felix':
    print('El Valor Ingresado No Es Un Entero')
    exit()

simbolo = input('ingrese Operacion: ')

if simbolo == '+':
    print('suma', primero+segundo)
elif simbolo == '-':
    print(primero-segundo)
elif simbolo == '*':
    print(primero*segundo)
elif simbolo == '/':
    print(primero/segundo)
else:
    print('El Simboloo Ingresaado No Es Valido')
'''primernumero = int(primero)
segundonumero = int(segundo)
print(primernumero+segundonumero)'''
