class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:  # Ignorar duplicados
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar(nodo_actual.derecha, valor)

    def buscar(self, valor):
        """Busca un valor en el árbol y devuelve True si lo encuentra."""
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar(nodo_actual.izquierda, valor)
        else:
            return self._buscar(nodo_actual.derecha, valor)

    def recorrido_inorden(self):
        """Realiza un recorrido en orden (inorder) del árbol."""
        elementos = []
        self._inorden(self.raiz, elementos)
        return elementos

    def _inorden(self, nodo_actual, elementos):
        if nodo_actual:
            self._inorden(nodo_actual.izquierda, elementos)
            elementos.append(nodo_actual.valor)
            self._inorden(nodo_actual.derecha, elementos)

    def recorrido_preorden(self):
        """Realiza un recorrido en preorden del árbol."""
        elementos = []
        self._preorden(self.raiz, elementos)
        return elementos

    def _preorden(self, nodo_actual, elementos):
        if nodo_actual:
            elementos.append(nodo_actual.valor)
            self._preorden(nodo_actual.izquierda, elementos)
            self._preorden(nodo_actual.derecha, elementos)

    def recorrido_postorden(self):
        """Realiza un recorrido en postorden del árbol."""
        elementos = []
        self._postorden(self.raiz, elementos)
        return elementos

    def _postorden(self, nodo_actual, elementos):
        if nodo_actual:
            self._postorden(nodo_actual.izquierda, elementos)
            self._postorden(nodo_actual.derecha, elementos)
            elementos.append(nodo_actual.valor)

 
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    valores = [50, 30, 70, 20, 40, 60, 80]

    for valor in valores:
        arbol.insertar(valor) 

    print("Recorrido en orden:", arbol.recorrido_inorden()) 
    print("Recorrido en preorden:", arbol.recorrido_preorden())  
    print("Recorrido en postorden:", arbol.recorrido_postorden())  

    
    print("¿Está 40 en el árbol?:", arbol.buscar(40)) 
    print("¿Está 90 en el árbol?:", arbol.buscar(90))           

