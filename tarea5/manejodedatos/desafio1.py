def agregar_prestamo(nombre_archivo):
    # Pedimos los datos al usuario
    libro = input("Ingrese el nombre del libro: ")
    prestatario = input("Ingrese el nombre del prestatario: ")
    fecha_prestamo = input("Ingrese la fecha del préstamo (formato: dd/mm/yyyy): ")
    
    # Abrimos el archivo en modo append para no sobrescribir el contenido
    with open(nombre_archivo, 'a') as archivo:
        # Escribimos el registro en el archivo
        archivo.write(f"{libro}, {prestatario}, {fecha_prestamo}\n")
        #archivo.close()
    print("Préstamo agregado exitosamente.")

def main():
    nombre_archivo = "prestamos.txt"
    
    while True:
        agregar_prestamo(nombre_archivo)
        continuar = input("¿Desea agregar otro préstamo? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
