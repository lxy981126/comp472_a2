from Node import Node
import General
import numpy as np
import heapq


class UniformCostSearch:
    def __init__(self, initial_node):
        self.open_list = []
        heapq.heapify(self.open_list)
        self.close_list = []
        self.initial = initial_node
        setattr(Node, "__lt__", lambda node, other: node.cost < other.cost)

    def start(self, search_path, solution_path):
        heapq.heappush(self.open_list, self.initial)
        while True:
            if len(self.open_list) == 0:
                return

            current_node = heapq.heappop(self.open_list)
            if General.is_goal(current_node):
                General.extract_solution_path(current_node, solution_path)
                General.extract_search_path(self.close_list, search_path)
                return

            successors = current_node.compute_successors()
            for successor in successors:
                node_in_open = self.find_in_open_list(successor)
                node_in_close = self.find_in_close_list(successor)
                if node_in_open is not None:
                    if node_in_open.cost > successor.cost:
                        node_in_open.parent = successor.parent
                        node_in_open.cost = successor.cost
                        self.open_list.sort()
                elif node_in_close is None:
                    heapq.heappush(self.open_list, successor)

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


