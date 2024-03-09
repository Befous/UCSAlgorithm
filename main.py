from graph import Graph, Node
from visualize_graph import visualize_graph
from ucs_algorithm import UCS

def run():
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Node('A'))
    graph.add_node(Node('B'))
    graph.add_node(Node('C'))
    graph.add_node(Node('D'))
    graph.add_node(Node('E'))
    graph.add_node(Node('F'))
    graph.add_node(Node('G'))
    
    # Add edges
    graph.add_edge('A', 'B', 5)
    graph.add_edge('A', 'D', 3)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'E', 4)
    graph.add_edge('C', 'E', 6)
    graph.add_edge('C', 'G', 8)
    graph.add_edge('D', 'E', 2)
    graph.add_edge('D', 'F', 2)
    graph.add_edge('E', 'G', 4)
    graph.add_edge('F', 'G', 3)

    # Execute the algorithm
    alg = UCS(graph, "C", "A")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")
    visualize_graph(graph)

if __name__ == '__main__':
  run()

# V1 -> V3 -> V4 -> V5 -> V6
# Length of the path: 6