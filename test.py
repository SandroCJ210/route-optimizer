from src.Graph import Graph
def test_graph():
    """
    Función de prueba para verificar que la clase Graph funciona correctamente.
    """
    print("=== PRUEBA DE LA CLASE GRAPH ===")
    
    # Grafo dirigido de ejemplo
    g = Graph(directed=True)
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "D", 3)
    g.add_edge("C", "D", 4)
    g.add_edge("D", "A", -5)
    
    print("\nEstructura del grafo:")
    print(g)
    
    # Pruebas básicas
    assert "A" in g.get_nodes(), "Error: el nodo A debería existir."
    assert ("B", 1) in g.get_neighbors("A"), "Error: A debería tener vecino B con peso 1."
    assert ("A", -5) in g.get_neighbors("D"), "Error: D debería tener vecino A con peso -5."
    
    print("\nNodos del grafo:", g.get_nodes())
    print("Aristas del grafo:", g.get_edges())
    
    print("\nLa clase Graph funciona correctamente.")

# Para ejecutar la prueba
if __name__ == "__main__":
    test_graph()
