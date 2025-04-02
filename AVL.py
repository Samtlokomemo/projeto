import networkx as nx
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if node is None:
        return 0
    return node.height

def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def update_height(node):
    if node is not None:
        node.height = 1 + max(height(node.left), height(node.right))

def rotate_right(y):
    x = y.left
    t2 = x.right

    x.right = y
    y.left = t2

    update_height(y)
    update_height(x)

    return x

def rotate_left(x):
    y = x.right
    t2 = y.left

    x.right = t2
    y.left = x

    update_height(x)
    update_height(y)

    return y

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    update_height(root)

    balance = balance_factor(root)

    if balance > 1:
        if key < root.left.key:
            return rotate_right(root)
        else:
            root.left = rotate_left(root.left)
            return rotate_right(root)

    if balance < -1:
        if key > root.right.key:
            return rotate_left(root)
        else:
            root.right = rotate_right(root.right)
            return rotate_left(root)

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

# Criação da árvore AVL
root = None
keys = random.sample(range(1, 100), 17)
for key in keys:
    root = insert(root, key)

# Criação do grafo NetworkX
graph = nx.DiGraph()
pos = build_graph(root, graph, {})

# Desenho do grafo
pos = nx.get_node_attributes(graph, 'pos')
nx.draw(graph, pos, with_labels=True, node_size=500, node_color='lightgreen', font_size=10)
plt.show()
