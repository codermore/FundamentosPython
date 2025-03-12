############ TUPLAS ############
'''
Una tupla es una estructura de datos inmutable y ordenada que permite almacenar una colección de elementos. 
Los elementos de una tupla se encierran entre paréntesis (), separados por comas
'''

punto = (3, 4)

print(punto[0])  # Imprime 3
print(punto[1])  # Imprime 4

'''
A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas. 
No se pueden agregar, eliminar o cambiar elementos en una tupla existente.
Las tuplas son útiles cuando necesitas almacenar una colección de elementos que no deben modificarse, como coordenadas o datos de configuración.

# Métodos de tuplas 

Aunque las tuplas son inmutables, Python proporciona varios métodos útiles para trabajar con ellas:

count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 
index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.
'''

mi_tupla = (1, 2, 3, 2, 4, 2)
# pos ->    0  1  2  3  4  5

# tupla.index(valor, inicio, fin)
print (mi_tupla.index(2))   # Salida: 1
print (mi_tupla.index(2, 2))   #Salida: 3
print (mi_tupla.index(2, 3, 5))   #Salida: 3


'''
    Otro ejemplo
'''
canasto_de_frutas = ('manzana', 'banana', 'cereza', 'durazno', 'banana')
canasto_de_frutas_total = len(canasto_de_frutas)
indice = canasto_de_frutas.index('banana', 0)  # Busca 'banana' empezando desde el índice 0
bananas_total = canasto_de_frutas.count('banana')


print('La cantidad de frutas en el canasto es de: ', canasto_de_frutas_total)
print('indice de banana es: ', indice)  # Esto imprimirá 2, que es la segunda aparición de 'banana'
print('cantidad de bananas es: ', bananas_total)

def obtener_datos():
    return ("Hola", 42, True)


'''
    Desempaquetado de tupla
'''

mensaje, numero, _ = obtener_datos()

print(mensaje)  # "Hola"
print(numero)   # 42
# No imprimimos `_` porque lo ignoramos



