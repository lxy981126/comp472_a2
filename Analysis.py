import glob
import os


def analyze():
    if os.path.exists("./output/analysis.txt"):
        os.remove("./output/analysis.txt")
    analyze_ucs()
    analyze_gbfs()
    analyze_astar()


def analyze_ucs():
    ucs_search = glob.glob('./output/*ucs_search.txt')
    ucs_solution = glob.glob('./output/*ucs_solution.txt')
    analyze_search(ucs_search, 'UCS')
    analyze_solution(ucs_solution, 'UCS')
    with open('./output/analysis.txt', 'a+') as file:
        file.write('UCS optimal solution path guaranteed\n\n')


def analyze_gbfs():
    gbfs_h1_search = glob.glob('./output/*gbfs_h1_search.txt')
    gbfs_h1_solution = glob.glob('./output/*gbfs_h1_solution.txt')
    analyze_search(gbfs_h1_search, 'GBFS-h1')
    analyze_solution(gbfs_h1_solution, 'GBFS-h1')

    with open('./output/analysis.txt', 'a+') as file:
        file.write('\n\n')

    gbfs_h2_search = glob.glob('./output/*gbfs_h2_search.txt')
    gbfs_h2_solution = glob.glob('./output/*gbfs_h2_solution.txt')
    analyze_search(gbfs_h2_search, 'GBFS-h2')
    analyze_solution(gbfs_h2_solution, 'GBFS-h2')
    with open('./output/analysis.txt', 'a+') as file:
        file.write('GBFS optimal solution path NOT guaranteed\n\n')


def analyze_astar():
    astar_h1_search = glob.glob('./output/*astar_h1_search.txt')
    astar_h1_solution = glob.glob('./output/*astar_h1_solution.txt')
    analyze_search(astar_h1_search, 'A*-h1')
    analyze_solution(astar_h1_solution, 'A*-h1')

    with open('./output/analysis.txt', 'a+') as file:
        file.write('\n\n')

    astar_h2_search = glob.glob('./output/*astar_h2_search.txt')
    astar_h2_solution = glob.glob('./output/*astar_h2_solution.txt')
    analyze_search(astar_h2_search, 'A*-h2')
    analyze_solution(astar_h2_solution, 'A*-h2')
    with open('./output/analysis.txt', 'a+') as file:
        file.write('A* optimal solution path guaranteed\n\n')


def analyze_solution(solutions, algorithm):
    no_solution = 0
    total_length = 0
    total_cost = 0
    for solution in solutions:
        with open(solution, 'r') as file:
            line = file.readline()
            if line == 'No solution':
                no_solution += 1
                continue
            else:
                split_list = line.split(' ')
                total_cost += int(split_list[1])
                total_length += sum(1 for line in file)
    avg_length = total_length / (50 - no_solution) if no_solution != 50 else total_length
    avg_cost = total_cost / (50 - no_solution) if no_solution != 50 else total_cost
    with open('./output/analysis.txt', 'a+') as file:
        file.write(algorithm + ' Total length of solution paths: ' + str(total_length) + '\n')
        file.write(algorithm + ' Average length of solution paths: ' + str(avg_length) + '\n')
        file.write(algorithm + ' Total cost: ' + str(total_cost) + '\n')
        file.write(algorithm + ' Average cost: ' + str(avg_cost) + '\n')
        file.write(algorithm + ' Number of no solution: ' + str(no_solution) + '\n')


def analyze_search(searches, algorithm):
    no_solution = 0
    total_length = 0
    total_time = 0
    for search in searches:
        with open(search, 'r') as file:
            for line in file:
                if line == 'No solution':
                    no_solution += 1
                else:
                    total_length += 1
                    total_time += float(line) if ' ' not in line else 0
    avg_length = total_length / (50 - no_solution) if no_solution != 50 else total_length
    avg_time = total_time / (50 - no_solution) if no_solution != 50 else total_time
    with open('./output/analysis.txt', 'a+') as file:
        file.write(algorithm + ' Total length of search paths: ' + str(total_length) + '\n')
        file.write(algorithm + ' Average length of search paths: ' + str(avg_length) + '\n')
        file.write(algorithm + ' Total time: ' + str(total_time) + '\n')
        file.write(algorithm + ' Average time: ' + str(avg_time) + '\n')


if __name__ == '__main__':
    analyze()

