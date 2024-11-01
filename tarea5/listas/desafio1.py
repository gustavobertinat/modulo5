# Función para determinar el número mayor o si todos son iguales
def encontrar_mayor(num1, num2, num3):
    if num1 == num2 == num3:
        return "Todos los números son iguales."
    elif num1 >= num2 and num1 >= num3:
        return f"El número mayor es: {num1}"
    elif num2 >= num1 and num2 >= num3:
        return f"El número mayor es: {num2}"
    else:
        return f"El número mayor es: {num3}"

# Solicitar tres números al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Llamar a la función y mostrar el resultado
resultado = encontrar_mayor(num1, num2, num3)
print(resultado)
