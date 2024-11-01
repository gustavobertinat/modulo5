def buscar_calificacion(matriz_calificaciones, calificacion_buscar):
    # Recorremos cada fila (cada estudiante) en la matriz
    for i in range(len(matriz_calificaciones)):
        # Recorremos cada calificación en la fila actual
        for j in range(len(matriz_calificaciones[i])):
            # Comparamos la calificación actual con la calificación que buscamos
            if matriz_calificaciones[i][j] == calificacion_buscar:
                # Si encontramos la calificación, retornamos la posición
                return (i, j)  # (estudiante, materia)
    # Si no encontramos la calificación, retornamos None
    return None

# Ejemplo de uso
matriz_calificaciones = [
    [85, 90, 78],  # Estudiante 0
    [88, 76, 95],  # Estudiante 1
    [92, 89, 84]   # Estudiante 2
]

calificacion_a_buscar = 76
resultado = buscar_calificacion(matriz_calificaciones, calificacion_a_buscar)

if resultado:
    estudiante, materia = resultado
    print(f"La calificación {calificacion_a_buscar} se encuentra en el estudiante {estudiante} y en la materia {materia}.")
else:
    print(f"La calificación {calificacion_a_buscar} no se encontró en la matriz.")
