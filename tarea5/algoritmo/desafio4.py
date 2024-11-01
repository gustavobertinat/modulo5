def ordenamiento_seleccion(estudiantes_promedios):
    n = len(estudiantes_promedios)
    
    # Recorremos toda la lista de estudiantes
    for i in range(n):
        # Suponemos que el máximo es el primer elemento no ordenado
        max_index = i
        
        # Buscamos el promedio más alto en el resto de la lista
        for j in range(i + 1, n):
            if estudiantes_promedios[j][1] > estudiantes_promedios[max_index][1]:
                max_index = j
        
        # Intercambiamos el elemento encontrado con el primero no ordenado
        estudiantes_promedios[i], estudiantes_promedios[max_index] = estudiantes_promedios[max_index], estudiantes_promedios[i]

# Ejemplo de uso
estudiantes_promedios = [
    ("Ana", 85.5),
    ("Benjamín", 92.3),
    ("Carlos", 78.4),
    ("Daniela", 88.7),
    ("Elena", 95.0)
]

ordenamiento_seleccion(estudiantes_promedios)

# Imprimimos la lista ordenada
print("Estudiantes ordenados por promedio (de mayor a menor):")
for estudiante, promedio in estudiantes_promedios:
    print(f"{estudiante}: {promedio}")
