#-*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from grafos.grafo import Grafo
from grafos.recorrido_grafo import RecorridoGrafo

print("Test Recorrido de grafos")
g = Grafo()
g.agregar_arista('Juan Carlos', 'Felipe', 1)
g.agregar_arista('Juan Carlos', 'Elena', 1)
g.agregar_arista('Juan Carlos', 'Cristina', 1)
g.agregar_arista('Felipe', 'Leonor', 2)
g.agregar_arista('Felipe', 'Sofia', 2)
g.agregar_arista('Elena', 'Frolan', 3)
g.agregar_arista('Elena', 'Victoria', 3)
g.agregar_arista('Cristina', 'Juan', 4)
g.agregar_arista('Cristina', 'Pablo', 4)
g.agregar_arista('Cristina', 'Miguel', 4)
g.agregar_arista('Cristina', 'Irene', 4)

g = g.retornar_grafo()

rg = RecorridoGrafo()

print("Búsqueda en Profundidad")
print(rg.busqueda_En_Profundidad(g, "Juan Carlos"))
print("Búsqueda en Anchura")
print(rg.busqueda_En_Anchura(g, "Juan Carlos"))
