'''
Python nos permite leer y escribir datos en archivos externos. 
Podemos abrir archivos en diferentes modos, como lectura ("r"), escritura ("w") o anexar ("a"), y realizar operaciones de lectura y escritura.
'''

############ Lectura de archivos ############

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()


############ Escritura de archivos ############

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

        #! Es importante cerrar siempre los archivos después de utilizarlos para liberar los recursos del sistema. !#

''' También puedes utilizar la declaración with para manejar la apertura y cierre de archivos de manera automática. '''

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# En este caso, el archivo se abre utilizando la declaración with y se cierra automáticamente una vez que se sale del bloque with, incluso si ocurre una excepción.