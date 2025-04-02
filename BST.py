class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def build_graph(root, graph, pos, x=0, y=0, layer=1):
    if root is not None:
        graph.add_node(root.key, pos=(x, -y))
        if root.left:
            graph.add_edge(root.key, root.left.key)
            l_x, l_y = x - 1 / 2 ** layer, y + 1
            pos = build_graph(root.left, graph, pos, l_x, l_y, layer + 1)
        if root.right:
            graph.add_edge(root.key, root.right.key)
            r_x, r_y = x + 1 / 2 ** layer, y + 1
            pos = build_graph(root.right, graph, pos, r_x, r_y, layer + 1)
    return pos

# Construção da árvore
root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = insert(root, key)

# Criação do grafo NetworkX
graph = nx.DiGraph()
pos = build_graph(root, graph, {})

# Desenho do grafo
pos = nx.get_node_attributes(graph, 'pos')
nx.draw(graph, pos, with_labels=True, node_size=500, node_color='lightgreen', font_size=10)
plt.show()
