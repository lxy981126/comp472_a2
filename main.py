from Node import Node
from UniformCostSearch import UniformCostSearch
from multiprocessing import Process
import numpy as np


def process_input(input_file):
    states = np.array([])
    with open(input_file, 'r') as file:
        for line in file:
            string_list = str.split(line)
            int_list = [int(element) for element in string_list]
            entry = np.ndarray.reshape(np.asarray(int_list), 2, 4)
            node = Node(entry, None)
            states = np.append(states, node)
            print(entry)

    return states


def extract_solution_path(node, solution_path):
    file = open(solution_path, 'w')
    while node is not None:
        state = np.ndarray.reshape(node.entries, 1, 8)
        np.savetxt(file, state, delimiter=' ', fmt='%i')
        node = node.parent
    file.close()


def extract_search_path(close_list, search_path):
    file = open(search_path, 'w')
    for node in close_list:
        state = np.ndarray.reshape(node.entries, 1, 8)
        np.savetxt(file, state, delimiter=' ', fmt='%i')
    file.close()


def run_uniform_cost_search(initial, index):
    search_path = "./output/" + str(index) + "_ucs_search.txt"
    solution_path = "./output/" + str(index) + "_ucs_solution.txt"

    ucs = UniformCostSearch(initial)
    process = Process(target=ucs.start)
    process.start()
    process.join(timeout=60)

    if process.is_alive():
        process.terminate()
        with open(search_path, 'w') as file:
            file.write("Not solution")
            file.close()
        with open(solution_path, 'w') as file:
            file.write("No solution")
            file.close()
        print("ucs timeout")
    else:
        extract_search_path(ucs.close_list, search_path)
        extract_solution_path(ucs.goal, solution_path)


if __name__ == '__main__':
    file_name = "samplePuzzles.txt"
    initial_nodes = process_input(file_name)
    i = 0

    for initial_node in initial_nodes:
        print(initial_node.entries)
        run_uniform_cost_search(initial_node, i)
        i += 1
