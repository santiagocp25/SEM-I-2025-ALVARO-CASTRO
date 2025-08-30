def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def ordenar_fila_matriz(matriz, indice_fila):


    matriz_copia = [fila[:] for fila in matriz]

    if 0 <= indice_fila < len(matriz_copia):
        bubble_sort(matriz_copia[indice_fila])
    else:
        print(f"Índice de fila inválido: {indice_fila}")
    return matriz_copia

def mostrar_matriz(matriz, titulo=None):
    if titulo:
        print(titulo)
    for fila in matriz:
        print(fila)
    print()

def main():
    matriz = [
        [29, 32, 15],
        [14, 27, 11],
        [36, 13, 28]
    ]

    print("Matriz original:")
    mostrar_matriz(matriz)

    try:
        fila_idx = int(input("¿Qué fila deseas ordenar? (0-2): "))
    except ValueError:
        print("Entrada inválida. Se usará la fila 0 por defecto.")
        fila_idx = 0

    nueva_matriz = ordenar_fila_matriz(matriz, fila_idx)

    print(f"Matriz con la fila {fila_idx} ordenada:")
    mostrar_matriz(nueva_matriz)

if __name__ == "__main__":
    main()