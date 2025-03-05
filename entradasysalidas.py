############ Entrada de datos del usuario ############
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

'''
La función input() siempre devuelve una cadena de texto. 
Si deseas trabajar con otros tipos de datos, como números enteros o flotantes, debes realizar una conversión explícita utilizando funciones como int() o float().
'''

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


############ Salida de datos ############
'''
Para mostrar información en la pantalla, utilizamos la función print(). Esta función toma uno o más argumentos y los muestra en la consola.
Podemos utilizar la f-string (formateo de cadenas) para incrustar variables directamente dentro de una cadena de texto.
'''

nombre = "Juan"
edad = 25

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")