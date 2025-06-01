from Graph import Graph
from collections import deque

def push_relabel_max_flow(graph, source, sink):
    residual = {}
    for u in graph.get_nodes():
        residual[u] = {}
        for v, w in graph.get_neighbors(u):
            residual[u][v] = w
            if v not in residual:
                residual[v] = {}
            if u not in residual[v]:
                residual[v][u] = 0

    for u in list(residual.keys()):
        for v in residual[u]:
            if v not in residual:
                residual[v] = {}
            if u not in residual[v]:
                residual[v][u] = 0

    all_nodes = list(residual.keys())
    height = {node: 0 for node in all_nodes}
    excess = {node: 0 for node in all_nodes}
    height[source] = len(all_nodes)

    for v, capacity in graph.get_neighbors(source):
        residual[source][v] = 0
        residual[v][source] = capacity
        excess[v] = capacity
        excess[source] -= capacity

    active = [u for u in all_nodes if u != source and u != sink and excess[u] > 0]

    def push(u, v):
        send = min(excess[u], residual[u][v])
        residual[u][v] -= send
        if u not in residual[v]:
            residual[v][u] = 0
        residual[v][u] += send
        excess[u] -= send
        excess[v] += send
        if v != source and v != sink and excess[v] == send:
            active.append(v)

    def relabel(u):
        min_height = float('inf')
        for v in residual[u]:
            if residual[u][v] > 0:
                min_height = min(min_height, height[v])
        if min_height < float('inf'):
            height[u] = min_height + 1

    index = 0
    while index < len(active):
        u = active[index]
        pushed = False
        for v in residual[u]:
            if residual[u][v] > 0 and height[u] == height[v] + 1:
                push(u, v)
                pushed = True
                if excess[u] == 0:
                    break
        if not pushed:
            relabel(u)
            index = 0
        else:
            index += 1

    flow = sum(residual[v][source] for v in residual if source in residual[v])
    return flow

if __name__ == "__main__":
    g = Graph(directed=True)
    g.add_edge("s", "a", 16)
    g.add_edge("s", "c", 13)
    g.add_edge("a", "b", 12)
    g.add_edge("b", "c", 10)
    g.add_edge("c", "a", 4)
    g.add_edge("b", "t", 20)
    g.add_edge("c", "d", 14)
    g.add_edge("d", "b", 7)
    g.add_edge("d", "t", 4)

    max_flow = push_relabel_max_flow(g, "s", "t")
    print("Flujo máximo:", max_flow)