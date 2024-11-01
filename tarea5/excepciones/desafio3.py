import math

def calcular_factorial():
    try:
        # Solicitamos un número al usuario
        numero = int(input("Introduce un número entero positivo: "))

        # Verificamos si el número es negativo
        if numero < 0:
            raise ValueError("El número no puede ser negativo.")

        # Calculamos el factorial usando la función factorial de math
        resultado = math.factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")

    except ValueError as ve:
        # Este except maneja números negativos o entradas no enteras
        print(f"Error: {ve}")
    
    except OverflowError:
        # Maneja el caso de un número demasiado grande para calcular el factorial
        print("Error: El número es demasiado grande para calcular su factorial.")
    
    except Exception as e:
        # Cualquier otro error que pueda ocurrir
        print(f"Ha ocurrido un error inesperado: {e}")

# Llamamos a la función
calcular_factorial()
