############ Try ############
'''
El bloque try contiene el código que puede generar una excepción.
Si ocurre una excepción dentro del bloque try, el flujo de ejecución se transfiere al bloque except correspondiente.
'''
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")


############ Except ############
'''
El bloque except especifica el tipo de excepción que se desea capturar y manejar. Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.
'''
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")


############ Finally ############
'''
El bloque finally es opcional y se ejecuta siempre, independientemente de si ocurrió una excepción o no. 
Se utiliza comúnmente para realizar tareas de limpieza o liberación de recursos.
'''
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    pass
    # archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción



############ Excepciones personalizadas ############

def funcion():
    # Código que puede generar una excepción personalizada
    condicion = True  # Cambia esto a False para evitar la excepción
    if condicion:
        raise Exception("Descripción del error")

'''
Si condicion es True, se lanza una excepción utilizando raise Exception("Descripción del error"). 
Esto significa que se crea y se lanza una nueva excepción con un mensaje que describe el error.
'''

try:
    funcion()
except Exception as error:
    print(f"Error: {str(error)}")

'''
Aquí utilizas un bloque try para llamar a funcion(). Si funcion() lanza una excepción, se ejecutará el bloque except.
En el bloque except, capturas la excepción en la variable e y luego imprimes un mensaje que incluye la descripción de la excepción. 
La función str(error) convierte la excepción en una cadena para que puedas mostrar el mensaje de error.
'''


############ Excepciones personalizadas ###########

class ValidacionError(Exception):
    pass

def validar_dato(dato):
    if not isinstance(dato, int):
        raise ValidacionError("El dato debe ser un número entero.")
    
'''
Con excepciones personalizadas, puedes manejar diferentes tipos de errores de manera más específica en tus bloques except.
Esto te permite tomar acciones diferentes según el tipo de excepción que se haya lanzado.
'''

try:
    validar_dato("texto")
except ValidacionError as ve:
    print(f"Error de validación: {str(ve)}")
except Exception as e:
    print(f"Error general: {str(e)}")