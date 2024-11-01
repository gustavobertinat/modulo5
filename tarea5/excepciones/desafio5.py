def leer_archivo(nombre_archivo):
    try:
        # Intentamos abrir el archivo
        archivo = open(nombre_archivo, 'r')
        
        # Leemos y mostramos el contenido
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

    except FileNotFoundError:
        # Este except maneja el caso de que el archivo no exista
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    
    except Exception as e:
        # Cualquier otro error inesperado se maneja aquí
        print(f"Ha ocurrido un error inesperado: {e}")
    
    finally:
        # Nos aseguramos de que el archivo se cierre
        try:
            archivo.close()
            print("El archivo se ha cerrado correctamente.")
        except NameError:
            # Si no se abrió el archivo, 'archivo' no existirá
            print("El archivo no pudo abrirse, por lo que no es necesario cerrarlo.")

# Llamamos a la función con el nombre del archivo a leer
nombre_archivo = input("Introduce el nombre del archivo (incluyendo extensión) a leer: ")
leer_archivo(nombre_archivo)
