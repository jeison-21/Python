c = open('chanchito.txt','w')
#con el for se puede manipula linia p[or linea ] |
#for x in c:
#    print(x)
c.write('\naqui agregamos una nueva linea')

#cerrar la consulta
c.close()

x = open('chanchito.txt')
print (x.read())