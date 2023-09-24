from utils import get_game_table, print_algorithm_name
from UCS import UCS
from State import State
from BestFirstSearch import BestFirstSearch
from AStar import AStar
from DFS import DFS
from BFS import BFS
from AlgorithmType import AlgorithmType

# Get Input
rows, cols = list(map(lambda a: int(a), input().split(' ')))
costs, config, robot_location, butters_count = get_game_table(rows, cols)

initial_state = State(config, robot_location, butters_count)

map_algorithm_name_to_class = {
    AlgorithmType.UCS: UCS,
    AlgorithmType.BEST_FIRST_SEARCH: BestFirstSearch,
    AlgorithmType.A_STAR: AStar,
    AlgorithmType.BFS: BFS,
    AlgorithmType.DFS: DFS,
}

for [AlgorithmName, AlgorithmClass] in map_algorithm_name_to_class.items():
    print_algorithm_name(AlgorithmName)
    algorithm_answer = AlgorithmClass(costs, initial_state)
    print(algorithm_answer)
