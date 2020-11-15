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
            # entry = np.array([[5, 2, 3, 4], [6, 0, 7, 1]])
            node = Node(entry, None)
            states = np.append(states, node)
    return states


def run_uniform_cost_search(initial, index):
    search_path = "./output/" + str(index) + "_ucs_search.txt"
    solution_path = "./output/" + str(index) + "_ucs_solution.txt"

    ucs = UniformCostSearch(initial)

    process = Process(target=ucs.start, args=(search_path, solution_path))
    process.start()
    process.join(timeout=60)
    # process.join()

    if process.is_alive():
        process.terminate()
        process_timeout(search_path, solution_path)


def process_timeout(search_path, solution_path):
    print("ucs timeout")
    with open(search_path, 'w') as file:
        file.write("No solution")
        file.close()
    with open(solution_path, 'w') as file:
        file.write("No solution")
        file.close()


if __name__ == '__main__':
    file_name = "samplePuzzles.txt"
    initial_nodes = process_input(file_name)
    i = 0

    for initial_node in initial_nodes:
        print(initial_node.entries)
        run_uniform_cost_search(initial_node, i)
        i += 1
