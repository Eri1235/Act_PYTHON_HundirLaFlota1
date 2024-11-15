import string
import random
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

#---------Posición de los objeto (L,Z,B,P)----------- 
#Buque ocupa 3 casillas horizontales - consecutivas
#Acorazado ocupa 4 caillas verticales - consecutivas
#Portaviones ocupa 5 casillas verticales - consecutivas


	
def disparar(tablero, fila, columna,bror,pror,lror,aror):

    if tablero[fila][columna] == "X" or tablero[fila][columna] == "A":
        print("Ya disparaste en esta posición, vuelve a intentar.")
        return bror , pror , lror , aror, False 




    if tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
        bror = bror - 1
    elif tablero[fila][columna] == "L":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
        lror = lror - 1
    elif tablero[fila][columna] == "Z":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
        aror = aror - 1
    elif tablero[fila][columna] == "P":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
        pror -= 1
    else:
        tablero[fila][columna] = "A"  # Agua
        print("\nAgua...")
    return bror,lror,aror,pror, True


def disparar_or(tablero, fila, columna,brt1,lrt1,art1,prt1):

    if tablero[fila][columna] == "X" or tablero[fila][columna] == "A":
        return brt1 , prt1 , lrt1 , art1, False 


    if tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"
        print("\n¡Impacto a tu Barco D:!")
        brt1 = brt1 - 1
    elif tablero[fila][columna] == "L":
        tablero[fila][columna] = "X"
        print("\n¡Impacto! Una lancha menos")
        lrt1 = lrt1 - 1
    elif tablero[fila][columna] == "Z":
        tablero[fila][columna] = "X"
        print("\n¡El acorazado ha recibido daño!")
        art1 = art1 - 1
    elif tablero[fila][columna] == "P":
        tablero[fila][columna] = "X"
        print("\n¡Portavión en peligro!")
        prt1 = prt1 - 1
    else:
        tablero[fila][columna] = "A"  # Agua
        print("\nImpacto al agua vives un rato más")
    return brt1,lrt1,art1,prt1, True
    
   
    

# Convertir las entradas en índices de la matriz
    



# Realizar el disparo

def disparar(tablero, fila, columna,bror,pror,lror,aror):

    if tablero[fila][columna] == "X" or tablero[fila][columna] == "A":
        print("Ya disparaste en esta posición, vuelve a intentar.")
        return bror , pror , lror , aror, False 




    if tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
        bror = bror - 1
    elif tablero[fila][columna] == "L":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
        lror = lror - 1
    elif tablero[fila][columna] == "Z":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
        aror = aror - 1
    elif tablero[fila][columna] == "P":
        tablero[fila][columna] = "X"
        print("\n¡Impacto!")
        pror -= 1
    else:
        tablero[fila][columna] = "A"  # Agua
        print("\nAgua...")
    return bror,lror,aror,pror, True


def disparar_or(tablero, fila, columna,brt1,lrt1,art1,prt1):

    if tablero[fila][columna] == "X" or tablero[fila][columna] == "A":
        return brt1 , prt1 , lrt1 , art1, False 


    if tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"
        print("\n¡Impacto a tu Barco D:!")
        brt1 = brt1 - 1
    elif tablero[fila][columna] == "L":
        tablero[fila][columna] = "X"
        print("\n¡Impacto! Una lancha menos")
        lrt1 = lrt1 - 1
    elif tablero[fila][columna] == "Z":
        tablero[fila][columna] = "X"
        print("\n¡El acorazado ha recibido daño!")
        art1 = art1 - 1
    elif tablero[fila][columna] == "P":
        tablero[fila][columna] = "X"
        print("\n¡Portavión en peligro!")
        prt1 = prt1 - 1
    else:
        tablero[fila][columna] = "A"  # Agua
        print("\nImpacto al agua vives un rato más")
    return brt1,lrt1,art1,prt1, True

# Imprimir el tablero después del disparo
   



def tablon():
    tablerorandom = crear_tablero()

    #Lanchas
    tablerorandom [1][1] = "L"
    tablerorandom [7][9] = "L"
    tablerorandom [8][5] = "L"
    #Portaviones
    '''
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
    '''
    bror = sum(fila.count("B") for fila in tablerorandom)
    lror = sum(fila.count("L") for fila in tablerorandom)
    aror = sum(fila.count("Z") for fila in tablerorandom)
    pror = sum(fila.count("P") for fila in tablerorandom)


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

    brt1 = sum(fila.count("B") for fila in tablero1)
    lrt1 = sum(fila.count("L") for fila in tablero1)
    art1 = sum(fila.count("Z") for fila in tablero1)
    prt1 = sum(fila.count("P") for fila in tablero1)

#Imprimir tableros

    while brt1 > 0 or prt1 > 0 or lrt1> 0 or art1 > 0 or bror > 0 or pror > 0 or lror > 0 or aror > 0:
        print("---------- Tablero ordenador -----------")
        imprimir_tablero_oculto(tablerorandom)

        print("\n---------- Tu tablero :) -----------")
        imprimir_tablero(tablero1)

        while True:
            try:
                fila_input = input("Introduce la fila para disparar (A-J): ").upper() # Introducimos un valor de la A-J
                columna_input = input("Introduce la columna para disparar (0-9): ")
                
                fila = string.ascii_uppercase.index(fila_input)
                columna = int(columna_input)

                #Validamos las coordenadas se recorre la longitud de la fila y la columna y si sobre pasa o es un valor invalido vuelve al input
                if fila < 0 or fila >= len(tablerorandom) or columna < 0  or columna >= len(tablerorandom[0]):
                    print("Coordenada fuera de rango\n")
                    continue

                bror,pror,lror,aror, disparo_valido = disparar(tablerorandom, fila, columna,bror,pror,lror,aror)

                if disparo_valido:
                    print("\nTablero después del disparo:")
                    print("---------- Tablero ordenador -----------")
                    imprimir_tablero_oculto(tablerorandom)
                    if bror == 0 and pror == 0 and lror == 0 and aror == 0:
                        print("Le ganastes a la máquina vamooooos")
                        break

                    input("Enter para ver disparo del ordenador")

                    while True:

                        filarandom = random.randint(0,9) #Aquí para que mande a una fila random - para que pueda mandar
                        colrandom = random.randint(0,9) #Aquí para que mande a una columna random
                        
                        brt1,lrt1,art1,prt1,_ = disparar_or(tablero1,filarandom,colrandom,brt1,lrt1,art1,prt1)
                        print(f"El ordenador disparó en {string.ascii_uppercase[filarandom]} {colrandom}")
                        break
                    print("---------- Tu tablero :) -----------") 
                    imprimir_tablero(tablero1)
                    input("\nTe toca atacar >:) (Enter)")

                    if brt1 == 0 and prt1 == 0 and lrt1 == 0 and art1 == 0:
                        print("Te ganó la máquina :(")
                        break

            except (ValueError, IndexError):
                print("Entrada no válida")