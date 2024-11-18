import random
import string
def posicionBarcos1(tablero): #3 casillas horizontales
    while True:
        for i in range(3): #total de barcos en el tablero
            filarandom = random.randint(0,9)
            colrandom = random.randint(0,7)
            #Evitar que se sobrepongan
            if tablero[filarandom][colrandom] == "B": 
                continue
            elif tablero[filarandom][colrandom] == "P":
                 continue
            elif tablero[filarandom][colrandom] == "Z":
                 continue
            elif tablero[filarandom][colrandom] == "L":
                 continue
            #Hasta aquí haz un cp
            for i in range(3): #casillas que ocupa
                tablero [filarandom][colrandom + i] = "B"
                br = sum(fila.count("B") for fila in tablero)
        
        if br == 9:
             break
        
def posicionPortaviones1(tablero):
    while True:
        for i in range(1):
            filarandom = random.randint(0,5)
            colrandom = random.randint(0,9)
            if tablero[filarandom][colrandom] == "P": 
                continue
            elif tablero[filarandom][colrandom] == "B": 
                continue
            elif tablero[filarandom][colrandom] == "Z":
                 continue
            elif tablero[filarandom][colrandom] == "L":
                 continue
            for i in range(5):
                tablero [filarandom + i][colrandom] = "P"
                pr = sum(fila.count("P") for fila in tablero)
        
        if pr == 5:
             break
        
def posicionAcorazados1(tablero):
    while True:
        for i in range(2):
            filarandom = random.randint(0,9)
            colrandom = random.randint(0,6)
            if tablero[filarandom][colrandom] == "Z": 
                continue
            elif tablero[filarandom][colrandom] == "B": 
                continue
            elif tablero[filarandom][colrandom] == "L":
                 continue
            elif tablero[filarandom][colrandom] == "P":
                 continue
            for i in range(4):
                tablero [filarandom][colrandom + i] = "Z"
                ar = sum(fila.count("Z") for fila in tablero)
        
        if ar == 8:
             break
def posicionLanchas1(tablero):
    for i in range(3):
        filarandom = random.randint(0,9)
        colrandom = random.randint(0,9)
        if tablero[filarandom][colrandom] == "P": 
            continue
        elif tablero[filarandom][colrandom] == "B": 
            continue
        elif tablero[filarandom][colrandom] == "Z":
            continue
        elif tablero[filarandom][colrandom] == "L":
            continue
        tablero [filarandom][colrandom] = "L"
        lr = sum(fila.count("L") for fila in tablero)
        return lr
        




#Nivel uno
# 1 portavion
# 2 acorazados = z
# 3 barcos

#Nivel dos
          
            





'''def posicionAcorazados(tablero): #4 casillas verticales
   for i in range(0,5,):
       filarandom = random.randint(0,9)
       colrandom = random.randint(0,9)
       tablero [colrandom] = "Z"
       '''
'''def posicionPortaviones(tablero):
   for i in range(0,6):
       filarandom = random.randint(0,9)
       colrandom = random.randint(0,9)
       tablero [colrandom] = "P"
'''
def crear_tablero(tamano=10):
	# Creamos una lista de listas (matriz) donde cada posición es "~"
	tablero = [["~" for _ in range(tamano)] for _ in range(tamano)]
	return tablero

def imprimir_tablero(tablero):
	letras_filas = string.ascii_uppercase[:len(tablero)]  # Obtener las primeras letras según el tamaño del tablero
	print("  " + " ".join([str(i) for i in range(len(tablero))]))  # Numeración de las columnas
	for i, fila in enumerate(tablero):
            print(f"{letras_filas[i]} " + " ".join(fila))

tablero1 = crear_tablero()
#imprimir_tablero(tablero1)
posicionLanchas1(tablero1)
posicionBarcos1(tablero1)
posicionAcorazados1(tablero1)
posicionPortaviones1(tablero1)
imprimir_tablero(tablero1)

