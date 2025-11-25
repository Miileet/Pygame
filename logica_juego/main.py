from modulo_funciones import *


def main():
    opcion = 0
    while opcion != 4:
        mostrar_menu()
        opcion = int(input("- - ->: "))
        match opcion:
            case 1:
                jugar()
            case 2:
                pass
            case 3:
                creditos()
            case 4:
                print("Saliendo del juego, adios")
            case _:
                print("ingrese una opcion correcta")

main()