# ANA MARIA MARTINEZ PIEDRA


from abc import ABC, abstractmethod
import math

# Clase abstracta: Forma
class Forma(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo opcional encapsulado

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

# Clase concreta: Circulo
class Circulo(Forma):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.__radio = radio

    def calcularArea(self):
        return math.pi * self.__radio ** 2

    def calcularPerimetro(self):
        return 2 * math.pi * self.__radio

# Clase concreta: Rectangulo
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        super().__init__("Rectángulo")
        self.__ancho = ancho
        self.__alto = alto

    def calcularArea(self):
        return self.__ancho * self.__alto

    def calcularPerimetro(self):
        return 2 * (self.__ancho + self.__alto)

# Clase de prueba
def main():
    formas = [
        Circulo(5),           # Radio = 5
        Rectangulo(4, 6),     # Ancho = 4, Alto = 6
        Circulo(2.5),
        Rectangulo(10, 3)
    ]

    for forma in formas:
        print(f"Forma: {forma.getNombre()}")
        print(f"Área: {forma.calcularArea():.2f}")
        print(f"Perímetro: {forma.calcularPerimetro():.2f}")
        print("-----")

# Ejecutar solo si es archivo principal
if __name__ == "__main__":
    main()
