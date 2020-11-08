from Node import Node
import numpy as np


def process_input(input_file):
    file = open(input_file, 'r')

    string = file.readline()
    string_list = str.split(string)
    int_list = [int(element) for element in string_list]
    arr = np.ndarray.reshape(np.asarray(int_list), 2, 4)
    node = Node(arr)

    return node


if __name__ == '__main__':
    file_name = "samplePuzzles.txt" # input("Enter input file: ")
    n = process_input(file_name)
    n.compute_successors()
