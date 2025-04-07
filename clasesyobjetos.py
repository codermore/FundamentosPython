############ 1. Clases y objetos ############
'''
Clases: Son plantillas o modelos que definen las propiedades (atributos) y comportamientos (métodos) de los objetos. 
En Python, las clases se definen usando la palabra clave class.
Objetos: Son instancias de una clase. Al crear un objeto, estás utilizando la clase como un molde para generar una instancia con sus propios atributos.
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo de instancia
        self.edad = edad      # atributo de instancia
    
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

    def __repr__(self):
        return f"{self.nombre}: edad = {self.edad}"


# Crear una instancia (objeto) de la clase Persona
persona1 = Persona("Juan", 30)
persona1.saludar()
print(persona1)

############ 2. Encapsulamiento ############
'''
El encapsulamiento es el principio de ocultar los detalles internos de un objeto y exponer solo lo que es necesario. 
En Python, puedes indicar que un atributo es "privado" utilizando un guion bajo (_ o __) delante del nombre del atributo o método, 
aunque es más una convención que una verdadera restricción.
'''

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo "privado"
    
    def depositar(self, cantidad):
        self.__saldo += cantidad
    
    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes")
    
    def obtener_saldo(self):
        return self.__saldo
        
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta._CuentaBancaria__saldo)  # No recomendable, pero funcionará
print(cuenta.obtener_saldo())


############ 3. Herencia ############
'''
La herencia permite crear una nueva clase basada en una clase existente, reutilizando sus atributos y métodos,
y permitiendo agregar o modificar el comportamiento.
'''
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass  # Método abstracto

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

perro = Perro("Rex")
gato = Gato("Luna")

perro.hacer_sonido()  # Guau!
gato.hacer_sonido()   # Miau!

''' En este ejemplo, Perro y Gato heredan de Animal, y cada uno implementa su propia versión del método hacer_sonido. '''


############ 4. Polimorfismo ############
'''
El polimorfismo permite que un mismo método funcione de manera diferente en clases derivadas. 
Como en el ejemplo anterior, diferentes objetos (perro y gato) pueden tener el mismo método hacer_sonido, pero cada uno produce un resultado diferente.
'''
# Clase base o clase padre
class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")

# Clases derivadas o hijas
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Muuu!"

# Función que demuestra polimorfismo
def hacer_sonidos(animales):
    for animal in animales:
        print(animal.hacer_sonido())

# Lista de diferentes tipos de animales
animales = [Perro(), Gato(), Vaca()]

# Ejecutar función que hace los sonidos de cada animal
hacer_sonidos(animales)

# Para que se usa el raise NotImplementedError
animal_generico = Animal()
# animal_generico.hacer_sonido()


############ 5.  Encapsulamiento y Abstracción ############
'''
La abstracción es el proceso de ocultar detalles complejos y exponer solo lo esencial. 
Se combina con el encapsulamiento para crear interfaces simples para interactuar con los objetos.
Python no tiene interfaces explícitas como en otros lenguajes, pero puedes lograr abstracción
definiendo métodos en la clase base que deben ser implementados en las clases derivadas.
'''
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.1416 * (self.radio ** 2)

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

formas = [Circulo(5), Rectangulo(4, 6)]

print (type(formas[0]))

for forma in formas:
    print(f"El área es: {forma.area()}")

'''
Aquí, Forma es una clase abstracta y los métodos abstractos como area deben ser implementados en las clases derivadas.
'''


############ 6. Metaclasses y Herencia Múltiple ############
'''
Rara vez se utiliza pero aqui va:
'''

class A:
    def saludar(self):
        print("Hola desde A")

class B:
    def saludar(self):
        print("Hola desde B")

    def despedir(self):
        print("Adios desde B")

class C(A, B):
    pass

c = C()
c.saludar()  # Hola desde A, porque A se define antes que B
c.despedir()


############ 7. Métodos y operadores especiales ############
'''
Python permite definir comportamientos especiales para las clases, como la forma en que se comportan con operadores (+, -, ==, etc.), 
accediendo a índices, o incluso cómo se imprimen los objetos.
'''

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro_punto): #__add__ funciona para usar el operador +
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)

    def __sub__(self, otro_punto): #__sub__ funciona para usar el operador -
        return Punto(self.x - otro_punto.x, self.y - otro_punto.y)

    def __repr__(self): #__repr__ Proporciona una representación legible de los objetos Punto cuando se imprimen o se convierten en cadenas.
        return f"Punto({self.x}, {self.y})"

# Crear dos puntos
p1 = Punto(5, 7)
p2 = Punto(2, 3)

# Sumar los puntos
p3 = p1 + p2  # Punto(7, 10)

# Restar los puntos
p4 = p1 - p2  # Punto(3, 4)

# Imprimir resultados
print(p3)  # Salida: Punto(7, 10)
print(p4)  # Salida: Punto(3, 4)


'''
Otro ejemplo
'''

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def __sub__(self, otro_personaje):
        # Calcular el daño recibido basado en la defensa
        daño = max(0, otro_personaje.ataque - self.defensa)
        self.vida -= daño
        return self

    def __add__(self, curacion):
        self.vida += curacion
        return self

    def __mul__(self, multiplicador):
        # Multiplicar el daño infligido en un ataque especial
        self.ataque *= multiplicador
        return self

    def __repr__(self):
        return f"{self.nombre}: Vida = {self.vida}, Ataque = {self.ataque}, Defensa = {self.defensa}"

# Crear personajes
guerrero = Personaje("Guerrero", 100, 20, 5)
mago = Personaje("Mago", 80, 15, 3)

# Ataque con cálculo de defensa
mago = mago - guerrero  # Mago recibe daño considerando la defensa
print(mago)  # Salida: Mago: Vida = 68, Ataque = 15, Defensa = 3

# Guerrero usa un ataque especial
guerrero = guerrero * 2  # Duplicar ataque del guerrero
print(guerrero)  # Salida: Guerrero: Vida = 100, Ataque = 40, Defensa = 5
