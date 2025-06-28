# Abstracción
# Encapsulamiento 
# Herencia.
from abc import ABC, abstractmethod  # Para crear clases abstractas

# Clase base abstracta: Animal
class Animal(ABC):
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Encapsulamiento: atributo privado
        self.__edad = edad

    # Encapsulamiento con getters y setters
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    # Método abstracto (Abstracción)
    @abstractmethod
    def hacerSonido(self):
        pass

    # Método concreto
    def comer(self):
        print(f"{self.__nombre} está comiendo.")

# Clase derivada: Perro
class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hacerSonido(self):
        print("¡Guau guau!")

# Clase derivada: Gato
class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hacerSonido(self):
        print("¡Miau miau!")

# Clase de prueba (main)
def main():
    perro1 = Perro("Lassie", 5)
    gato1 = Gato("Cat", 3)

    animales = [perro1, gato1]

    for animal in animales:
        print(f"Nombre: {animal.getNombre()}")
        print(f"Edad: {animal.getEdad()}")
        animal.comer()
        animal.hacerSonido()
        print("-----")

# Ejecutar solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()



# ANA MARIA MARTINEZ PIEDRA

