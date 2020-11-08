from Node import Node
from collections import deque
import numpy as np


class UniformCostSearch:
    def __init__(self, initial_entries, goal_entries):
        self.open_list = deque()
        self.close_list = deque()
        self.initial = Node(initial_entries, None)
        self.goal = goal_entries

    def start(self):
        self.open_list.append(self.initial)
        while True:
            if len(self.open_list) == 0:
                return None

            current_node = self.open_list.pop()
            successors = current_node.compute_successors()
            for successor in successors:
                node = self.is_success_in_open_list(successor)
                if node is not None:
                    if node.cost > successor.cost:
                        node.parent = successor.parent
                        node.cost = successor.cost
                else:
                    self.open_list.append(successor)

            self.open_list = sorted(self.open_list, key=lambda n: n.cost, reverse=True)
            print("open list:\n")
            [print(element.entries) for element in self.open_list]

            self.close_list.append(current_node)
            if np.array_equal(current_node.entries, self.goal):
                return current_node

    def is_success_in_open_list(self, successor):
        for node in self.open_list:
            if np.array_equal(node.entries, successor.entries):
                return node
        return None


