from collections import defaultdict
import heapq


class PrimKruskal(object):

    def prim(self, grafo, inicio):
        mst = defaultdict(set)
        visitados = [(inicio)]
        arista = [
            (costo, inicio, destino) for destino, costo in grafo[inicio].items()
        ]
        heapq.heapify(arista)

        while arista:
            costo, desde, destino = heapq.heappop(arista)

            if destino not in visitados:
                visitados.append(destino)

                mst[desde].add(destino)

                for adyacentes, costo in grafo[destino].items():
                    if adyacentes not in visitados:
                        heapq.heappush(arista, (costo, destino, adyacentes))

        return mst

    def kruskal(self, grafo=dict()):
        mst = defaultdict(set)
        visitados = []
        aristas = []

        for origen, adyacentes in grafo.items():
            for destino, peso in adyacentes.items():
                aristas.append((peso, origen, destino))

        heapq.heapify(aristas)

        while aristas:

            peso, origen, destino = heapq.heappop(aristas)

            if destino not in visitados:

                visitados.append(destino)

                mst[origen].add(destino)

        return dict(mst)
