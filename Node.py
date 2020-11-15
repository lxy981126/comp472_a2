import copy
import numpy as np


class Node:
    def __init__(self, entries, parent):
        self.cost = 0
        self.heuristic = 0
        self.entries = entries
        self.parent = parent
        self.empty = np.argwhere(entries == 0)[0]
        print("New Node Created: \n", self.entries, self.empty)

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic

    def compute_successors(self):
        successors = np.array([])

        vertical = self.vertical_move()
        successors = np.append(successors, vertical)

        horizontal = self.horizontal_move()
        successors = np.append(successors, horizontal)

        wrapping = self.wrapping_move()
        successors = np.append(successors, wrapping)

        diagonal = self.diagonal_move()
        successors = np.append(successors, diagonal)

        return successors

    def vertical_move(self):
        new_node = copy.deepcopy(self)
        new_node.empty[0] = (new_node.empty[0] + 1) % 2
        swap(new_node.entries, self.empty, new_node.empty)
        new_node.cost += 1
        new_node.parent = self
        return new_node

    def horizontal_move(self):
        new_nodes = np.array([])
        if self.empty[1] != 3:
            right_node = copy.deepcopy(self)
            right_node.cost += 1
            right_node.parent = self
            right_node.empty[1] = (right_node.empty[1] + 1) % 4
            swap(right_node.entries, self.empty, right_node.empty)
            new_nodes = np.append(new_nodes, right_node)

        if self.empty[1] != 0:
            left_node = copy.deepcopy(self)
            left_node.cost += 1
            left_node.parent = self
            left_node.empty[1] = (left_node.empty[1] - 1) % 4
            swap(left_node.entries, self.empty, left_node.empty)
            new_nodes = np.append(new_nodes, left_node)

        return new_nodes

    def wrapping_move(self):
        new_nodes = np.array([])
        if self.empty[1] == 0:
            right_node = copy.deepcopy(self)
            right_node.cost += 2
            right_node.parent = self
            right_node.empty[1] = (right_node.empty[1] + 3) % 4
            swap(right_node.entries, self.empty, right_node.empty)
            new_nodes = np.append(new_nodes, right_node)

        if self.empty[1] == 3:
            left_node = copy.deepcopy(self)
            left_node.cost += 2
            left_node.parent = self
            left_node.empty[1] = (left_node.empty[1] - 3) % 4
            swap(left_node.entries, self.empty, left_node.empty)
            new_nodes = np.append(new_nodes, left_node)

        return new_nodes

    def diagonal_move(self):
        new_nodes = np.array([])
        # right diagonal
        right_node = copy.deepcopy(self)
        right_node.cost += 3
        right_node.parent = self
        right_node.empty[0] = (right_node.empty[0] + 1) % 2
        right_node.empty[1] = (right_node.empty[1] + 1) % 4
        swap(right_node.entries, self.empty, right_node.empty)
        new_nodes = np.append(new_nodes, right_node)
        # left diagonal
        left_node = copy.deepcopy(self)
        left_node.cost += 3
        left_node.parent = self
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
