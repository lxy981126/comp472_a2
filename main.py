from Node import Node
from UniformCostSearch import UniformCostSearch
from GreedyBestFirstSearch import GreedBestFirstSearch
from multiprocessing import Process
import numpy as np
import General


def process_input():
    states = np.array([])
    with open(input_file, 'r') as file:
        for line in file:
            string_list = str.split(line)
            int_list = [int(element) for element in string_list]
            # entry = np.ndarray.reshape(np.asarray(int_list), 2, 4)
            entry = np.array([[5, 2, 3, 4], [6, 0, 7, 1]])
            node = Node(entry, None)
            states = np.append(states, node)
    return states


def run_uniform_cost_search():
    search_path = "./output/" + str(i) + "_ucs_search.txt"
    solution_path = "./output/" + str(i) + "_ucs_solution.txt"
    ucs = UniformCostSearch(initial_node)

    process = Process(target=ucs.start, args=(search_path, solution_path))
    process.start()
    process.join(timeout=60)
    if process.is_alive():
        process.terminate()
        process_timeout(search_path, solution_path)


def run_greedy_best_first_search():
    search_path = "./output/" + str(i) + "_gbfs_search.txt"
    solution_path = "./output/" + str(i) + "_gbfs_solution.txt"

    gbfs = GreedBestFirstSearch(initial_node)
    process = Process(target=gbfs.start, args=(General.h1, search_path, solution_path))
    process.start()
    # process.join(timeout=60)
    process.join()
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
    input_file = "samplePuzzles.txt"
    initial_nodes = process_input()
    i = 0

    for initial_node in initial_nodes:
        print(initial_node.entries)

        # run_uniform_cost_search()
        run_greedy_best_first_search()
        i += 1
