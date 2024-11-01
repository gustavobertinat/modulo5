class Nodo:
    def __init__(self, promedio, estudiante):
        self.promedio = promedio
        self.estudiante = estudiante
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, promedio, estudiante):
        if self.raiz is None:
            self.raiz = Nodo(promedio, estudiante)
        else:
            self._insertar_recursivo(self.raiz, promedio, estudiante)

    def _insertar_recursivo(self, nodo, promedio, estudiante):
        if promedio < nodo.promedio:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(promedio, estudiante)
            else:
                self._insertar_recursivo(nodo.izquierda, promedio, estudiante)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(promedio, estudiante)
            else:
                self._insertar_recursivo(nodo.derecha, promedio, estudiante)

    def recorrido_inorden(self):
        return self._recorrido_inorden_recursivo(self.raiz)

    def _recorrido_inorden_recursivo(self, nodo):
        resultado = []
        if nodo:
            resultado.extend(self._recorrido_inorden_recursivo(nodo.izquierda))
            resultado.append((nodo.estudiante, nodo.promedio))
            resultado.extend(self._recorrido_inorden_recursivo(nodo.derecha))
        return resultado

# Ejemplo de uso
estudiantes_promedios = [
    ("Ana", 85.5),
    ("Benjamín", 92.3),
    ("Carlos", 78.4),
    ("Daniela", 88.7),
    ("Elena", 95.0)
]

arbol = ArbolBinarioBusqueda()

# Insertar estudiantes en el árbol
for estudiante, promedio in estudiantes_promedios:
    arbol.insertar(promedio, estudiante)

# Recorrer el árbol en inorden y mostrar estudiantes en orden ascendente
estudiantes_ordenados = arbol.recorrido_inorden()

print("Estudiantes en orden ascendente de rendimiento académico:")
for estudiante, promedio in estudiantes_ordenados:
    print(f"{estudiante}: {promedio}")
