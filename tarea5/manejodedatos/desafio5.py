from collections import Counter
import re

def contar_palabras_mas_comunes(archivo):
    # Leer el archivo y procesar el texto
    with open(archivo, 'r', encoding='utf-8') as file:
        texto = file.read().lower()  # Convertir a minúsculas para evitar duplicados por capitalización
    
    # Eliminar caracteres especiales y dividir en palabras
    palabras = re.findall(r'\b\w+\b', texto)
    
    # Contar la frecuencia de cada palabra
    contador_palabras = Counter(palabras)
    
    # Obtener las 5 palabras más comunes
    palabras_comunes = contador_palabras.most_common(5)
    
    # Mostrar el resultado
    print("Las 5 palabras más comunes son:")
    for palabra, frecuencia in palabras_comunes:
        print(f"{palabra}: {frecuencia} veces")

# Ejemplo de uso
contar_palabras_mas_comunes('libros.txt')
