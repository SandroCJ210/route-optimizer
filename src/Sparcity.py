from Graph import Graph
def generate_sparsifier(graph, weight_threshold):
    """
    Devuelve un nuevo grafo donde solo se mantienen las aristas con peso <= weight_threshold.
    """
    new_graph = Graph(directed=graph.directed)
    for u, v, w in graph.get_edges():
        if w <= weight_threshold:
            new_graph.add_edge(u, v, w)
    return new_graph

if __name__ == "__main__":
    g = Graph(directed=True)
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 10)
    g.add_edge("C", "D", 1)
    g.add_edge("D", "A", 20)

    print("Grafo original:")
    print(g)

    sparse_g = generate_sparsifier(g, weight_threshold=5)
    print("\nGrafo sparsificado (umbral=5):")
    print(sparse_g)
