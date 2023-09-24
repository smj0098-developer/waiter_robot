from enum import Enum


class AlgorithmType(str, Enum):
    BFS = "BFS"
    DFS = "DFS"
    IDS = "IDS"
    UCS = "UCS"
    A_STAR = "AStar"
    BEST_FIRST_SEARCH = "BestFirstSearch"

    def __str__(self):
        return str(self.value)
