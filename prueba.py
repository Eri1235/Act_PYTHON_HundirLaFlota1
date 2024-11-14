import string
import random
from funciones import *
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
    print("Bienvenidos a Hundir la flota")
    print("############################")

    dificultad = int(input("Dificultad: "))
    if dificultad == 1:
       tablon()
          
          
          



#----------------------------------------------------------------------------




# Inicializar y mostrar el tablero
#tablero = crear_tablero()
#imprimir_tablero(tablero) 

#--------------------PRUEBA RANDOM------------------------------

def datosAleatorios(): #ponemos el límite de lanchas que queremos poner
    tablerorandom = crear_tablero()

    #Lanchas
    tablerorandom [1][1] = "L"
    tablerorandom [7][9] = "L"
    tablerorandom [8][5] = "L"
    #Portaviones
    tablerorandom [2][8] = "P"
    tablerorandom [3][8] = "P"
    tablerorandom [4][8] = "P"
    tablerorandom [5][8] = "P"
    tablerorandom [6][8] = "P"
    #Buques
    tablerorandom [5][3] = "B"
    tablerorandom [5][4] = "B"
    tablerorandom [5][5] = "B"
    tablerorandom [3][1] = "B"
    tablerorandom [3][2] = "B"
    tablerorandom [3][3] = "B"
    #Acorazados
    tablerorandom [9][0] = "Z"
    tablerorandom [9][1] = "Z"
    tablerorandom [9][2] = "Z"
    tablerorandom [9][3] = "Z"
    tablerorandom [0][5] = "Z"
    tablerorandom [0][6] = "Z"
    tablerorandom [0][7] = "Z"
    tablerorandom [0][8] = "Z"

    filarandom = random.randint(0,9) #Aquí para que mande a una fila random - para que pueda mandar
    colrandom = random.randint(0,9) #Aquí para que mande a una columna random
    tablerorandom [filarandom] [colrandom] == random.choice(" ")
    disparar(tablerorandom,filarandom,colrandom) 


    imprimir_tablero(tablerorandom)

#-------------------------DISPARO JUGADOR------------------------
def disparar(tablero, fila, columna):
    if tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"  # Impacto
        print("\n¡Impacto!")
    elif tablero[fila][columna] == "L":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
    elif tablero[fila][columna] == "Z":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
    elif tablero[fila][columna] == "P":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
    else:
        tablero[fila][columna] = "A"  # Agua
        print("\nAgua...")
    
   
    

# Convertir las entradas en índices de la matriz
    



# Realizar el disparo
# Imprimir el tablero después del disparo
   



def tablon():
    print("---------- Tablero ordenador -----------")
    tablerorandom = crear_tablero()

    #Lanchas
    tablerorandom [1][1] = "L"
    tablerorandom [7][9] = "L"
    tablerorandom [8][5] = "L"
    #Portaviones
    tablerorandom [2][8] = "P"
    tablerorandom [3][8] = "P"
    tablerorandom [4][8] = "P"
    tablerorandom [5][8] = "P"
    tablerorandom [6][8] = "P"
    #Buques
    tablerorandom [5][3] = "B"
    tablerorandom [5][4] = "B"
    tablerorandom [5][5] = "B"
    tablerorandom [3][1] = "B"
    tablerorandom [3][2] = "B"
    tablerorandom [3][3] = "B"
    #Acorazados
    tablerorandom [9][0] = "Z"
    tablerorandom [9][1] = "Z"
    tablerorandom [9][2] = "Z"
    tablerorandom [9][3] = "Z"
    tablerorandom [0][5] = "Z"
    tablerorandom [0][6] = "Z"
    tablerorandom [0][7] = "Z"
    tablerorandom [0][8] = "Z"
    imprimir_tablero_oculto(tablerorandom)

    tablero1 = crear_tablero()
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
    print("---------- Tu tablero :) -----------")
    imprimir_tablero(tablero1)

    while(True):
        fila_input = input("Introduce la fila para disparar (A-J): ").upper() # Introducimos un valor de la A-J
        columna_input = input("Introduce la columna para disparar (0-9): ")
        fila = string.ascii_uppercase.index(fila_input)
        columna = int(columna_input)
        disparar(tablerorandom, fila, columna)
        print("\nTablero después del disparo:")
        print("---------- Tablero ordenador -----------")
        imprimir_tablero_oculto(tablerorandom)

        input("Enter para ver disparo del ordenador")


        filarandom = random.randint(0,9) #Aquí para que mande a una fila random - para que pueda mandar
        colrandom = random.randint(0,9) #Aquí para que mande a una columna random
        tablerorandom [filarandom] [colrandom] == random.choice(" ")
        disparar(tablero1,filarandom,colrandom)
        print("---------- Tu tablero :) -----------") 
        imprimir_tablero(tablero1)






    
def imprimir_tablero_oculto(tablero):
    letras_filas = string.ascii_uppercase[:len(tablero)]
    print("  " + " ".join([str(i) for i in range(len(tablero))]))
    for i, fila in enumerate(tablero): 
        fila_oculta = [
            '~' if celda == "B" else
            '~' if celda == "L" else
            '~' if celda == "P" else
            '~' if celda == "Z" else
            celda for celda in fila
        ]
        print(f"{letras_filas[i]} " + " ".join(fila_oculta))

    #Acorazados


    #Buques


    #Portaviones


    
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