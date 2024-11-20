from menu import Menu
from maquina_dinero import MaquinaDinero
from maquina_dispensadora import Maquina_Dispensadora

menu = Menu()
maquina_dispensadora = Maquina_Dispensadora()
maquina_dinero = MaquinaDinero()

opcion_seleccionada = input(f"Que tipo de cafe desea elegir {menu.obtener_nombres()} ")
while opcion_seleccionada != "off":
    if opcion_seleccionada == "reporte":
        maquina_dispensadora.reporte()
        maquina_dinero.reporte()
    else:
        obj_cafe = menu.buscar_cafe(opcion_seleccionada)
        if maquina_dispensadora.hay_suficientes_recursos(obj_cafe) and maquina_dinero.ejecutar_pago(obj_cafe.costo):
            maquina_dispensadora.hacer_cafe(obj_cafe)
    opcion_seleccionada = input(f"Que tipo de cafe desea elegir {menu.obtener_nombres()} ")
