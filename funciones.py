from prueba import *

def MenuDificultad(): #Menú de dificultad del juego
    print("############################")
    print("Bienvenida a Hundir la flota")
    print("############################")

    dificultad = int(input("Dificultad: "))
    if dificultad == 1:
          print("\n--- Ordenador malvado D: ---\n")
          tabla1_ordenador()
          print("\n--- Tu ordenador :D ---\n")
          tabla1()
          



    