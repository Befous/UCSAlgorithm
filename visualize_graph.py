import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    G = nx.Graph()

    # Tambahkan node
    for node in graph.nodes:
        G.add_node(node.value)

    # Tambahkan edge
    for node in graph.nodes:
        for neighbor, weight in node.neighbors:
            G.add_edge(node.value, neighbor.value, weight=weight)

    # Buat posisi node
    pos = nx.spring_layout(G)

    # Gambar node
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # Gambar label node
    nx.draw_networkx_labels(G, pos)

    # Gambar edge
    nx.draw_networkx_edges(G, pos)

    # Gambar label edge
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Tampilkan plot
    plt.title("Graph Visualization")
    plt.axis('off')
    plt.show()