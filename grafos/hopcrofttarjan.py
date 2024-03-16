from collections import defaultdict

class HopcroftTarjan:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(list)
        self.ids = [-1] * num_vertices
        self.low = [-1] * num_vertices
        self.on_stack = [False] * num_vertices
        self.stack = []
        self.current_id = 0
        self.scc = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def tarjan(self):
        for v in range(self.num_vertices):
            if self.ids[v] == -1:
                self._dfs(v)

    def _dfs(self, v):
        self.ids[v] = self.current_id
        self.low[v] = self.current_id
        self.current_id += 1
        self.stack.append(v)
        self.on_stack[v] = True

        for neighbor in self.adj_list[v]:
            if self.ids[neighbor] == -1:
                self._dfs(neighbor)
            if self.on_stack[neighbor]:
                self.low[v] = min(self.low[v], self.low[neighbor])

        if self.ids[v] == self.low[v]:
            component = []
            while True:
                node = self.stack.pop()
                self.on_stack[node] = False
                component.append(node)
                if node == v:
                    break
            self.scc.append(component)
