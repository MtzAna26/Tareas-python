class Animal:
    def __init__(self, raza, genero):
        self.raza = raza
        self.genero = genero
    def informacion(self):
        print (f"El animal es de raza {self.raza}, y su género es {self.genero}")
    
a1 = Animal("Labrador retriever", "femenino")
a1.informacion()

a2 = Animal("Golden retriver", "Masculino")
a2.informacion()