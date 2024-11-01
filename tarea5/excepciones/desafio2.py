def realizar_operaciones(lista):
    try:
        # Sumar todos los valores
        suma = sum(lista)
        print(f"La suma de los valores es: {suma}")

        # Calcular el promedio
        promedio = suma / len(lista)
        print(f"El promedio de los valores es: {promedio}")

        # Dividir el primer valor entre el segundo
        division = lista[0] / lista[1]
        print(f"El resultado de dividir {lista[0]} entre {lista[1]} es: {division}")

    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    
    except TypeError:
        print("Error: La lista contiene elementos que no son numéricos.")
    
    except ValueError:
        print("Error: No se pueden realizar operaciones con valores inválidos.")
    
    except IndexError:
        print("Error: La lista debe tener al menos dos elementos para realizar la división.")
    
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

# Ejemplo de lista
valores = [10, 5, 3, 8]

# Llamamos a la función
realizar_operaciones(valores)
