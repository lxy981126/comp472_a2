import General
import numpy as np
import heapq


class GreedBestFirstSearch:
    def __init__(self, initial_node):
        self.open_list = []
        heapq.heapify(self.open_list)
        self.close_list = []
        self.initial = initial_node
        self.goal = None

    def start(self, heuristic, search_path, solution_path):
        self.initial.h = heuristic(self.initial)
        heapq.heappush(self.open_list, (self.initial.h, self.initial))
        while True:
            if len(self.open_list) == 0:
                return

            current_node = heapq.heappop(self.open_list)
            if General.is_goal(current_node[1]):
                General.extract_solution_path(current_node[1], solution_path)
                General.extract_search_path(self.close_list, search_path)
                return

            successors = compute_successors(current_node[1], heuristic)
            for successor in successors:
                node_in_open = General.find_if_in_list(self.open_list, successor)
                node_in_close = General.find_if_in_list(self.close_list, successor)
                if node_in_open is not None:
                    if node_in_open.h > successor.h:
                        self.open_list.remove(node_in_open)
                        heapq.heapify(self.open_list)
                        heapq.heappush(self.open_list, (successor.h, successor))
                elif node_in_close is None:
                    heapq.heappush(self.open_list, (successor.h, successor))
            self.close_list.append(current_node)


def compute_successors(node, heuristic):
    successors = np.array([])

    vertical = node.vertical_move()
    vertical.h = heuristic(vertical)
    successors = np.append(successors, vertical)

    horizontal = node.horizontal_move()
    for element in horizontal:
        element.h = heuristic(element)
    successors = np.append(successors, horizontal)

    wrapping = node.wrapping_move()
    for element in wrapping:
        element.h = heuristic(element)
    successors = np.append(successors, wrapping)

    diagonal = node.diagonal_move()
    for element in diagonal:
        element.h = heuristic(element)
    successors = np.append(successors, diagonal)

    return successors



