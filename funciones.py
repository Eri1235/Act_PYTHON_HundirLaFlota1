def MenuDificultad(): #Menú de dificultad del juego
    print("############################")
    print("Bienvenida a Hundir la flota")
    print("############################")
    dificultad = int(input(print("Por favor, seleccione el nivel de dificultad: ")))
    return dificultad


def CrearTableroVacío(totalFilas,totalCol,valor):
    matrizVacía = []
    for fila in range(totalFilas):
        matrizVacía.append([])
        for columna in range(totalCol):
            matrizVacía[fila].append(valor)
    return matrizVacía

def imprimirfilasMatriz(m):
    for fila in m:
        print(fila)
    