# Lista original con números, incluyendo duplicados
numeros = [3, 5, 3, 2, 8, 5, 1, 2, 9, 8]

# Eliminar duplicados convirtiendo la lista a un conjunto y volviendo a convertirla en lista
numeros_sin_duplicados = list(set(numeros))

# Mostrar la lista original y la lista sin duplicados
print("Lista original:", numeros)
print("Lista sin duplicados:", numeros_sin_duplicados)
