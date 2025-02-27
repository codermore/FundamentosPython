############ For ############

'''
El bucle for se utiliza para iterar sobre una secuencia (como una lista, una tupla o una cadena) o cualquier objeto iterable. 
La sintaxis básica es la siguiente:
'''
def instrucciones (string, variable):
    print(string, variable)
    return

secuencia = [1,2,3]
for variable in secuencia:

    # Bloque de código a repetir
    instrucciones("variable en secuencia:", variable)


' Otro ejemplo '

frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    instrucciones("Fruta en interacion:", fruta)



############ While ############
'''
El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera. 
La sintaxis básica es la siguiente:
'''


condicion = True

while condicion:

    # Bloque de código a repetir
    instrucciones('while condicion =', condicion)
    condicion = False



############ Control de Bucles: Break ############
'''
La instrucción break se utiliza para salir prematuramente de un bucle, independientemente de la condición. 
Cuando se encuentra un break, el bucle se detiene y el flujo de ejecución continúa con la siguiente instrucción fuera del bucle.
'''

contador = 0
while True:

    print("break:",contador)
    contador += 1


    if contador == 5:
        break

############ Control de Bucles: Continue ############
'''
La instrucción continue se utiliza para saltar el resto del bloque de código dentro de un bucle y pasar a la siguiente iteración.
'''

for i in range(10):

    if (i%2 == 0):
        continue
    
    instrucciones("Numero impares only:", i)


'''
En este ejemplo, el bucle for itera sobre los números del 0 al 9 utilizando la función range(). 
Dentro del bucle, se verifica si el número es divisible por 2 utilizando el operador de módulo %. 
Si el número es divisible por 2 (es decir, si es par), se ejecuta la instrucción continue, 
lo que hace que se salte el resto del bloque de código y se pase a la siguiente iteración del bucle. 
Como resultado, solo se imprimirán los números impares.
'''

############ Control de Bucles: Pass ############
'''
La instrucción pass es una operación nula que no hace nada. 
Se utiliza como marcador de posición cuando se requiere una instrucción sintácticamente, pero no se desea realizar ninguna acción.
'''

for i in range(5):
    pass
    

'''
En este ejemplo, el bucle for itera sobre los números del 0 al 4, pero no se realiza ninguna acción dentro del bucle debido a la instrucción pass. 
Esto puede ser útil cuando se está desarrollando un programa y se desea reservar un bloque de código para implementarlo más adelante.
'''

for i in range (1,7):
    print(i)
