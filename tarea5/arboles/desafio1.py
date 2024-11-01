class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijo_izquierdo = None
        self.hijo_derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, valor):
        """Inserta un nuevo valor en el árbol binario."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(self.raiz, valor)

    def _agregar(self, nodo_actual, valor):
        """Método auxiliar para recorrer el árbol e insertar el nodo en la posición correcta."""
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

    def recorrido_preorden(self, nodo):
        """Imprime el valor de los nodos en preorden (raíz, izquierda, derecha)."""
        if nodo:
            print(nodo.valor, end=" ")
            self.recorrido_preorden(nodo.hijo_izquierdo)
            self.recorrido_preorden(nodo.hijo_derecho)

# Ejemplo de uso: Construir el árbol binario
arbol = ArbolBinario()

# Insertar valores en el árbol
arbol.agregar_nodo(10)
arbol.agregar_nodo(5)
arbol.agregar_nodo(15)
arbol.agregar_nodo(3)
arbol.agregar_nodo(7)
arbol.agregar_nodo(12)
arbol.agregar_nodo(18)

# Mostrar el recorrido en preorden
print("Recorrido en preorden del árbol binario:")
arbol.recorrido_preorden(arbol.raiz)
