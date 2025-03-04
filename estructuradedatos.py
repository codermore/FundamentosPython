"""
Estructuras de Datos en Python: Listas, Tuplas, Diccionarios y Conjuntos
Autor: ChatGPT
"""

# 🔹 LISTAS (list)
# Son mutables, ordenadas y permiten duplicados
mi_lista = [1, 2, 3, 4, 5, 2]  # Se pueden repetir elementos
mi_lista.append(6)  # Agregar un elemento
print("Lista:", mi_lista)
print("Elemento en índice 2:", mi_lista[2])  # Acceder por índice

# 🔹 TUPLAS (tuple)
# Son inmutables, ordenadas y permiten duplicados
mi_tupla = (1, 2, 3, 4, 5, 2)
print("\nTupla:", mi_tupla)
print("Elemento en índice 2:", mi_tupla[2])  # Acceder por índice
# mi_tupla[1] = 10  # ❌ Esto daría error porque las tuplas son inmutables

# 🔹 DICCIONARIOS (dict)
# Son mutables, ordenados (desde Python 3.7) y almacenan clave-valor
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"}
print("\nDiccionario:", mi_diccionario)
print("Nombre:", mi_diccionario["nombre"])  # Acceder por clave
mi_diccionario["edad"] = 31  # Modificar un valor
print("Diccionario modificado:", mi_diccionario)

# 🔹 CONJUNTOS (set)
# Son mutables, NO ordenados y no permiten duplicados
mi_conjunto = {1, 2, 3, 4, 5, 2}  # El 2 duplicado se eliminará automáticamente
mi_conjunto.add(6)  # Agregar un elemento
mi_conjunto.remove(3)  # Eliminar un elemento
print("\nConjunto:", mi_conjunto)

# 🔹 OPERACIONES CON CONJUNTOS
A = {1, 2, 3}
B = {3, 4, 5}
print("\nUnión de A y B:", A | B)  # {1, 2, 3, 4, 5}
print("Intersección de A y B:", A & B)  # {3}
