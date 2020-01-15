import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from arboles.prim_kruskal import PrimKruskal

ejemplo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}

prim_kruskal = PrimKruskal()

arbol = prim_kruskal.prim(ejemplo, 'A')

print('{:-^25}'.format(' Prim '))

for desde, destino in arbol.items(): print(desde, '->', destino)

print('{:-^25}'.format(' Kruskal '))

arbol = prim_kruskal.kruskal(ejemplo)

for origen, destino in arbol.items(): print(origen, '->', destino)