# 1. Escritura del archivo de texto
# Crear un archivo llamado "my_notes.txt" en modo escritura ("w")
f = open("my_notes.txt", "w", encoding="utf-8")

# Escribir al menos tres líneas de notas personales
f.write("Nota 1: Muy pronto termina el primer ciclo.\n")
f.write("Nota 2: Quiero practicar más ejercicios de Python.\n")
f.write("Nota 3: Aprender mucho sobre programacion.\n")

# Cerramos el archivo para asegurar que los datos se guarden
f.close()

# 2. Lectura del archivo línea por línea
# Abrir el archivo en modo lectura ("r")
f = open("my_notes.txt", "r", encoding="utf-8")

# Leer línea por línea usando readline()
line = f.readline()  # leer la primera línea
while line != "":    # readline() devuelve cadena vacía "" cuando ya no hay más líneas
    # Imprimir la línea leída. Usamos .rstrip("\n") para quitar el salto de línea al final (opcional)
    print(line.rstrip("\n"))
    # Leer la siguiente línea
    line = f.readline()

# 3. Cerrar el archivo después de la lectura
f.close()
