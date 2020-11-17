import numpy as np


class Node:
    def __init__(self, entries, parent):
        self.g = 0
        self.h = 0
        self.f = 0
        self.row = np.shape(entries)[0]
        self.column = np.shape(entries)[1]
        self.entries = entries
        self.parent = parent
        self.empty = np.argwhere(entries == 0)[0]

    def __lt__(self, other):
        return self.f < other.f

    def vertical_move(self):
        new_nodes = np.array([])
        if self.empty[0] < self.row - 1:
            down_entries = np.copy(self.entries)
            down_node = Node(parent=self, entries=down_entries)
            down_node.empty[0] = (down_node.empty[0] + 1) % self.row
            swap(down_node.entries, self.empty, down_node.empty)
            new_nodes = np.append(new_nodes, down_node)

        if self.empty[0] > 0:
            up_entries = np.copy(self.entries)
            up_node = Node(parent=self, entries=up_entries)
            up_node.empty[0] = (up_node.empty[0] - 1) % self.row
            swap(up_node.entries, self.empty, up_node.empty)
            new_nodes = np.append(new_nodes, up_node)
        return new_nodes

    def horizontal_move(self):
        new_nodes = np.array([])
        if self.empty[1] < self.column - 1:
            new_entries = np.copy(self.entries)
            right_node = Node(parent=self, entries=new_entries)
            right_node.empty[1] = (right_node.empty[1] + 1) % self.column
            swap(right_node.entries, self.empty, right_node.empty)
            new_nodes = np.append(new_nodes, right_node)

        if self.empty[1] > 0:
            new_entries = np.copy(self.entries)
            left_node = Node(parent=self, entries=new_entries)
            left_node.empty[1] = (left_node.empty[1] - 1) % self.column
            swap(left_node.entries, self.empty, left_node.empty)
            new_nodes = np.append(new_nodes, left_node)

        return new_nodes

    def wrapping_move(self):
        new_nodes = np.array([])
        if self.empty[1] == 0:
            new_entries = np.copy(self.entries)
            right_node = Node(parent=self, entries=new_entries)
            right_node.empty[1] = (right_node.empty[1] + self.column - 1) % self.column
            swap(right_node.entries, self.empty, right_node.empty)
            new_nodes = np.append(new_nodes, right_node)

        if self.empty[1] == self.column - 1:
            new_entries = np.copy(self.entries)
            left_node = Node(parent=self, entries=new_entries)
            left_node.empty[1] = (left_node.empty[1] - self.column + 1) % self.column
            swap(left_node.entries, self.empty, left_node.empty)
            new_nodes = np.append(new_nodes, left_node)

        if self.empty[0] == 0:
            new_entries = np.copy(self.entries)
            new_node = Node(parent=self, entries=new_entries)
            new_node.empty[0] = (new_node.empty[0] + self.row - 1) % self.row
            swap(new_node.entries, self.empty, new_node.empty)
            new_nodes = np.append(new_nodes, new_node)

        if self.empty[0] == self.row - 1:
            new_entries = np.copy(self.entries)
            new_node = Node(parent=self, entries=new_entries)
            new_node.empty[0] = (new_node.empty[0] - self.row + 1) % self.row
            swap(new_node.entries, self.empty, new_node.empty)
            new_nodes = np.append(new_nodes, new_node)

        return new_nodes

    def diagonal_move(self):
        new_nodes = np.array([])
        if self.empty[0] != self.row - 1 and self.empty[1] != 0:
            new_right_entries = np.copy(self.entries)
            right_node = Node(parent=self, entries=new_right_entries)
            right_node.empty[0] = (right_node.empty[0] + 1) % self.row
            right_node.empty[1] = (right_node.empty[1] - 1) % self.column
            swap(right_node.entries, self.empty, right_node.empty)
            new_nodes = np.append(new_nodes, right_node)

        if self.empty[0] != self.row - 1 and self.empty[1] != self.column - 1:
            new_right_entries = np.copy(self.entries)
            right_node = Node(parent=self, entries=new_right_entries)
            right_node.empty[0] = (right_node.empty[0] + 1) % self.row
            right_node.empty[1] = (right_node.empty[1] + 1) % self.column
            swap(right_node.entries, self.empty, right_node.empty)
            new_nodes = np.append(new_nodes, right_node)

        if self.empty[0] != 0 and self.empty[1] != 0:
            new_left_entries = np.copy(self.entries)
            left_node = Node(parent=self, entries=new_left_entries)
            left_node.empty[0] = (left_node.empty[0] - 1) % self.row
            left_node.empty[1] = (left_node.empty[1] - 1) % self.column
            swap(left_node.entries, self.empty, left_node.empty)
            new_nodes = np.append(new_nodes, left_node)

        if self.empty[0] != 0 and self.empty[1] != self.column - 1:
            new_left_entries = np.copy(self.entries)
            left_node = Node(parent=self, entries=new_left_entries)
            left_node.empty[0] = (left_node.empty[0] - 1) % self.row
            left_node.empty[1] = (left_node.empty[1] + 1) % self.column
            swap(left_node.entries, self.empty, left_node.empty)
            new_nodes = np.append(new_nodes, left_node)

        return new_nodes


def swap(array, index1, index2):
    temp = array[index1[0]][index1[1]]
    array[index1[0]][index1[1]] = array[index2[0]][index2[1]]
    array[index2[0]][index2[1]] = temp
    return array
