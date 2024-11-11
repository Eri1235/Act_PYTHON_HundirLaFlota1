abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
'''def crearMatriz(totalFilas,totalCol,valor):
    matriz = []
    for fila in range(totalFilas):
        matriz.append([])
        for col in range(totalCol): #Accedemos a la fila y añadimos un valor
            matriz[fila].append(valor)
    return matriz '''



def crearMatriz(totalFilas, totalCol, valor):
    matriz = []
    letra = ord('a')  # Valor ASCII de 'a'
    
    for fila in range(totalFilas):
        fila_actual = []
        
        # Asignamos la letra solo en la primera columna
        fila_actual.append(chr(letra))
        
        # Rellenamos las demás columnas con el valor dado
        for col in range(1, totalCol):
            fila_actual.append(valor)
        
        matriz.append(fila_actual)
        
        # Incrementamos la letra solo para la primera columna y reiniciamos en 'a' al llegar a 'j'
        letra += 1
        if letra > ord('j'):
            letra = ord('a')
    
    return matriz




def imprimirFilasMatriz(m): #Formato tablero
    for fila in m:
        print(fila)

matrizNueva = crearMatriz(10,10,"-")
imprimirFilasMatriz(matrizNueva)

#tablero = crear_tablero()
#imprimirFilasMatriz(tablero)