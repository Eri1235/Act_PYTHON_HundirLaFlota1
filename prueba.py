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
          check_player_hit(tabla1_ordenador,tabla1)




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

#--------------------PRUEBA RANDOM------------------------------

def datosAleatorios(limite = 5): #ponemos el límite de lanchas que queremos poner
    tablerorandom = crear_tablero()
    for i in range(limite):
        filarandom = random.randint(0,9) #Aquí para que mande a una fila random - para que pueda mandar
        colrandom = random.randint(0,9) #Aquí para que mande a una columna random
        tablerorandom [filarandom] [colrandom] = random.choice("L")


    imprimir_tablero(tablerorandom)

#-------------------------DISPARO JUGADOR------------------------
def check_player_hit(tabla2, tabla1):
    """
    function for player hit or missed on enemy ship
    """
    row = int(input("Introduce fila: "))
    col = int(input("Enter your col:"))

    if tabla2[row][col] == "Z":
        tabla1[row][col] = "Z"
        print("Computer: Battleship been hit!")
    elif tabla2[row][col] == "L":
        tabla1[row][col] = "L"
        print("Computer: Cruiser been hit!")
    elif tabla2[row][col] == "F":
        tabla1[row][col] = "F"
        print("Computer: Frigate been hit!")
    elif tabla2[row][col] == "B":
        tabla1[row][col] = "B"
        print("Computer: Aircraft Carrier been hit")
    elif tabla2[row][col] == "S":
        tabla1[row][col] = "S"
        print("Computer: Sub been hit")
    else:
        tabla1[row][col] = "M"
        print("Missed me!")



#------------COORDENADAS ESTÁTICAS------------



def tabla1():
    tablero1 = crear_tablero()
    #Lanchas
    tablero1 [1][1] = "L"
    tablero1 [7][9] = "L"
    tablero1 [8][5] = "L"
    #Portaviones
    tablero1 [2][8] = "P"
    tablero1 [3][8] = "P"
    tablero1 [4][8] = "P"
    tablero1 [5][8] = "P"
    tablero1 [6][8] = "P"
    #Buques
    tablero1 [5][3] = "B"
    tablero1 [5][4] = "B"
    tablero1 [5][5] = "B"
    tablero1 [3][1] = "B"
    tablero1 [3][2] = "B"
    tablero1 [3][3] = "B"
    #Acorazados
    tablero1 [9][0] = "Z"
    tablero1 [9][1] = "Z"
    tablero1 [9][2] = "Z"
    tablero1 [9][3] = "Z"
    tablero1 [0][5] = "Z"
    tablero1 [0][6] = "Z"
    tablero1 [0][7] = "Z"
    tablero1 [0][8] = "Z"
    

    imprimir_tablero(tablero1)

def tabla1_ordenador():
    tablero2 = crear_tablero()
    #Lanchas
    tablero2 [6][1] = "L"
    tablero2 [3][6] = "L"
    tablero2 [1][0] = "L"
    tablero2 [7][8] = "L"
    #Acorazados


    #Buques


    #Portaviones


    
    imprimir_tablero(tablero2)
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