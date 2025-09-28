# Creamos el diccionario 'informacion_personal' con las claves solicitadas
informacion_personal = {
    "nombre": "Cristina Castro",
    "edad": 10,
    "ciudad": "Latacunga",
    "profesion": "Estudiante"
}

# 1) Acceder al valor asociado con la clave "ciudad" y mostrarlo
print("Ciudad original:", informacion_personal["ciudad"])

# 2) Modificar la ciudad con otra diferente
informacion_personal["ciudad"] = "Quito"  # cambiamos la ciudad

# 3) Agregar / actualizar la clave "profesion" (si ya existía, la sobrescribimos)
informacion_personal["profesion"] = "Doctora"

# 4) Verificar si la clave "telefono" existe; si no existe, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0912345678"  # número ficticio (Ecuador)

# 5) Eliminar la clave "edad" porque no es necesaria
informacion_personal.pop("edad", None)  # pop con valor por defecto evita KeyError

# 6) Imprimir el diccionario final después de todas las operaciones
print("Diccionario final:", informacion_personal)
