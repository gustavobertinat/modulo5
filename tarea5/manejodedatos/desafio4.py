def mostrar_prestamos():
    archivo = 'prestamos.txt'
    
    # Leer el archivo y almacenar cada línea en una lista
    with open(archivo, mode='r') as file:
        prestamos = file.readlines()
    
    # Mostrar los registros actuales de préstamos con un índice para elegir
    print("Registros de préstamos:")
    for idx, prestamo in enumerate(prestamos, start=1):
        print(f"{idx}. {prestamo.strip()}")
    
    return prestamos

def eliminar_prestamo():
    archivo = 'prestamos.txt'
    
    # Mostrar los préstamos actuales y devolver la lista
    prestamos = mostrar_prestamos()
    
    try:
        # Solicitar el número de préstamo a eliminar
        num_prestamo = int(input("Ingrese el número del préstamo que desea eliminar: ")) - 1
        
        # Validar que el número de préstamo esté en el rango correcto
        if num_prestamo < 0 or num_prestamo >= len(prestamos):
            print("Número de préstamo inválido.")
            return
        
        # Eliminar el registro seleccionado de la lista
        prestamo_eliminado = prestamos.pop(num_prestamo)
        
        # Actualizar el archivo con los registros restantes
        with open(archivo, mode='w') as file:
            file.writelines(prestamos)
        
        print(f"El registro '{prestamo_eliminado.strip()}' ha sido eliminado.")
    
    except ValueError:
        print("Debe ingresar un número válido.")

# Ejecutar el programa
eliminar_prestamo()
