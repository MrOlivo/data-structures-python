import heapq

class Dijkstra(object):
    def encontrar_el_camino(self, grafo, inicio, fin):
        cola = [(0, inicio, [])]
        visitados = set()
        
        while True:
            costo, v, camino = heapq.heappop(cola)

            if v not in visitados:
                camino = camino + [v]
                visitados.add(v)
            
            if v == fin:
                return costo, camino
            
            for (next, c) in grafo[v].items():
                heapq.heappush(cola, (costo + c, next, camino))
