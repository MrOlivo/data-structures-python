class Grafo(object):
    def __init__(self):
        self._relaciones = {}

    def agregar_vertice(self, vertice):
        self._relaciones.update({vertice:{}})

    def agregar_arista(self, origen, destino, peso):
        if origen not in self._relaciones:
            self.agregar_vertice(origen)

        if destino not in self._relaciones:
            self.agregar_vertice(destino)

        self._relaciones[origen].setdefault(destino, peso)
        self._relaciones[destino].setdefault(origen, peso)
    
    def retornar_grafo(self):
        return self._relaciones