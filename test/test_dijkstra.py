import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from grafos.dijkstra import Dijkstra

grafo = {
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'B': {'A': 5, 'D': 1, 'G': 2},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}
    }

dj = Dijkstra()

costo, camino = dj.encontrar_el_camino(grafo, "G", "F")
print(costo, camino)