import string
import random
'''def crearMatriz(totalFilas,totalCol,valor):
    matriz = []
    for fila in range(totalFilas):
        matriz.append([])
        for col in range(totalCol): #Accedemos a la fila y añadimos un valor
            matriz[fila].append(valor)
    return matriz '''



#FUNCIONA
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




#----------------------------------------------------------------------------


# Crear el tablero vacío de 10x10
def crear_tablero(tamano=10):
	# Creamos una lista de listas (matriz) donde cada posición es "~"
	tablero = [["~" for _ in range(tamano)] for _ in range(tamano)]
	return tablero

# Función para imprimir el tablero de una forma amigable con letras en las filas
def imprimir_tablero(tablero):
	letras_filas = string.ascii_uppercase[:len(tablero)]  # Obtener las primeras letras según el tamaño del tablero
	print("  " + " ".join([str(i) for i in range(len(tablero))]))  # Numeración de las columnas
	for i, fila in enumerate(tablero):
            print(f"{letras_filas[i]} " + " ".join(fila))  # Usar letra en lugar de número para cada fila

# Inicializar y mostrar el tablero
#tablero = crear_tablero()
#imprimir_tablero(tablero) 

#------------COORDENADAS ESTÁTICAS------------

def tabla1():
    tablero = crear_tablero()
    tablero[0][0] = "L"
    tablero[4][4] = "Z"
    tablero[4][5] = "Z"
    tablero[4][6] = "Z"
    tablero[4][7] = "Z"
    imprimir_tablero(tablero)

def tabla1_ordenador():
    tablero = crear_tablero()
    imprimir_tablero(tablero)
    tablero[1][1] = "B" 
    tablero[1][2] = "B"
    tablero[1][3] = "B"
    tablero[1][3] = "B"
    #imprimir_tablero(tablero) (solucion)
        

#------------COORDENADAS DINÁMICAS------------
#Para más tarde


#----------------------------------------------------------------------------


MenuDificultad()


'''
def imprimirFilasMatriz(m): #Formato tablero
    for fila in m:
        print(fila)

matrizNueva = crearMatriz(10,10,"-")
imprimirFilasMatriz(matrizNueva)
'''

#tablero = crear_tablero()
#imprimirFilasMatriz(tablero)