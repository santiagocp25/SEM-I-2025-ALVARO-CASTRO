#Matriz de registro de temperaturas
#inicializamos las variables de la matriz
ciudades = ["Quito","Latacunga","Puyo"]
semanas = 4
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

#inicializamos la matriz temperaturas
#capas: Ciudades
#filas: Semanas
#columnas: Valores de temperatura diarios

temperaturas = [
    [   # Quito
        [17,18,19,16,18,19,15], # Semana 1
        [16,18,19,20,17,18,19], # Semana 2
        [19,13,15,17,15,13,19], # Semana 3
        [17,18,16,15,19,17,18]  # Semana 4

    ],
    [   # Latacunga
        [13,15,16,15,14,13,15], # Semana 1
        [15,16,13,17,16,14,16], # Semana 2
        [13,12,14,15,14,13,12], # Semana 3
        [16,15,14,13,17,17,15]  # Semana 4

    ],
    [    # Puyo
        [21,19,20,18,19,21,20], # Semana 1
        [19,18,17,18,19,18,17], # Semana 2
        [21,19,20,18,18,21,19], # Semana 3
        [18,18,17,18,17,18,17]  # Semana 4
    ]

]
def calcular_promedios_redondeados(temperaturas, ciudades, semanas, dias, decimales=2):
    suma_total = 0
    cuenta_total = 0

    promedios_por_ciudad_semana = {}

    for idx_ciudad, ciudad in enumerate(ciudades):
        suma_ciudad = 0
        cuenta_ciudad = 0
        promedios_semana = []

        for semana in range(semanas):
            lista_dias = temperaturas[idx_ciudad][semana]
            suma_sem = sum(lista_dias)
            cuenta_sem = len(lista_dias)
            promedio_sem = suma_sem / cuenta_sem if cuenta_sem else 0
            promedio_sem_red = round(promedio_sem, decimales)
            promedios_semana.append(promedio_sem_red)

            suma_ciudad += suma_sem
            cuenta_ciudad += cuenta_sem

            suma_total += suma_sem
            cuenta_total += cuenta_sem

        promedio_ciudad = suma_ciudad / cuenta_ciudad if cuenta_ciudad else 0
        promedios_por_ciudad_semana[ciudad] = promedios_semana

    promedio_total = suma_total / cuenta_total if cuenta_total else 0
    promedio_total_red = round(promedio_total, decimales)

    return {
        "promedio_total": promedio_total_red,
        "promedio_por_ciudad_semana": promedios_por_ciudad_semana
    }

resultados = calcular_promedios_redondeados(temperaturas, ciudades, semanas, dias, decimales=2)

print("Promedio total:", resultados["promedio_total"])
for ciudad, lista_prom_sem in resultados["promedio_por_ciudad_semana"].items():
    print(f"Promedios semanales de {ciudad}:", lista_prom_sem)