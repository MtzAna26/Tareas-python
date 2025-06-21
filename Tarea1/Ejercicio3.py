class Calculadora:
    def __init__(self):
        self.resultado = 0
    def sumar(self, valor):
        self.resultado += valor
    def restar(self, valor):
        self.resultado -= valor
    def mostrar_resultado(self):
        print("Resultado actual:", self.resultado)
calc = Calculadora()
calc.sumar(100)
calc.restar(50)
calc.sumar(5)
calc.mostrar_resultado()