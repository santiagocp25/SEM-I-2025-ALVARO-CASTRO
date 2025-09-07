#Matriz de registro de temperaturas

#inicializamos las variables de la matriz
ciudades = ["Quito","Latacunga","Puyo"]
semanas = 2
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

#inicializamos la matriz temperaturas
#capas: Ciudades
#filas: Semanas
#columnas: Valores de temperatura diarios

temperaturas = [
    [   # Quito
        [17,18,19,16,18,19,15], # Semana 1
        [16,18,19,20,17,18,19] # Semana 2

    ],
    [   # Latacunga
        [13,15,16,15,14,13,15], # Semana 1
        [15,16,13,17,16,14,16] # Semana 2

    ],
    [    # Puyo
        [21,19,20,18,19,21,20], # Semana 1
        [19,18,17,18,19,18,17] # Semana 2
    ]

]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for semana in range(semanas):
        suma = 0
        for dia in range(len(dias)):
            suma += temperaturas[i][semana][dia]
        promedio = suma/len(dias)
        print(f"Semana {semana+1}: Promedio = {promedio:.2f} °C")