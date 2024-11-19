# 1. Crear una clase
# Por convencion los nombres de las clases inician con mayuscula
# 2. Creacion de atributos
class Alumno:
    carnet = 1234
    
    # 3. Creacion de metodos
    def saludar(self) -> str:
        return "Hola que tal"

    def pagar(self) -> None:
        # Conectarse a la base de datos
        # Insertar un registro con el pago en la tabla Pago
        print("Se realiza el pago de lBienvenidosa mensualidad")