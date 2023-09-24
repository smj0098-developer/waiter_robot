from Node import Node
from State import State


class DFSNode(Node):
    # Contains an State as well as it's G
    def __init__(self, state: State, g: int):
        super().__init__(state)
        self.g = g

    def __str__(self):
        return f"{self.state} g: {self.g}"
