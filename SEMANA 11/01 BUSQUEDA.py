def buscar_en_matriz(matriz, objetivo):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == objetivo:
                return True, i, j
    return False, None, None
def main():
    # Definimos la matriz de ejemplo (3×3)
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # Pedimos un valor a buscar
    objetivo = int(input("Introduce el valor a buscar en la matriz: "))
    encontrado, fila, columna = buscar_en_matriz(matriz, objetivo)
    if encontrado:
        print(f"Valor {objetivo} encontrado en la posición [fila={fila}][columna={columna}].")
    else:
        print(f"Valor {objetivo} no se encontró en la matriz.")
if __name__ == "__main__":
    main()