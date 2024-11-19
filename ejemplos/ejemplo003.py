class Factura:
    # La siguiente es una variable de clase:
    vendedor = "Juan Carlos"
    # lista_productos = [] # Lista es una variable de clase

    # codigo_factura es una variable de instancia
    def __init__(self, codigo_factura:str):
        self.codigo_factura = codigo_factura
        self.lista_productos = []