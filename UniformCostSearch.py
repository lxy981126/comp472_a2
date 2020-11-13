from Node import Node
from collections import deque
import numpy as np


class UniformCostSearch:
    def __init__(self, initial_node):
        self.open_list = deque()
        self.close_list = deque()
        self.initial = initial_node
        self.goal = None

    def start(self):
        self.open_list.append(self.initial)
        while True:
            if len(self.open_list) == 0:
                return

            current_node = self.open_list.pop()
            if is_goal(current_node):
                self.goal = current_node
                return

            successors = current_node.compute_successors()
            for successor in successors:
                node_in_open = self.find_in_open_list(successor)
                node_in_close = self.find_in_close_list(successor)
                if node_in_close is not None:
                    if node_in_close.cost > successor.cost:
                        self.close_list.remove(node_in_close)
                        self.open_list.append(successor)
                elif node_in_open is not None:
                    if node_in_open.cost > successor.cost:
                        node_in_open.parent = successor.parent
                        node_in_open.cost = successor.cost
                else:
                    self.open_list.append(successor)

            self.open_list = sorted(self.open_list, key=lambda n: n.cost, reverse=True)
            self.close_list.append(current_node)

    def find_in_open_list(self, target):
        for node in self.open_list:
            if np.array_equal(node.entries, target.entries):
                return node
        return None

    def find_in_close_list(self, target):
        for node in self.close_list:
            if np.array_equal(node.entries, target.entries):
                return node
        return None


def is_goal(node):
    goal1 = np.array([[1, 2, 3, 4], [5, 6, 7, 0]])
    goal2 = np.array([[1, 3, 5, 7], [2, 4, 6, 0]])
    if np.array_equal(node.entries, goal1) or np.array_equal(node.entries, goal2):
        return True
    else:
        return False
