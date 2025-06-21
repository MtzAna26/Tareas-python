class Coche:
    def __init__(self, marca):
        self.marca = marca

    def acelerar(self):
        print("El coche está acelerando 🚗")
mi_coche0 = Coche ("Toyota")
print(mi_coche0.marca)
mi_coche0.acelerar()
print()

# Modificar el atributo marca fuera de la clase
mi_coche0.marca = "Honda"
print("Marca modificada:", mi_coche0.marca)
mi_coche0.acelerar()
print()

mi_coche1 = Coche("Chevrolet")
print(mi_coche1.marca)
mi_coche1.acelerar()