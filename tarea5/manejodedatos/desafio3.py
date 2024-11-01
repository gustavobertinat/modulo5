import csv

def actualizar_inventario(nombre_archivo, titulo_libro, nuevas_copias):
    try:
        # Leer el inventario existente
        lista_inventario = []
        with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            inventario = list(lector)  # Convertimos a lista para poder modificar

        # Bandera para verificar si se encontró el libro
        libro_encontrado = False

        # Actualizar la cantidad de copias
        for i in range(len(inventario)-1):
            if inventario[i][0].split(';')[0].strip() == titulo_libro:
               
                lista_inventario.append(titulo_libro + ';'+ str(nuevas_copias))
                libro_encontrado = True
            else:
                lista_inventario.append(inventario[i])
        # Escribir los cambios de vuelta al archivo

        if libro_encontrado:
            # Escribir los cambios de vuelta al archivo
            with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(lista_inventario)  # Escribir todas las filas actualizadas
            print(f"La cantidad de copias de '{titulo_libro}' ha sido actualizada a {nuevas_copias}.")
        else:
            print(f"No se encontró el libro '{titulo_libro}' en el inventario.")

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Especificar la ruta correcta al archivo
nombre_archivo = r"C:\Users\guchu\Desktop\profesorado\programacion\tarea5\manejodedatos\inventario.csv"  # Cambia esto según tu sistema
titulo_libro = input("Ingrese el título del libro que desea actualizar: ")
nuevas_copias = int(input("Ingrese la nueva cantidad de copias: "))
actualizar_inventario(nombre_archivo, titulo_libro, nuevas_copias)