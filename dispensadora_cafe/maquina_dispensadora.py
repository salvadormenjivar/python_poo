class Maquina_Dispensadora:

    def __init__(self):
        self.recursos = {
            "agua":300,
            "leche":200,
            "cafe":100
        }

    # Mostrar los recursos con que cuenta la maquina dispensadora
    def reporte(self):
        print(f"Agua: {self.recursos['agua']} ml")
        print(f"Leche: {self.recursos['leche']} ml")
        print(f"Cafe: {self.recursos['cafe']} gr")

    def hay_suficientes_recursos(self, cafe):
        suficiente = True
        for ingrediente in cafe.ingredientes:
            if cafe.ingredientes[ingrediente] > self.recursos[ingrediente]:
                print(f"Lo sentimos no tenemos suficiente {ingrediente}")
                suficiente = False
        return suficiente

    def hacer_cafe(self, cafe):
        for ingrediente in cafe.ingredientes:
            self.recursos[ingrediente] -= cafe.ingredientes[ingrediente]
            # self.recursos[ingrediente] = self.recursos[ingrediente]  - cafe.ingredientes[ingrediente]
        print(f"Su cafe {cafe.nombre} esta listo !!! ")

'''
# Esta parte es solo para probar los metodos de la clase
cafe_late = Cafe("latte", 200, 100, 50, 2.5)
maquina_dispensadora = Maquina_Dispensadora()
# maquina_dispensadora.reporte()
# maquina_dispensadora.hay_suficientes_recursos(cafe_late)
maquina_dispensadora.hacer_cafe(cafe_late)
# agua 100,   leche 100,   cafe 50
'''