import math

# Definimos la excepción personalizada
class NegativeNumberError(Exception):
    def __init__(self, message="Error: No se puede calcular la raíz cuadrada de un número negativo."):
        self.message = message
        super().__init__(self.message)

def calcular_raiz_cuadrada():
    try:
        # Solicitamos un número al usuario
        numero = float(input("Introduce un número para calcular su raíz cuadrada: "))

        # Si el número es negativo, lanzamos la excepción personalizada
        if numero < 0:
            raise NegativeNumberError
        
        # Calculamos la raíz cuadrada
        resultado = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {resultado}")

    except NegativeNumberError as ne:
        # Manejamos la excepción personalizada
        print(ne)
    
    except ValueError:
        # Manejamos el error de valor no numérico
        print("Error: Debes ingresar un número válido.")
    
    except Exception as e:
        # Manejamos cualquier otro tipo de error
        print(f"Ha ocurrido un error inesperado: {e}")

# Llamamos a la función
calcular_raiz_cuadrada()
