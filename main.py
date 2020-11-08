from Node import Node
from UniformCostSearch import UniformCostSearch
import numpy as np


def process_input(input_file):
    file = open(input_file, 'r')

    string = file.readline()
    # string = file.readline()
    print(string)
    string_list = str.split(string)
    int_list = [int(element) for element in string_list]
    arr = np.ndarray.reshape(np.asarray(int_list), 2, 4)
    node = Node(arr, None)

    return node


# def extract_solution(initial, node):


if __name__ == '__main__':
    # file_name = "samplePuzzles.txt" # input("Enter input file: ")
    # n = process_input(file_name)
    initial_state = np.array([[4, 2, 3, 1], [5, 6, 7, 0]])
    goal_state = np.array([[4, 2, 3, 0], [5, 6, 7, 1]])
    UniformCostSearch(initial_state, goal_state).start()
