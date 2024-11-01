class Nodo:
    def __init__(self, valor):
        """Inicializa un nodo con un valor entero y sin hijos."""
        self.valor = valor
        self.hijo_izquierdo = None
        self.hijo_derecho = None

class ArbolBinario:
    def __init__(self):
        """Inicializa un árbol binario vacío."""
        self.raiz = None

    def agregar_nodo(self, valor):
        """Agrega un nuevo nodo al árbol binario."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(self.raiz, valor)

    def _agregar(self, nodo_actual, valor):
        """Inserta un nuevo nodo en la posición adecuada según el valor."""
        if valor < nodo_actual.valor:
            if nodo_actual.hijo_izquierdo is None:
                nodo_actual.hijo_izquierdo = Nodo(valor)
            else:
                self._agregar(nodo_actual.hijo_izquierdo, valor)
        else:
            if nodo_actual.hijo_derecho is None:
                nodo_actual.hijo_derecho = Nodo(valor)
            else:
                self._agregar(nodo_actual.hijo_derecho, valor)

    def recorrido_inorden_y_suma(self, nodo):
        """
        Realiza un recorrido en inorden (izquierda, raíz, derecha) y calcula la suma de todos los valores de los nodos.
        """
        if nodo is None:
            return 0
        # Suma los valores del subárbol izquierdo, el valor del nodo actual, y el subárbol derecho
        suma_izquierda = self.recorrido_inorden_y_suma(nodo.hijo_izquierdo)
        suma_nodo = nodo.valor
        suma_derecha = self.recorrido_inorden_y_suma(nodo.hijo_derecho)
        
        # Retorna la suma total
        return suma_izquierda + suma_nodo + suma_derecha

# Ejemplo de uso: Construir el árbol binario y calcular la suma
arbol = ArbolBinario()

# Insertar algunos valores en el árbol
valores = [10, 5, 15, 3, 7, 12, 18]
for valor in valores:
    arbol.agregar_nodo(valor)

# Calcular la suma de todos los valores en el árbol binario
suma_total = arbol.recorrido_inorden_y_suma(arbol.raiz)
print("La suma de los valores de todos los nodos es:", suma_total)
