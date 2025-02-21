print('hola mundo')

c = 4 % 2; 

print (c)

frutas = ['manzana', 'banna', 'melon', 'uva']
print (frutas)

for fruta in frutas:
    print (fruta)

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

miTupla = (1182, 3, 21)

print ('miTupla', miTupla)

print (miTupla.index(3))   # Salida: 1

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}

# Las estructuras de datos en Python nos brindan una gran flexibilidad y potencia para almacenar y manipular datos en nuestros programas. 
# Las listas son útiles para colecciones ordenadas y mutables, 
# las tuplas para colecciones ordenadas e inmutables, 
# los diccionarios para almacenar pares clave-valor y
# los conjuntos para colecciones no ordenadas de elementos únicos.

def multiplicar (a, b):
     
    return a * b

resultado = multiplicar (5, 3) + multiplicar (2, 4)

print(resultado)