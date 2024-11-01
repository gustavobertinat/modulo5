def solicitar_numeros():
    try:
        # Solicitamos los números al usuario
        numero1 = int(input("Introduce el primer número entero: "))
        numero2 = int(input("Introduce el segundo número entero: "))

        # Intentamos realizar la división
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado}")

    except ValueError:
        # Este except maneja errores de conversión de tipos no válidos
        print("Error: Debes ingresar números enteros válidos.")
    
    except ZeroDivisionError:
        # Este except maneja la división por cero
        print("Error: No se puede dividir por cero.")
    
    except Exception as e:
        # Cualquier otra excepción se manejará aquí
        print(f"Ha ocurrido un error inesperado: {e}")

# Llamamos a la función
solicitar_numeros()
