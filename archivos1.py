import os

if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
else:
    print("El Archivo no exste")
#eliminamos carpetas
#os.rmdir(chanchito)
