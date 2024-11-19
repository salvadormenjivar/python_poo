'''
Desafio 1
Crea una clase llamada Carro que tenga los siguientes atributos y métodos:
1. Atributos: marca, modelo, año.
2. Método encender: Imprime que el coche se ha encendido.
3. Método mostrar_detalles: Muestra la marca, el modelo y el año del coche.
4. Crea un objeto de la clase Coche e invoca a sus métodos.
'''

class Carro:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def encender(self):
        print("El coche se ha encendido")

    def mostrar_detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio} ")

mi_coche = Carro("Toyota", "Corolla", 2024)
mi_coche.encender()
mi_coche.mostrar_detalles()

mi_carro = Carro("Nissan", "X", 2022)
mi_carro.encender()
mi_carro.mostrar_detalles()
