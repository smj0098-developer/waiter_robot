class Answer:
    def __init__(self, movements, cost):
        self.movements = movements
        self.cost = cost

    def __str__(self):
        path = ""

        map_movement_to_direction = {
            (0, 1): "R",
            (0, -1): "L",
            (1, 0): "D",
            (-1, 0): "U"
        }

        for movement in self.movements:
            path += f"{map_movement_to_direction[movement]} "

        return f"{path}\n{self.cost}\n{len(self.movements)}"
