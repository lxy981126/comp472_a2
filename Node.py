import numpy as np


class Node:
    def __init__(self, entries, parent):
        self.g = 0
        self.h = 0
        self.f = 0
        self.entries = entries
        self.parent = parent
        self.empty = np.argwhere(entries == 0)[0]

    def __lt__(self, other):
        return self.f < other.f

    def vertical_move(self):
        new_entries = np.copy(self.entries)
        new_node = Node(parent=self, entries=new_entries)
        new_node.empty[0] = (new_node.empty[0] + 1) % 2
        swap(new_node.entries, self.empty, new_node.empty)
        return new_node

    def horizontal_move(self):
        new_nodes = np.array([])
        if self.empty[1] != 3:
            new_entries = np.copy(self.entries)
            right_node = Node(parent=self, entries=new_entries)
            right_node.empty[1] = (right_node.empty[1] + 1) % 4
            swap(right_node.entries, self.empty, right_node.empty)
            new_nodes = np.append(new_nodes, right_node)

        if self.empty[1] != 0:
            new_entries = np.copy(self.entries)
            left_node = Node(parent=self, entries=new_entries)
            left_node.empty[1] = (left_node.empty[1] - 1) % 4
            swap(left_node.entries, self.empty, left_node.empty)
            new_nodes = np.append(new_nodes, left_node)

        return new_nodes

    def wrapping_move(self):
        new_nodes = np.array([])
        if self.empty[1] == 0:
            new_entries = np.copy(self.entries)
            right_node = Node(parent=self, entries=new_entries)
            right_node.empty[1] = (right_node.empty[1] + 3) % 4
            swap(right_node.entries, self.empty, right_node.empty)
            new_nodes = np.append(new_nodes, right_node)

        if self.empty[1] == 3:
            new_entries = np.copy(self.entries)
            left_node = Node(parent=self, entries=new_entries)
            left_node.empty[1] = (left_node.empty[1] - 3) % 4
            swap(left_node.entries, self.empty, left_node.empty)
            new_nodes = np.append(new_nodes, left_node)

        return new_nodes

    def diagonal_move(self):
        new_nodes = np.array([])
        # right diagonal
        new_right_entries = np.copy(self.entries)
        right_node = Node(parent=self, entries=new_right_entries)
        right_node.empty[0] = (right_node.empty[0] + 1) % 2
        right_node.empty[1] = (right_node.empty[1] + 1) % 4
        swap(right_node.entries, self.empty, right_node.empty)
        new_nodes = np.append(new_nodes, right_node)
        # left diagonal
        new_left_entries = np.copy(self.entries)
        left_node = Node(parent=self, entries=new_left_entries)
        left_node.empty[0] = (left_node.empty[0] - 1) % 2
        left_node.empty[1] = (left_node.empty[1] - 1) % 4
        swap(left_node.entries, self.empty, left_node.empty)
        new_nodes = np.append(new_nodes, left_node)

        return new_nodes


def swap(array, index1, index2):
    temp = array[index1[0]][index1[1]]
    array[index1[0]][index1[1]] = array[index2[0]][index2[1]]
    array[index2[0]][index2[1]] = temp
    return array
