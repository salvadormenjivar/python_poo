from cafe import Cafe
class Menu:
    def __init__(self):
        self.menu = [
            Cafe("Latte", 200, 150, 24, 2.5),
            Cafe("Expresso", 50, 0, 18, 1.5),
            Cafe("Capuccino", 250, 50, 24, 3)
        ]

    def obtener_nombres(self):
        opciones = ""
        for cafe in self.menu:
            opciones += cafe.nombre + " | "
        return opciones

    def buscar_cafe(self, nombre_cafe):
        for objeto_cafe in self.menu:
            if objeto_cafe.nombre.upper() == nombre_cafe.upper():
                return objeto_cafe
        print("El cafe seleccionado no esta disponible")

'''
menu = Menu()
cafe_retornado = menu.buscar_cafe("Latte2")

print(menu.obtener_nombres())

latte = Cafe("latte", 200, 150, 24, 2.5),
expresso = Cafe("expresso", 50, 0, 18, 1.5),
capuccino = Cafe("capuccino", 250, 50, 24, 3)

lista_cafes = [latte, expresso, capuccino]


participantes = ["Juan", "Antonio"]
'''