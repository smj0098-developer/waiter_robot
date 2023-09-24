from utils import tuple_sum, hash_iterable, get_manhattan_distance
from tabulate import tabulate
from CellType import CellType
from copy import deepcopy

# Contains table config (butters and points locations) as well as robot location, butters_count and a list of movements that ended up to current state


class State:
    def __init__(self, config: list[list[int]], robot_location: tuple[int, int], butters_count: int, movements: list[tuple[int, int]] = []):
        self.config = config
        self.robot_location = robot_location
        self.butters_count = butters_count
        self.movements = movements
        return

    def __str__(self):
        return f"{tabulate(self.config)} {tabulate(self.movements)} rb: {self.robot_location}  butters: {self.butters_count}"

    def get_cell_value(self, location: tuple[int, int]):
        return self.config[location[0]][location[1]]

    def set_cell(self, location: tuple[int, int], new_value: CellType):
        cell_value = self.get_cell_value(location)
        if (cell_value == CellType.BUTTER):
            self.butters_count -= 1
        if (new_value == CellType.BUTTER):
            self.butters_count += 1
        self.config[location[0]][location[1]] = new_value

    def is_movement_valid(self, movement: tuple[int]) -> bool:
        next_cell_location = tuple_sum(self.robot_location, movement)
        double_next_cell_location = tuple_sum(next_cell_location, movement)

        next_cell_value = self.get_cell_value(next_cell_location)
        double_next_cell_value = self.get_cell_value(double_next_cell_location)

        is_next_cell_empty = next_cell_value == CellType.EMPTY or next_cell_value == CellType.POINT
        is_double_next_cell_empty = double_next_cell_value == CellType.EMPTY or double_next_cell_value == CellType.POINT

        # Check whether or not we can move to the next location:
        # 1. If the next location is empty (or point)
        # 2. If the next location is butter and the location after that is empty (or point)
        if (
            is_next_cell_empty
            or
            (next_cell_value == CellType.BUTTER and is_double_next_cell_empty)
        ):
            return True

        return False

    # Returns a new state with a deepcopy of updated config, robot_location, movements and butters_count
    def move(self, movement: tuple[int, int]):
        next_cell_location = tuple_sum(self.robot_location, movement)
        double_next_cell_location = tuple_sum(next_cell_location, movement)

        # Edit reference of movements array and add a movement to the chain
        new_movements = self.movements[:]
        new_movements.append(movement)

        config_copy = deepcopy(self.config)

        # Create new state with new robot location and a deepcopy of latest config to separate it from the current old config
        new_state = State(config_copy,
                          next_cell_location,
                          self.butters_count,
                          new_movements)

        next_cell_value = new_state.get_cell_value(next_cell_location)

        if (next_cell_value == CellType.BUTTER):
            double_next_cell_value = new_state.get_cell_value(
                double_next_cell_location)

            # Remove butter from its location
            new_state.set_cell(next_cell_location, CellType.EMPTY)

            if (double_next_cell_value == CellType.POINT):
                # Set double next cell to a Block cell
                new_state.set_cell(double_next_cell_location, CellType.BlOCK)
            else:
                # Move the butter to the next location
                new_state.set_cell(double_next_cell_location, CellType.BUTTER)

        return new_state

    def hash(self):
        return f"{hash_iterable(self.config)}_{hash_iterable(self.robot_location)}"

    def heuristic(self):
        locations = dict()
        locations["r"] = [self.robot_location]
        locations["b"] = []
        locations["p"] = []
        i = 0

        for row in self.config:
            j = 0
            for cell in row:
                if cell == "b" or cell == "p":
                    locations[cell].append((i, j))
                j += 1
            i += 1

        totalH = 0
        # compute all distances from butters to points
        butter_point_pairs = {}
        for b in locations["b"]:
            for p in locations["p"]:
                butter_point_pairs[(b, p)] = get_manhattan_distance(b, p)
        # find the nearest point for each butter and return their manhattan distances from that point

        while (len(butter_point_pairs) != 0):

            # sort butter_point_pairs so that we can choose the nearest point for our butter
            butter_point_pairs = sorted(
                butter_point_pairs.items(), key=lambda x: x[1])
            current = butter_point_pairs.pop(0)
            for i in butter_point_pairs:
                # remove other occurrences of current butter and point
                if i[0][1] == current[0][1] or i[0][0] == current[0][0]:
                    butter_point_pairs = dict(butter_point_pairs)
                    butter_point_pairs.pop(i[0])

            totalH += current[1]

        # compute the distance of robot from the farthest butter
        robot_butter_pairs = {}
        for b in locations["b"]:
            robot_butter_pairs[(self.robot_location, b)] = get_manhattan_distance(
                self.robot_location, b)

        if len(robot_butter_pairs.values()) != 0:
            totalH += max(robot_butter_pairs.values())

        return totalH
