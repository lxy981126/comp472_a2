from Node import Node
from UniformCostSearch import UniformCostSearch
from GreedyBestFirstSearch import GreedBestFirstSearch
from AStar import AStar
from multiprocessing import Process
import numpy as np
import time
import random
import General


def generate_inputs(path):
    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    with open(path, 'w') as file:
        for index in range(0, 50):
            random.shuffle(arr)
            np.savetxt(file, [arr], delimiter=' ', fmt='%i')
            file.flush()


def process_input():
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


def run_uniform_cost_search():
    search_path = "./output/" + str(i) + "_ucs_search.txt"
    solution_path = "./output/" + str(i) + "_ucs_solution.txt"
    ucs = UniformCostSearch(initial_node)

    process = Process(target=ucs.start, args=(search_path, solution_path))
    start_time = time.time()
    process.start()
    process.join(timeout=60)
    # process.join()
    exec_time = time.time() - start_time
    if process.is_alive():
        process.terminate()
        print("ucs: timeout")
        General.process_failure(search_path, solution_path)
    else:
        with open(search_path, 'a') as file:
            file.write(str(exec_time))


def run_greedy_best_first_search(heuristic):
    h = 1 if heuristic == General.h1 else 2
    search_path = "./output/" + str(i) + "_gbfs_h" + str(h) + "_search.txt"
    solution_path = "./output/" + str(i) + "_gbfs_h" + str(h) + "_solution.txt"

    gbfs = GreedBestFirstSearch(initial_node)
    process = Process(target=gbfs.start, args=(heuristic, search_path, solution_path))
    start_time = time.time()
    process.start()
    process.join(timeout=60)
    # process.join()
    exec_time = time.time() - start_time
    if process.is_alive():
        process.terminate()
        print("gbfs: timeout")
        General.process_failure(search_path, solution_path)
    else:
        with open(search_path, 'a') as file:
            file.write(str(exec_time))


def run_a_star(heuristic):
    h = 1 if heuristic == General.h1 else 2
    search_path = "./output/" + str(i) + "_astar_h" + str(h) + "_search.txt"
    solution_path = "./output/" + str(i) + "_astar_h" + str(h) + "_solution.txt"

    astar = AStar(initial_node)
    process = Process(target=astar.start, args=(heuristic, search_path, solution_path))
    start_time = time.time()
    process.start()
    process.join(timeout=60)
    # process.join()
    exec_time = time.time() - start_time
    if process.is_alive():
        process.terminate()
        print("a*: timeout")
        General.process_failure(search_path, solution_path)
    else:
        with open(search_path, 'a') as file:
            file.write(str(exec_time))


if __name__ == '__main__':
    input_file = "inputs.txt"
    generate_inputs(input_file)
    initial_nodes = process_input()
    i = 0

    for initial_node in initial_nodes:
        print(initial_node.entries)
        run_uniform_cost_search()
        run_greedy_best_first_search(General.h1)
        run_a_star(General.h1)
        run_greedy_best_first_search(General.h2)
        run_a_star(General.h2)
        i += 1
