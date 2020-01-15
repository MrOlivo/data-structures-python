import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class RecorridoGrafo():
    def busqueda_En_Profundidad(self, grafo, origen):
        pila = []
        visitados = []

        pila.append(origen)

        while pila:
            actual = pila.pop()

            if actual not in visitados:
                visitados.append(actual)
            
            v = grafo[actual]

            for key, value in v.items():
                if key not in visitados:
                    pila.append(key)
            
        return visitados
    
    def busqueda_En_Anchura(self, grafo, origen):
        visitados = []
        lista = []
        i = 0
        lista.append(origen)
        while i < len(lista):
            actual = lista[i]

            if actual not in visitados:
                visitados.append(actual)
            
            v = grafo[actual]
            w = v.items()
            for key, value in w:
                if key not in visitados:
                    lista.append(key)
            i += 1
        return visitados
