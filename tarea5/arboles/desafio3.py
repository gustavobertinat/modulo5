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

    def recorrido_postorden_max(self, nodo):
        """
        Realiza un recorrido en postorden (izquierda, derecha, raíz) y encuentra el valor máximo.
        """
        if nodo is None:
            return float('-inf')  # Devuelve el valor más bajo posible si el nodo es nulo.

        # Recorrer el subárbol izquierdo, el subárbol derecho, y luego el nodo actual.
        max_izquierda = self.recorrido_postorden_max(nodo.hijo_izquierdo)
        max_derecha = self.recorrido_postorden_max(nodo.hijo_derecho)
        max_actual = nodo.valor

        # Retorna el mayor valor entre los tres (izquierda, derecha, nodo actual)
        return max(max_izquierda, max_derecha, max_actual)

# Ejemplo de uso: Construir el árbol binario y encontrar el valor máximo
arbol = ArbolBinario()

# Insertar algunos valores en el árbol
valores = [10, 5, 15, 3, 7, 12, 18]
for valor in valores:
    arbol.agregar_nodo(valor)

# Encontrar el valor máximo en el árbol binario con un recorrido postorden
maximo = arbol.recorrido_postorden_max(arbol.raiz)
print("El valor máximo en el árbol binario es:", maximo)
