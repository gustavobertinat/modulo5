class Nodo:
    def __init__(self, valor):
        """Inicializa un nodo con un valor entero y sin hijos."""
        self.valor = valor
        self.hijo_izquierdo = None
        self.hijo_derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        """Inicializa un árbol binario de búsqueda vacío."""
        self.raiz = None

    def agregar_nodo(self, valor):
        """Agrega un nuevo nodo al árbol de búsqueda binaria."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(self.raiz, valor)

    def _agregar(self, nodo_actual, valor):
        """Inserta un nuevo nodo en la posición adecuada en el árbol."""
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

    def buscar(self, nodo, valor):
        """
        Busca un valor en el árbol de búsqueda binaria.
        Devuelve True si el valor existe, False en caso contrario.
        """
        if nodo is None:
            return False  # Si el nodo es None, el valor no existe en el árbol.
        
        if valor == nodo.valor:
            return True  # Si el valor coincide con el nodo actual, el valor existe.

        # Si el valor es menor, buscar en el subárbol izquierdo.
        if valor < nodo.valor:
            return self.buscar(nodo.hijo_izquierdo, valor)
        else:
            # Si el valor es mayor, buscar en el subárbol derecho.
            return self.buscar(nodo.hijo_derecho, valor)

# Ejemplo de uso: Construir el árbol binario de búsqueda y buscar un valor
arbol = ArbolBinarioBusqueda()

# Insertar algunos valores en el árbol
valores = [10, 5, 15, 3, 7, 12, 18]
for valor in valores:
    arbol.agregar_nodo(valor)

# Buscar un número en el árbol
numero_a_buscar = 7
encontrado = arbol.buscar(arbol.raiz, numero_a_buscar)

if encontrado:
    print(f"El número {numero_a_buscar} se encuentra en el árbol.")
else:
    print(f"El número {numero_a_buscar} NO se encuentra en el árbol.")
