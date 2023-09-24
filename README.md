# AI Course: Waiter Robot Project

## Table of Contents <!-- omit in toc -->

- [Project Overview](#project-overview)
- [Parsing the Input](#parsing-the-input)
- [Classes and Methods](#classes-and-methods)
  - [`State` Class](#state-class)
  - [`Node` Class](#node-class)
  - [`Successor` Class](#successor-class)
  - [`utils.py`](#utilspy)
- [Algorithms](#algorithms)
  - [`UCS`](#ucs)
  - [`BestFirstSearch`](#bestfirstsearch)
  - [`A*`](#a)
  - [`BFS`](#bfs)
  - [`DFS`](#dfs)

## Project Overview

You can read [Project Statement](https://github.com/theMasix/waiter_robot/blob/main/project_statement.pdf) to become informed of the project overview, requirements and other detail.

## Parsing the Input

We use `get_game_table` util to construct variables based on inputs.

We create following variables:

- `costs`: A 2d list of costs. Each item shows the cost of moving to that location
- `config`: A 2d list of remaining elements of the game map. Each item is one of the following character:
  - `x`: meaning that the location is blocked
  - `b`: butter location
  - `p`: point location
  - `0`: empty location
- `robot_location`: A tuple of `(row, col)` of the initial robot location
- `butters_count`: A number representing the initial counts of butter on the table

## Classes and Methods

### `State` Class

It contains the actual `config` map, `robot_location`, prior `movements` and `butters_count`. The last one can be computed from the `config` map, but we store it separately to reduce the time complexity of the application, It's time consuming to compute it in every usage.

#### `get_cell_value` method

- Inputs: `location`
- Returns: `str`

Returns the cell value of the requested location

#### `set_cell` method

- Inputs: `location`, `new_value`
- Returns: `None`

Set value of the requested location as `new_value` param
Also, modifies the corresponding `butters_count` value.

#### `is_movement_valid` method

- Inputs: `movement`
- Returns: `bool`

Check whether we can move to the next location, we can move to the next location if one of these conditions occurs:

1. If the next location is empty (or point)
2. If the next location is butter and the location after that is empty (or point)

#### `move` method

Inputs: `movement`
Returns: A fresh new state with a deepcopy of updated `config`, `robot_location`, `movements` and `butters_count`

Do the actual robot movement based on its attributes.

If a `butter` goes on a `point` location, it updates the location as `block` so we can not move the `butter` anymore

Time Complexity: `O(1)`

Space Complexity: `O(n*m)`

#### `hash` method

Inputs: `None`
Returns: `str`

Returns a string from concatenation of `state` hash and `robot_location` hash

#### `heuristic` method

computes manhattan distance of each butter from its nearest point and adds up all the distances (part A).
Then, it computes the manhattan distance of robot from the farthest butter to the robot, and adds this value to the previously computed manhattan distance in part A.<br>
Returns : the `sum of all distances` introduced above.<br>

Time Complexity: `O(n*m)`. note: n and m are the number of rows and columns in game's board respectively.

Space Complexity: `O(b*p)` . note : b => number of butters, p => number of points.

### `Node` Class

Used as a base class for other classes to write based on it.
Contains the `state` as the required attribute of all nodes classes

### `Successor` Class

The successor class

#### `generate` method

Inputs: `State`
Returns: A list of pairs of (tuple) `state` and `cost` of the corresponding available movements

It checks all the available 4 movements, and generate the related state with the cost of going to that state

Time Complexity: `O(4)`

Space Complexity: `O(n*m)`

#### `CellType` Class

It's an `Enum` of all available cell types

#### `Answer` Class

Used to store `movements` and `cost` of founded answer. Provides an `__str__` method which helps to print those values in the required format.

### `utils.py`

#### `get_manhattan_distance` method

Inputs: two tuples.
Returns: manhattan distance of the two input tuples.

Time Complexity: `O(1)`

Space Complexity: `O(1)`

## Algorithms

### `UCS`

A class that uses a `PriorityQueue` to sort states based on the `g` (the cost of moving from initial state to the corresponding state).

Inputs: `costs`, the initial `state`
Returns:

- `can’t pass the butter` string if an answer is not found
- `Answer` class if the answer is found

Time Complexity: `O(b^{1+⌊C∗/ε⌋})`

Space Complexity: `O(b^{1+⌊C∗/ε⌋})`

#### `UCSNode` Class

Constructed based on `UCS` Class, adds `g` attribute and its corresponding `__lr__` to the `UCS` class to be used at priority queue in `UCS` algorithm

### `BestFirstSearch`

A class that uses a `PriorityQueue` to sort states based on the `h` (the estimated cost from the current node to the goal).

Inputs: `costs`, the initial `state`
Returns:

- `can’t pass the butter` string if an answer is not found
- `Answer` class if the answer is found

Time Complexity: `O(b* ^ d)` . note: b\*: effective branching factor/ d: maximum depth of the tree

Space Complexity: `O(b* ^ d)`

#### `BestFirstSearchNode` Class

Constructed based on `BestFirstSearch` Class, adds `h` attribute and its corresponding `__lr__` to the `BestFirstSearch` class to be used at priority queue in `BestFirstSearch` algorithm

### `A*`

A class that uses a `PriorityQueue` to sort states based on the `h+g` (where h is the estimated cost from the current node to the goal AND g is the cost of moving from initial state to the corresponding state).

Inputs: `costs`, the initial `state`
Returns:

- `can’t pass the butter` string if an answer is not found
- `Answer` class if the answer is found

Time Complexity: `O(b* ^ d)` . note: b\*: effective branching factor/ d: maximum depth of the tree

Space Complexity: `O(b* ^ d)`

#### `AStarNode` Class

Constructed based on `AStar` Class, adds `h+g` attribute and its corresponding `__lr__` to the `AStar` class to be used at priority queue in `AStar` algorithm

### `BFS`

A class that uses a `FIFO Queue` to do search on a tree.

Inputs: `costs`, the initial `state`
Returns:

- `can’t pass the butter` string if an answer is not found
- `Answer` class if the answer is found

Time Complexity: `O(b ^ d)` . note: b: branching factor/ d: maximum depth of the tree

Space Complexity: `O(b ^ d)`

#### `BFSNode` Class

Constructed based on `BFS` Class, adds `g` attribute so that we can calculate the goal's path cost at the end.

### `DFS`

A class that uses a `LIFO Queue` to do search on a tree.

Inputs: `costs`, the initial `state`
Returns:

- `can’t pass the butter` string if an answer is not found
- `Answer` class if the answer is found

Time Complexity: `O(b ^ d)` . note: b: branching factor/ d: maximum depth of the tree

Space Complexity: `O(bd)`

#### `DFSNode` Class

Constructed based on `DFS` Class, adds `g` attribute so that we can calculate the goal's path cost at the end.
