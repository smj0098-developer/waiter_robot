from queue import LifoQueue
from State import State
from Successor import Successor
from Answer import Answer
from DFSNode import DFSNode
from AlgorithmType import AlgorithmType


def DFS(costs: list[list[int]], initial_state: State):
    pq: LifoQueue[DFSNode] = LifoQueue()
    successor = Successor(costs)
    visited: dict = dict()

    initial_node = DFSNode(initial_state, 0)
    pq.put(initial_node)

    while not (pq.empty()):
        frontier = pq.get()
        # Check if we've found the solution
        if (frontier.state.butters_count == 0):
            return Answer(frontier.state.movements, frontier.g)

        generated_states = successor.generate(
            frontier.state, AlgorithmType.DFS)

        for generated_data in generated_states:

            generated_state = generated_data[0]

            # Check if the state is duplicate and has seen before
            state_hash = generated_state.hash()
            if (state_hash in visited):
                continue
            # Mark the state (config & robot_location) as visited
            visited[state_hash] = True
            # Add node to the priority queue
            new_node = DFSNode(
                generated_state, frontier.g + generated_data[1])

            pq.put(new_node)

    return "can’t pass the butter"
