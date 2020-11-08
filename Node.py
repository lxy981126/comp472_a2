import copy
import numpy as np


class Node:
    # cost: int, cost from root to current node
    # entries: 2*4 array
    # empty: 1D array with 2 elements for the empty tile
    def __init__(self, entries):
        self.cost = 0
        self.entries = entries
        for i in range(0, 1):
            for j in range(0, 3):
                if entries[i][j] == 0:
                    self.empty = [i, j]
        print("New Node Created: \n", self.entries, self.empty, "\n")

    def compute_successors(self):
        successors = np.array([])

        vertical = self.vertical_move()
        successors = np.append(successors, vertical)

        print("successors: ")
        [print(element.entries) for element in successors]
        return successors

    def vertical_move(self):
        new_node = copy.deepcopy(self)
        new_vertical_index = (new_node.empty[0] + 1) % 2
        new_node.empty[0] = new_vertical_index
        swap(new_node.entries, self.empty, new_node.empty)
        self.cost += 1
        return new_node

    def horizontal_move(self):
        new_node = copy.deepcopy(self)
        return new_node


def swap(array, index1, index2):
    temp = array[index1[0]][index1[1]]
    array[index1[0]][index1[1]] = array[index2[0]][index2[1]]
    array[index2[0]][index2[1]] = temp
    return array
