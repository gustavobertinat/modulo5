# Listas de números enteros de diferentes longitudes
lista1 = [3, 5, 7, 9]
lista2 = [2, 4, 6]

# Determinar la longitud máxima entre ambas listas
longitud_maxima = max(len(lista1), len(lista2))

# Extender ambas listas para que tengan la misma longitud, usando 0 para elementos faltantes
lista1.extend([0] * (longitud_maxima - len(lista1)))
lista2.extend([0] * (longitud_maxima - len(lista2)))

# Sumar los elementos de las listas en las posiciones correspondientes
suma_listas = [lista1[i] + lista2[i] for i in range(longitud_maxima)]

# Mostrar las listas originales y la lista resultante
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Suma de las listas:", suma_listas)
