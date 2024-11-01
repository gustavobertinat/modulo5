def buscar_libros_por_autor(nombre_archivo, autor_buscar):
    try:
        with open(nombre_archivo, 'r') as archivo:
            libros_encontrados = []
            for linea in archivo:
                # Separamos el título y el autor
                libro, autor = linea.strip().split(';', 1)  # '1' para limitar la separación a dos partes
                # Comparamos el autor de la línea con el autor buscado (sin distinción de mayúsculas/minúsculas)
                if autor_buscar.lower() in autor.lower():  # Usar 'in' para verificar coincidencias parciales
                    libros_encontrados.append(libro)
        
        # Mostrar los resultados
        if libros_encontrados:
            print(f"Libros escritos por '{autor_buscar}':")
            for libro in libros_encontrados:
                print(f"- {libro}")
        else:
            print(f"No hay libros de '{autor_buscar}' en la lista.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
nombre_archivo = "C:/Users/guchu/Desktop/profesorado/programacion/tarea5/manejodedatos/libros.txt"
autor_a_buscar = input("Ingrese el nombre del autor que desea buscar: ")
buscar_libros_por_autor(nombre_archivo, autor_a_buscar)
