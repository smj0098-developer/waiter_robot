from State import State
from AlgorithmType import AlgorithmType

Cost = int
Heuristic = int


class Successor:
    def __init__(self, costs: list[list[int]]):
        self.costs = costs

    def generate(self, state: State, algoName) -> list[tuple[State, Cost, Heuristic]]:
        states: list[tuple[State, Cost, Heuristic]] = list()

        movements = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for movement in movements:
            if (state.is_movement_valid(movement)):
                # New state is a fresh copy of state with updated data
                new_state = state.move(movement)
                rb = new_state.robot_location

                h = None
                g = self.costs[rb[0]][rb[1]]
                if algoName == AlgorithmType.BEST_FIRST_SEARCH or algoName == AlgorithmType.A_STAR:
                    h = new_state.heuristic()

                states.append([new_state, g, h])

        return states
