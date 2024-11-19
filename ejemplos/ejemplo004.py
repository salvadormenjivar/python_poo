def sumar(*args):  # *args significa cualquier cantidad de parametros
    resultado = 0
    for num in args:
        # resultado = resultado + num
        resultado += num
    return resultado

print(sumar(1, 2))
print(sumar(100, 200, 300))
print(sumar(100, 200, 300, 400, 500))

# Funciones dentro de funciones ->  Pendientes
def funcion_externa(num_externa):
    def funcion_interna(num_interna):
        return num_interna ** 2
    return funcion_interna(num_externa) + num_externa

resultado = funcion_externa(3)
print(resultado)
