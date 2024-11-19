from ejemplo003 import Factura

factura01 = Factura("001")
factura02 = Factura("002")

# Variable de clase: El mismo valor para ambos objetos
print(factura01.vendedor)
print(factura02.vendedor)
# Variable de instancia: Diferente valor para cada objeto
print(factura01.codigo_factura)
print(factura02.codigo_factura)

factura01.lista_productos.append("Acetaminofen")
factura02.lista_productos.append("Dolofin")
factura02.lista_productos.append("Tylenol")

print(factura01.lista_productos)
print(factura02.lista_productos)
