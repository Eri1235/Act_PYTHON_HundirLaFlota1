import random
import string
def posicionBarcos(tablero): #3 casillas horizontales
    for i in range(3):
        filarandom = random.randint(0,7)
        colrandom = random.randint(0,7)   
        for i in range(3):
            tablero [filarandom][colrandom + i] = "B"

def posicionPortaviones(tablero): #3 casillas horizontales
    for i in range(2):
        filarandom = random.randint(0,5)
        colrandom = random.randint(0,5)   
        for i in range(5):
            tablero [filarandom + i][colrandom] = "P"

def posicionAcorazados(tablero): #3 casillas horizontales
    for i in range(2):
        filarandom = random.randint(0,6)
        colrandom = random.randint(0,6)   
        for i in range(4):
            tablero [filarandom + i][colrandom] = "Z"


            
          
            





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
posicionBarcos(tablero1)
posicionPortaviones(tablero1)
posicionAcorazados(tablero1)
imprimir_tablero(tablero1)

