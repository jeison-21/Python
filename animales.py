
class Animal:
    def __init__(self,  nombre, anotopeya):
        self.nombre = nombre
        self.anotopeya = anotopeya
    def saludo(self):
        print('Hola, soy un ',self.tipo, 'y mi sonido es el', self.anotopeya)


class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre , anotopeya):
        Animal.__init__(self,nombre,anotopeya)
        print('hola soy un texo extendido')


class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, anotopeya):
        super().__init__(nombre,anotopeya)
        print('istanciando un perro')
class Canario(Animal):
    tipo = 'canario'

gato = Gato('Floffy', 'maullido')
gato.saludo()

perro = Perro('firulanis', 'ladrido')
perro.saludo()

canario = Canario ('Piolin','Silvido')
canario.saludo()