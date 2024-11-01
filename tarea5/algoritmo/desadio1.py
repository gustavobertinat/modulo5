class Nodo:
    def __init__(self, grado):
        """Inicializa un nodo con el grado y una lista de estudiantes."""
        self.grado = grado
        self.estudiantes = []  # Lista de estudiantes en este grado
        self.hijos = []  # Lista de nodos hijos (grados inferiores)

    def agregar_estudiante(self, estudiante):
        """Agrega un estudiante a la lista de estudiantes del nodo."""
        self.estudiantes.append(estudiante)

    def agregar_hijo(self, nodo_hijo):
        """Agrega un nodo hijo (grado inferior) a la lista de hijos."""
        self.hijos.append(nodo_hijo)


def recorrido_por_niveles(raiz):
    """Realiza un recorrido por niveles desde el nodo raíz."""
    if not raiz:
        return

    cola = [raiz]  # Cola para almacenar los nodos a procesar

    while cola:
        nodo_actual = cola.pop(0)  # Extraer el primer nodo de la cola
        print(f"Grado: {nodo_actual.grado}, Estudiantes: {', '.join(nodo_actual.estudiantes)}")

        # Agregar los hijos (grados inferiores) a la cola
        for hijo in nodo_actual.hijos:
            cola.append(hijo)


# Ejemplo de uso
if __name__ == "__main__":
    # Creación del árbol de grupos de estudiantes
    grado12 = Nodo(12)
    grado12.agregar_estudiante("Estudiante A")
    grado12.agregar_estudiante("Estudiante B")

    grado11 = Nodo(11)
    grado11.agregar_estudiante("Estudiante C")
    grado11.agregar_estudiante("Estudiante D")

    grado10 = Nodo(10)
    grado10.agregar_estudiante("Estudiante E")
    
    grado9 = Nodo(9)
    grado9.agregar_estudiante("Estudiante F")

    # Construir el árbol (estructura jerárquica)
    grado12.agregar_hijo(grado11)  # Grado 12 tiene como hijo grado 11
    grado11.agregar_hijo(grado10)  # Grado 11 tiene como hijo grado 10
    grado10.agregar_hijo(grado9)    # Grado 10 tiene como hijo grado 9

    # Realizar el recorrido por niveles
    print("Recorrido por niveles de estudiantes:")
    recorrido_por_niveles(grado12)
