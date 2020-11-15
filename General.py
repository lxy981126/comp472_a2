import numpy as np


goal1 = np.array([[1, 2, 3, 4], [5, 6, 7, 0]])
goal2 = np.array([[1, 3, 5, 7], [2, 4, 6, 0]])


def is_goal(node):
    if np.array_equal(node.entries, goal1) or np.array_equal(node.entries, goal2):
        return True
    else:
        return False


def h0(node, target):
    if np.array_equal(node.entries, target):
        return 0
    else:
        return 1


# Improved version of Manhattan Distance
# Cost to adjacent tile = 1
# Cost to non-adjacent tile = 2, because other tiles need to move first to unblock it
def h1(node):
    entry = node.entries
    distance1 = np.inf
    distance2 = np.inf
    counter = 0

    return min(distance1, distance2)


def extract_solution_path(node, solution_path):
    with open(solution_path, 'w') as file:
        while node is not None:
            state = np.ndarray.reshape(node.entries, 1, 8)
            np.savetxt(file, state, delimiter=' ', fmt='%i')
            file.flush()
            node = node.parent
        file.close()


def extract_search_path(close_list, search_path):
    with open(search_path, 'w') as file:
        for node in close_list:
            state = np.ndarray.reshape(node.entries, 1, 8)
            np.savetxt(file, state, delimiter=' ', fmt='%i')
            file.flush()
        file.close()

