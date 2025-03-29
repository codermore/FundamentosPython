
############ Decorador ############

'''
Un decorador es una función especial que modifica el comportamiento de otra función sin necesidad de cambiar su código. 
Se usa con el símbolo @ antes del nombre de la función a modificar.'
'''

def decorador(func):
    def funcion_modificada():
        print("Antes de ejecutar la función")
        result = 2+3
        func(result)
        print("Después de ejecutar la función")
    return funcion_modificada

@decorador
def mi_funcion(data_decorador):
    print(f"Hola, soy la función original {data_decorador}")

mi_funcion()
