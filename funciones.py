def saludo(nombre):
    print(f"¡Hola, {nombre}!")

saludo('Gabriel')

def suma(a, b):
    return a + b


resultado = suma(3, 4)
print(resultado)  # Imprime 7
print(suma(3,5))

#funcionaes lambda
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25


#alcance de las variables (local vs global)
def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función


variable_global = 20


def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar


funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
# print(variable_local)  # Genera un error, la variable no está definida en este alcance.

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura

print(area_rectangulo(3,5))

#### Funciones con número variable de argumentos
''' 
Python permite definir funciones que acepten un número variable de argumentos. Esto se logra utilizando el operador * antes del nombre del parámetro. 
'''
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22


# funcion -> isinstance(objeto, clase)
'''
La función isinstance() en Python se utiliza para verificar si un objeto es una instancia de una clase o de una subclase de esa clase. 
Es una forma común de comprobar el tipo de un objeto de manera segura y legible.
'''
numero = 10
texto = "Hola"

# Verificar si 'numero' es un entero
print(isinstance(numero, int))  # Imprime True

# Verificar si 'texto' es un string
print(isinstance(texto, str))  # Imprime True

# Verificar si 'numero' es un string
print(isinstance(numero, str))  # Imprime False


'''
Seguridad: isinstance() es más seguro que usar el operador type(). 
Con type(), tendrías que comparar con el tipo exacto, mientras que isinstance() también verifica las subclases. 
Esto es útil en la programación orientada a objetos.
'''

class Animal:
    pass

class Perro(Animal):
    pass

perro = Perro()
print(isinstance(perro, Animal))  # Imprime True, porque Perro es una subclase de Animal
