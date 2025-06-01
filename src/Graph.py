class Graph:
    def __init__(self, directed=False):

        self.adj = {}  
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append((v, weight))

        if not self.directed:
            if v not in self.adj:
                self.adj[v] = []
            self.adj[v].append((u, weight))

    def get_neighbors(self, u):
        return self.adj.get(u, [])

    def get_nodes(self):
        return list(self.adj.keys())

    def get_edges(self):
        edges = []
        for u in self.adj:
            for v, w in self.adj[u]:
                if self.directed or (v, u, w) not in edges:
                    edges.append((u, v, w))
        return edges

    def __str__(self):
        result = []
        for u in self.adj:
            result.append(f"{u}: {self.adj[u]}")
        return "\n".join(result)
