from Node import Node
from collections import deque


class GreedBestFirstSearch:
    def __init__(self, initial_entries, goal_entries):
        self.open_list = deque()
        self.close_list = deque()
        self.initial = Node(initial_entries, None)
        self.goal = goal_entries

