import random
piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lista_opciones = [piedra, papel, tijera]
print("Bienvenido al juego de piedra, papel o tijera")

continuar = "SI"
while continuar.upper() == "SI":
    usuario_seleccion = int(input("Seleccione una opcion: 0.Piedra. 1.Papel, 2.Tijera   "))
    if usuario_seleccion >= 3 or usuario_seleccion < 0:
        print("Seleccione una opcion valida")
    else:
        print("Elegiste")
        print(lista_opciones[usuario_seleccion])
        seleccion_computadora = random.randint(0, 2)
        print("Seleccion de computadora: ")
        print(lista_opciones[seleccion_computadora])
        if usuario_seleccion == 0 and seleccion_computadora == 2 :
            print("Ganaste")
        elif seleccion_computadora == 0 and usuario_seleccion == 2:
            print("Perdiste")
        elif usuario_seleccion > seleccion_computadora:
            print("Ganaste")
        elif seleccion_computadora > usuario_seleccion:
            print("Perdiste")
        elif usuario_seleccion == seleccion_computadora:
            print("Empate")
        continuar = input("Desea continuar SI/NO  ")
