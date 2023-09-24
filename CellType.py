from enum import Enum


class CellType(str, Enum):
    EMPTY = "0"
    BUTTER = "b"
    POINT = "p"
    BlOCK = "x"
    ROBOT = "r"

    def __str__(self):
        return str(self.value)
