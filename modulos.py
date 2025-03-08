############ Importacion y creaccion de modulos ############
'''
Python viene con una amplia biblioteca estándar de módulos que proporcionan funcionalidades adicionales. 
Estos módulos están disponibles sin necesidad de instalarlos por separado.
'''

############ Importacion de modulos ############

import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

'''
En este ejemplo, se importa el módulo math utilizando la declaración import. 
Luego, se utiliza la función sqrt() del módulo math para calcular la raíz cuadrada de 25.
'''

    #! También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función. !#

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0


############ Funciones y clases de modulos estandar ############

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10

fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual


############ Creacion de modulos ############
'''

#mi_modulo.py <--- archivo
def saludar(nombre):
    print(f"Hola, {nombre}!")


def calcular_suma(a, b):
    return a + b
'''

import mi_modulo 

mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8
