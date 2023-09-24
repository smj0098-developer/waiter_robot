from queue import PriorityQueue
from AStarNode import AStarNode
from State import State
from Successor import Successor
from Answer import Answer
from AlgorithmType import AlgorithmType


def AStar(costs: list[list[int]], initial_state: State):
    pq: PriorityQueue[AStarNode] = PriorityQueue()
    successor = Successor(costs)
    best_path_cost_yet: dict = dict()

    initial_node = AStarNode(initial_state, 0, 0)
    pq.put(initial_node)

    while not (pq.empty()):
        frontier = pq.get()
        # Check if we've found the solution
        if (frontier.state.butters_count == 0):
            return Answer(frontier.state.movements, frontier.g)

        generated_states = successor.generate(
            frontier.state, AlgorithmType.A_STAR)

        for generated_data in generated_states:

            generated_state = generated_data[0]

            state_hash = generated_state.hash()
            # if the state is duplicate and has been seen before AND if the new "path's cost + heuristic value"
            # for a state is more than the previous "path's cost + heuristic value" for the same state, ignore the new state

            if (state_hash in best_path_cost_yet and best_path_cost_yet[state_hash] <= generated_data[1]+frontier.g+generated_data[2]):
                continue
            # Mark the state (config & robot_location) as visited
            best_path_cost_yet[state_hash] = generated_data[1] + \
                frontier.g + generated_data[2]
            # Add node to the priority queue
            new_node = AStarNode(
                generated_state, frontier.g + generated_data[1], generated_data[2])

            pq.put(new_node)

    return "can’t pass the butter"
