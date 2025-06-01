import heapq
import math
from Graph import Graph
from fibonacci_heap_mod import Fibonacci_heap

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(graph, start, goal, heuristic=manhattan_distance):

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {node: float('inf') for node in graph.get_nodes()}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph.get_nodes()}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor, weight in graph.get_neighbors(current):
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  


def a_star_with_fibonacci(graph, start, goal, heuristic=manhattan_distance):
    fib_heap = Fibonacci_heap()
    node_refs = {}

    f_score_start = heuristic(start, goal)
    start_node = fib_heap.enqueue(start, f_score_start)
    node_refs[start] = start_node

    came_from = {}
    g_score = {node: math.inf for node in graph.get_nodes()}
    g_score[start] = 0

    while fib_heap.m_size > 0:
        current = fib_heap.dequeue_min().get_value()

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor, weight in graph.get_neighbors(current):
            tentative_g = g_score[current] + weight
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                if neighbor in node_refs:
                    fib_heap.decrease_key(node_refs[neighbor], f)
                else:
                    neighbor_node = fib_heap.enqueue(neighbor, f)
                    node_refs[neighbor] = neighbor_node

    return None


if __name__ == "__main__":
    g = Graph(directed=False)
    g.add_edge((0, 0), (0, 1), 1)
    g.add_edge((0, 1), (0, 2), 1)
    g.add_edge((0, 2), (1, 2), 1)
    g.add_edge((1, 2), (1, 1), 1)
    g.add_edge((1, 1), (1, 0), 1)
    g.add_edge((1, 0), (0, 0), 1)

    start = (0, 0)
    goal = (1, 2)

    path = a_star_with_fibonacci(g, start, goal)
    print("Camino encontrado:", path)

