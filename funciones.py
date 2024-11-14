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


	
	
'''def datosAleatorios(limite = 5): #ponemos el límite de lanchas que queremos poner
    tablerorandom = crear_tablero()
    for i in range(limite):
        filarandom = random.randint(0,9) #Aquí para que mande a una fila random - para que pueda mandar
        colrandom = random.randint(0,9) #Aquí para que mande a una columna random
        tablerorandom [filarandom] [colrandom] = random.choice("L")'''