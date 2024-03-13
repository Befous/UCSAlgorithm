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
    graph.add_node(Node('H'))
    graph.add_node(Node('I'))
    graph.add_node(Node('J'))
    graph.add_node(Node('K'))
    graph.add_node(Node('L'))
    graph.add_node(Node('M'))
    graph.add_node(Node('N'))
    graph.add_node(Node('O'))
    graph.add_node(Node('P'))
    
    # Add edges
    graph.add_edge('A', 'C', 7)
    graph.add_edge('A', 'J', 15)
    graph.add_edge('A', 'B', 6)

    graph.add_edge('C', 'D', 5)

    graph.add_edge('J', 'L', 2)
    graph.add_edge('J', 'P', 12)
    graph.add_edge('J', 'I', 3)

    graph.add_edge('B', 'F', 8)
    graph.add_edge('B', 'G', 12)


    graph.add_edge('D', 'K', 5)
    graph.add_edge('D', 'L', 4)

    graph.add_edge('I', 'P', 11)
    graph.add_edge('I', 'H', 3)

    graph.add_edge('F', 'E', 4)
    graph.add_edge('F', 'H', 7)
    graph.add_edge('F', 'G', 7)

    graph.add_edge('G', 'H', 6)
    graph.add_edge('G', 'P', 13)
    graph.add_edge('G', 'M', 8)



    graph.add_edge('K', 'O', 12)

    graph.add_edge('H', 'P', 10)

    graph.add_edge('E', 'I', 5)

    graph.add_edge('M', 'N', 6)




    graph.add_edge('O', 'P', 5)

    graph.add_edge('N', 'P', 12)

    # Execute the algorithm
    alg = UCS(graph, "A", "P")
    path, _ = alg.search()
    print(" -> ".join(path))
    visualize_graph(graph)

if __name__ == '__main__':
  run()

# V1 -> V3 -> V4 -> V5 -> V6
# Length of the path: 6