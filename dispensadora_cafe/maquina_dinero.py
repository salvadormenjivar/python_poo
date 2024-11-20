class MaquinaDinero:
    MONEDA = "$"
    VALORES_MONEDA = {
        "veinticinco" : 0.25,
        "diez" : 0.10,
        "cinco" : 0.05,
        "un centavo" : 0.01
    }

    def __init__(self):
        self.ingreso_venta = 0
        self.dinero_recibido = 0

    def reporte(self):
        print(f"Dinero por ventas: {self.MONEDA} {self.ingreso_venta} ")

    def procesar_dinero(self):
        print(f"Por favor ingrese las monedas: ")
        for moneda in self.VALORES_MONEDA:
            self.dinero_recibido += round(int(input(f"Cuantas monedas de {moneda}")) * self.VALORES_MONEDA[moneda] , 2)
        return round(self.dinero_recibido, 2)

    def ejecutar_pago(self, costo):
        self.procesar_dinero()
        if self.dinero_recibido >= costo:
            cambio = round(self.dinero_recibido - costo, 2)
            print(f"Aqui esta su cambio {self.MONEDA} {cambio}")
            self.ingreso_venta += costo
            self.dinero_recibido = 0
            return True
        else:
            print(f"Lo siento, el dinero ingresado no es suficiente {self.MONEDA} {self.dinero_recibido}")
            print(f"El costo del cafe es: {self.MONEDA}{costo}")
            print("Su dinero fue devuelto por la maquina")
            self.dinero_recibido = 0
            return False
'''
maquina_dinero = MaquinaDinero()
maquina_dinero.ejecutar_pago(2.5)
'''