class Cafe:

    def __init__(self, nombre, agua, leche, cafe, costo):
        self.nombre = nombre
        self.costo = costo
        self.ingredientes = {
            "agua" : agua,
            "leche": leche,
            "cafe": cafe
        }

'''
cafe_late = Cafe("latte", 100, 50, 50, 2.5)
cafe_late.nombre
cafe_late.costo
for ingrediente in cafe_late.ingredientes:
    print(ingrediente["agua"])
    print(ingrediente["leche"])
    print(ingrediente["cafe"])
'''
