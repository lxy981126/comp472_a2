import General
import numpy as np
import heapq


class AStar:
    def __init__(self, initial_node):
        self.open_list = []
        heapq.heapify(self.open_list)
        self.close_list = []
        self.initial = initial_node

    def start(self, heuristic, search_path, solution_path):
        self.initial.h = heuristic(self.initial)
        self.initial.f = self.initial.h + self.initial.g
        heapq.heappush(self.open_list, (self.initial.f, self.initial))
        while True:
            if len(self.open_list) == 0:
                General.process_failure(search_path, solution_path)
                return

            current_node = heapq.heappop(self.open_list)
            if General.is_goal(current_node[1]):
                General.extract_solution_path(current_node[1], solution_path)
                General.extract_search_path(self.close_list, search_path)
                return

            successors = compute_successors(current_node[1], heuristic)
            for successor in successors:
                successor.h = heuristic(successor)
                successor.f = successor.h + successor.g
                node_in_open = General.find_if_in_list(self.open_list, successor)
                node_in_close = General.find_if_in_list(self.close_list, successor)
                if node_in_close is not None:
                    if node_in_close.f > successor.f:
                        self.close_list.remove(node_in_close)
                        heapq.heappush(self.open_list, (successor.f, successor))
                elif node_in_open is not None:
                    if node_in_open.f > successor.f:
                        self.open_list.remove(node_in_open)
                        heapq.heapify(self.open_list)
                        heapq.heappush(self.open_list, (successor.f, successor))
                else:
                    heapq.heappush(self.open_list, (successor.f, successor))
            self.close_list.append(current_node)


def compute_successors(node, heuristic):
    successors = np.array([])

    vertical = node.vertical_move()
    vertical.g = node.g + 1
    vertical.h = heuristic(vertical)
    vertical.f = vertical.g + vertical.h
    successors = np.append(successors, vertical)

    horizontal = node.horizontal_move()
    for element in horizontal:
        element.g = node.g + 1
        element.h = heuristic(element)
        element.f = element.g + element.h
    successors = np.append(successors, horizontal)

    wrapping = node.wrapping_move()
    for element in wrapping:
        element.g = node.g + 2
        element.h = heuristic(element)
        element.f = element.g + element.h
    successors = np.append(successors, wrapping)

    diagonal = node.diagonal_move()
    for element in diagonal:
        element.g = node.g + 3
        element.h = heuristic(element)
        element.f = element.g + element.h
    successors = np.append(successors, diagonal)

    return successors



