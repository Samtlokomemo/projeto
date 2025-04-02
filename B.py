import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, keys=[], children=[]):
        self.keys = keys
        self.children = children

def build_b_tree_graph(root, graph, pos, x=0, y=0, layer=1):
    if root:
        node_label = str(root.keys)
        graph.add_node(node_label, pos=(x, -y))
        child_x = x - len(root.children) / 2 if root.children else x
        for i, child in enumerate(root.children):
            child_label = str(child.keys)
            graph.add_edge(node_label, child_label)
            child_x = x + (i - len(root.children) / 2)
            build_b_tree_graph(child, graph, pos, child_x, y + 1, layer + 1)
    return pos

# Exemplo de Árvore B (simplificado)
root = Node([20, 40], [
    Node([10, 15]),
    Node([30, 35]),
    Node([50, 60])
])

# Criação do grafo NetworkX
graph = nx.DiGraph()
pos = build_b_tree_graph(root, graph, {})

# Desenho do grafo
pos = nx.get_node_attributes(graph, 'pos')
nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightgreen', font_size=10)
plt.show()
