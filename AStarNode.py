from Node import Node
from State import State


class AStarNode(Node):
    # Contains an State as well as it's G and it's H
    def __init__(self, state: State, g: int, h: int):
        super().__init__(state)
        self.g = g
        self.h = h

    def __str__(self):
        return f"{self.state} g: {self.g}"

    def __lt__(self, other):
        return self.h+self.g < other.h+other.g
