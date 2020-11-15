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

    def start(self, search_path, solution_path):
        heapq.heappush(self.open_list, (self.initial.cost, self.initial))
        while True:
            if len(self.open_list) == 0:
                return

            current_node = heapq.heappop(self.open_list)
            if General.is_goal(current_node[1]):
                General.extract_solution_path(current_node[1], solution_path)
                General.extract_search_path(self.close_list, search_path)
                return

            successors = current_node[1].compute_successors()
            for successor in successors:
                node_in_open = General.find_if_in_list(self.open_list, successor)
                node_in_close = General.find_if_in_list(self.close_list, successor)
                if node_in_open is not None:
                    if node_in_open[0] > successor.cost:
                        self.open_list.remove(node_in_open)
                        heapq.heapify(self.open_list)
                        heapq.heappush(self.open_list, (successor.cost, successor))
                elif node_in_close is None:
                    heapq.heappush(self.open_list, (successor.cost, successor))

            self.close_list.append(current_node)


