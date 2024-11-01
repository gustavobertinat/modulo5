def busqueda_binaria(lista_estudiantes, nombre_buscar):
    # Inicializamos los índices para la búsqueda
    izquierda = 0
    derecha = len(lista_estudiantes) - 1
    
    while izquierda <= derecha:
        # Calculamos el punto medio
        medio = (izquierda + derecha) // 2
        
        # Comparamos el nombre en el medio con el nombre que buscamos
        if lista_estudiantes[medio] == nombre_buscar:
            return medio  # Retornamos el índice si encontramos el nombre
        elif lista_estudiantes[medio] < nombre_buscar:
            izquierda = medio + 1  # Buscamos en la mitad derecha
        else:
            derecha = medio - 1  # Buscamos en la mitad izquierda
    
    return None  # Retornamos None si no encontramos el nombre

# Ejemplo de uso
lista_estudiantes = [
    "Ana",
    "Benjamín",
    "Carlos",
    "Daniela",
    "Elena",
    "Fernando",
    "Gabriela",
    "Hugo",
    "Isabel",
    "Juan"
]

nombre_a_buscar = "Daniela"
resultado = busqueda_binaria(lista_estudiantes, nombre_a_buscar)

if resultado is not None:
    print(f"El estudiante '{nombre_a_buscar}' se encuentra en la posición {resultado}.")
else:
    print(f"El estudiante '{nombre_a_buscar}' no se encontró en la lista.")
