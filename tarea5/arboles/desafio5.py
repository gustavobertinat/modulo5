class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para determinar la precedencia de operadores
def precedencia(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0

# Función para aplicar un operador a dos operandos
def aplicar_operador(operador, izquierdo, derecho):
    if operador == '+':
        return izquierdo + derecho
    elif operador == '-':
        return izquierdo - derecho
    elif operador == '*':
        return izquierdo * derecho
    elif operador == '/':
        return izquierdo / derecho

# Construcción del árbol de expresiones
def construir_arbol(expresion):
    operandos = []  # Pila para los operandos (nodos del árbol)
    operadores = []  # Pila para los operadores
    
    i = 0
    while i < len(expresion):
        if expresion[i].isdigit():
            # Extraer número completo y crear nodo
            num = 0
            while i < len(expresion) and expresion[i].isdigit():
                num = num * 10 + int(expresion[i])
                i += 1
            operandos.append(Nodo(num))
            i -= 1  # Ajuste de índice tras salir del bucle
        elif expresion[i] in "+-*/":
            # Evaluar precedencia y construir subárboles según sea necesario
            while (operadores and precedencia(operadores[-1]) >= precedencia(expresion[i])):
                operador = operadores.pop()
                derecho = operandos.pop()
                izquierdo = operandos.pop()
                nodo = Nodo(operador)
                nodo.izquierdo = izquierdo
                nodo.derecho = derecho
                operandos.append(nodo)
            operadores.append(expresion[i])
        i += 1

    # Construir el resto del árbol con los operadores y operandos restantes
    while operadores:
        operador = operadores.pop()
        derecho = operandos.pop()
        izquierdo = operandos.pop()
        nodo = Nodo(operador)
        nodo.izquierdo = izquierdo
        nodo.derecho = derecho
        operandos.append(nodo)
    
    return operandos[0]  # Raíz del árbol de expresiones

# Evaluación del árbol de expresiones
def evaluar_arbol(nodo):
    if nodo is None:
        return 0
    if nodo.izquierdo is None and nodo.derecho is None:
        return nodo.valor  # Nodo hoja
    
    # Evaluar subárbol izquierdo y derecho
    izquierdo = evaluar_arbol(nodo.izquierdo)
    derecho = evaluar_arbol(nodo.derecho)
    
    # Aplicar operador
    return aplicar_operador(nodo.valor, izquierdo, derecho)

# Prueba del programa con la expresión "5 + 3 * 4"
expresion = "5 + 3 * 4"
arbol = construir_arbol(expresion)
resultado = evaluar_arbol(arbol)
print(f"El resultado de '{expresion}' es: {resultado}")
