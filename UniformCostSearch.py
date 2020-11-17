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
        heapq.heappush(self.open_list, (self.initial.g, self.initial))
        while True:
            if len(self.open_list) == 0:
                return

            current_node = heapq.heappop(self.open_list)
            if General.is_goal(current_node[1]):
                General.extract_solution_path(current_node[1], solution_path)
                General.extract_search_path(self.close_list, search_path)
                return

            successors = compute_successors(current_node[1])
            for successor in successors:
                node_in_open = General.find_if_in_list(self.open_list, successor)
                node_in_close = General.find_if_in_list(self.close_list, successor)
                if node_in_open is not None:
                    if node_in_open.g > successor.g:
                        self.open_list.remove(node_in_open)
                        heapq.heapify(self.open_list)
                        heapq.heappush(self.open_list, (successor.g, successor))
                elif node_in_close is None:
                    heapq.heappush(self.open_list, (successor.g, successor))

            self.close_list.append(current_node)


def compute_successors(node):
    successors = np.array([])

    vertical = node.vertical_move()
    for element in vertical:
        element.g = node.g + 1
    successors = np.append(successors, vertical)

    horizontal = node.horizontal_move()
    for element in horizontal:
        element.g = node.g + 1
    successors = np.append(successors, horizontal)

    wrapping = node.wrapping_move()
    for element in wrapping:
        element.g = node.g + 2
    successors = np.append(successors, wrapping)

    diagonal = node.diagonal_move()
    for element in diagonal:
        element.g = node.g + 3
    successors = np.append(successors, diagonal)

    return successors

