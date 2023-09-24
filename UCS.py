from queue import PriorityQueue
from UCSNode import UCSNode
from State import State
from Successor import Successor
from Answer import Answer
from AlgorithmType import AlgorithmType


def UCS(costs: list[list[int]], initial_state: State):
    pq: PriorityQueue[UCSNode] = PriorityQueue()
    successor = Successor(costs)
    visited: dict = dict()

    initial_node = UCSNode(initial_state, 0)
    pq.put(initial_node)

    while not (pq.empty()):
        frontier = pq.get()
        # Check if we've found the solution
        if (frontier.state.butters_count == 0):
            return Answer(frontier.state.movements, frontier.g)

        generated_states = successor.generate(
            frontier.state, AlgorithmType.UCS)

        for generated_data in generated_states:

            generated_state = generated_data[0]

            # Check if the state is duplicate and has seen before
            state_hash = generated_state.hash()
            if (state_hash in visited):
                continue
            # Mark the state (config & robot_location) as visited
            visited[state_hash] = True
            # Add node to the priority queue
            new_node = UCSNode(
                generated_state, frontier.g + generated_data[1])

            pq.put(new_node)

    return "can’t pass the butter"
