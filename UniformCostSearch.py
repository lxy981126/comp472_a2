from Node import Node
import numpy as np


class UniformCostSearch:
    def __init__(self, initial_entries, goal_entries):
        self.open_list = np.array([])
        self.close_list = np.array([])
        self.initial = Node(initial_entries)
        self.goal = Node(goal_entries)

    def start(self):
        np.append(self.open_list, self.initial)
        sorted(self.open_list, key=lambda node: node.cost)
        [print(element.entries) for element in self.open_list]
