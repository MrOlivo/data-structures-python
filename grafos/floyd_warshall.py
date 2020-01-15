class FloydWarshall(object):

    def floyd_warshall(self, grafo):
        grafo = dict(sorted(grafo.items()))
        nodes = list(grafo.keys())
        distances = dict()

        for i in nodes:
            dict_i = dict()
            for j in nodes:
                if i == j:
                    dict_i[j] = 0
                    continue
                try:
                    dict_i[j] = grafo[i][j]
                except:
                    dict_i[j] = float("inf")

            distances[i] = dict_i

        for i in nodes:
            for j in nodes:
                for k in nodes:
                    ij = distances[i][j]
                    ik = distances[i][k]
                    kj = distances[k][j]

                    if ij > ik + kj:
                        distances[i][j] = ik + kj

        return distances
