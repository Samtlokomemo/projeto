class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
def move_to_front(self, data):
    if not self.head:
        return

    if self.head.data == data:
        return

    prev = None
    curr = self.head

    while curr and curr.data != data:
        prev = curr
        curr = curr.next

    if not curr:
        return

    prev.next = curr.next
    curr.next = self.head
    self.head = curr
import random

class SkipNode:
    def __init__(self, data, level):
        self.data = data
        self.next = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.head = SkipNode(-1, max_level)
        self.level = 0

    def random_level(self):
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, data):
        new_level = self.random_level()
        new_node = SkipNode(data, new_level)
        update = [None] * (new_level + 1)
        curr = self.head

        for i in range(new_level, -1, -1):
            while curr.next[i] and curr.next[i].data < data:
                curr = curr.next[i]
            update[i] = curr

        for i in range(new_level + 1):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

        if new_level > self.level:
            self.level = new_level
import matplotlib.pyplot as plt

def visualize_linked_list(linked_list):
    data = []
    curr = linked_list.head
    while curr:
        data.append(curr.data)
        curr = curr.next

    plt.figure(figsize=(10, 5))
    for i in range(len(data)):
        plt.plot(i, data[i], 'o', markersize=10)  # Nós
        if i < len(data) - 1:
            plt.plot([i, i + 1], [data[i], data[i + 1]], '-')  # Linhas

    plt.show()
def visualize_skip_list(skip_list):
    layers = []
    for i in range(skip_list.level + 1):
        layer = []
        curr = skip_list.head.next[i]
        while curr:
            layer.append(curr.data)
            curr = curr.next[i]
        layers.append(layer)

    plt.figure(figsize=(15, 10))
    for i, layer in enumerate(layers):
        y = -i  # Posição vertical da camada
        for j, data in enumerate(layer):
            plt.plot(j, y, 'o', markersize=10)
            if j < len(layer) - 1:
                plt.plot([j, j + 1], [y, y], '-')

    plt.show()

# Cria uma lista encadeada de exemplo
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(20)

# Visualiza a lista encadeada
visualize_linked_list(linked_list)

# Cria uma skip list de exemplo
skip_list = SkipList(max_level=4, p=0.5)
skip_list.insert(3)
skip_list.insert(6)
skip_list.insert(7)
skip_list.insert(9)
skip_list.insert(12)
skip_list.insert(19)
skip_list.insert(26)
skip_list.insert(17)
skip_list.insert(21)
skip_list.insert(25)

# Visualiza a skip list
visualize_skip_list(skip_list)
