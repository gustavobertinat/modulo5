# Lista de códigos de productos en el inventario
inventario = ["A123", "B456", "C789", "D012", "E345"]

# Solicitar el código de producto al usuario
codigo = input("Introduce el código de producto que deseas buscar: ")

# Verificar si el código está en la lista y mostrar su posición o un mensaje de no encontrado
if codigo in inventario:
    posicion = inventario.index(codigo)
    print(f"El código {codigo} se encuentra en la posición {posicion}.")
else:
    print("El código no se ha encontrado en el inventario.")
