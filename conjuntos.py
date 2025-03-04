############ CONJUNTOS ############
'''
Un conjunto es una estructura de datos mutable y no ordenada que permite almacenar una colección de elementos únicos.
Los conjuntos se encierran entre llaves {} o se crean utilizando la función set().
'''

frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])


'''
Explicación:
La función set() toma un iterable (como una lista, una tupla, o incluso un string) y lo convierte en un conjunto.
Los conjuntos en Python son colecciones desordenadas de elementos únicos, lo que significa que cualquier duplicado en la lista original será eliminado.
'''

# Los conjuntos admiten operaciones matemáticas de conjuntos, 
''' 
 la unión (|), La unión devuelve un conjunto que incluye todos los elementos de ambos conjuntos, sin duplicar los valores comunes.
 la intersección (&), La intersección es útil cuando necesitas encontrar los elementos comunes entre dos conjuntos.
 la diferencia (-) y devuelve un nuevo conjunto que contiene los elementos de conjunto1 que no están en conjunto2.
 la diferencia simétrica (^). La diferencia simétrica devuelve los elementos que están en conjunto1 o en conjunto2, pero no en ambos.
'''

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}


interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}


diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}


diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}



# Características de los conjuntos en Python:
'''
Elementos únicos: Si intentas crear un conjunto a partir de una lista con valores repetidos, el conjunto eliminará automáticamente los duplicados.
'''

numeros = set([5, 22, 13, 13, 4, 5])
print(numeros)  # Imprime {13, 4, 5, 22}

'''
Desordenado: Los conjuntos no tienen un orden fijo, por lo que los elementos no se almacenan ni se acceden en un orden específico.
Operaciones: Puedes realizar operaciones como unión, intersección, diferencia, etc., con conjuntos, como hemos visto en ejemplos anteriores.
'''

#Metodos de conjuntos
'''
Los conjuntos en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:
    add(elemento): agrega un elemento al conjunto.
    remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
    discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
    clear(): elimina todos los elementos del conjunto.
'''

frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()