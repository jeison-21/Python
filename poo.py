class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def saludo(self):
        print('Hola, Mi nombre es ', self.nombre, self.apellido)
class admin(Usuario):
    def supersaludo(self):
        print('Hola, Me llamo, ', self.nombre, 'y soy  el administrador')

usuario = Usuario('felipe' , 'feliz')
usuario.nombre = 'chanchito'

usuario.saludo()

#del usuario.nombre
#print(usuario)

admin = admin('super','feliz')
admin.saludo()
admin.supersaludo()

