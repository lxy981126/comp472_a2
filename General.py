import numpy as np
import math


goal1 = np.array([[1, 2, 3, 4], [5, 6, 7, 0]])
goal2 = np.array([[1, 3, 5, 7], [2, 4, 6, 0]])


def is_goal(node):
    if np.array_equal(node.entries, goal1) or np.array_equal(node.entries, goal2):
        return True
    else:
        return False


# Monotonic
def h0(node):
    if np.array_equal(node.entries, goal1) or np.array_equal(node.entries, goal2):
        return 0
    else:
        return 1


# Sum of Euclidean distances of all tiles
# Non-Monotonic
def h1(node):
    entry = node.entries
    distance1 = 0
    distance2 = 0
    for i in range(0, 2):
        for j in range(0, 4):
            index1 = np.argwhere(goal1 == entry[i][j])[0]
            distance1 += math.pow(index1[0] - i, 2) + math.pow(index1[1] - j, 2)
            index2 = np.argwhere(goal2 == entry[i][j])[0]
            distance2 += math.pow(index2[0] - i, 2) + math.pow(index2[1] - j, 2)
    return math.sqrt(min(distance1, distance2))


# Number of mismatched columns
# Monotonic
def h2(node):
    entry = node.entries
    diff1 = 0
    diff2 = 0
    for i in range(0, 4):
        if not np.array_equal(entry[:, i], goal1[:, i]):
            diff1 += 1
        if not np.array_equal(entry[:, i], goal2[:, i]):
            diff2 += 1
    return min(diff1, diff2)


def extract_solution_path(node, solution_path):
    with open(solution_path, 'w') as file:
        while node is not None:
            values = np.array([[node.f, node.g, node.h]])
            state = np.ndarray.reshape(node.entries, 1, 8)
            values = np.append(values, state)
            np.savetxt(file, [values], delimiter=' ', fmt='%i')
            file.flush()
            node = node.parent
        file.close()


def extract_search_path(close_list, search_path):
    with open(search_path, 'w') as file:
        for node in close_list:
            state = np.ndarray.reshape(node[1].entries, 1, 8)
            np.savetxt(file, state, delimiter=' ', fmt='%i')
            file.flush()
        file.close()


def process_failure(search_path, solution_path):
    with open(search_path, 'w') as file:
        file.write("No solution")
        file.close()
    with open(solution_path, 'w') as file:
        file.write("No solution")
        file.close()


def find_if_in_list(list_to_search, node):
    next((x for x in list_to_search if np.array_equal(x[1].entries, node.entries)), None)


