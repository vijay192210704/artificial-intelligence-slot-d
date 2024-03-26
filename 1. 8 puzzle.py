import heapq
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

initial_state = [[2, 8, 3],
                 [1, 6, 4],
                 [7, 0, 5]]


def manhattan_distance(state):
    """
    Calculate the Manhattan distance heuristic for the given state.
    """
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                row = (state[i][j] - 1) // 3
                col = (state[i][j] - 1) % 3
                distance += abs(row - i) + abs(col - j)
    return distance


def is_goal_state(state):
    """
    Check if the given state is the goal state.
    """
    return state == goal_state


def get_neighbors(state):
    """
    Generate possible neighbors of the given state by moving the empty tile.
    """
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    empty_row, empty_col = find_empty_tile(state)

    for dr, dc in directions:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            neighbor = [row[:] for row in state]
            neighbor[empty_row][empty_col], neighbor[new_row][new_col] = neighbor[new_row][new_col], neighbor[empty_row][empty_col]
            neighbors.append(neighbor)

    return neighbors


def find_empty_tile(state):
    """
    Find the coordinates of the empty tile (0) in the given state.
    """
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def solve_puzzle(initial_state):
    """
    Solve the 8-Puzzle problem using the A* algorithm with Manhattan distance heuristic.
    """
    heap = [(manhattan_distance(initial_state), 0, initial_state)]
    heapq.heapify(heap)
    visited = set()

    while heap:
        _, cost, current_state = heapq.heappop(heap)

        if is_goal_state(current_state):
            return cost

        if tuple(map(tuple, current_state)) in visited:
            continue
        visited.add(tuple(map(tuple, current_state)))

        neighbors = get_neighbors(current_state)
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor)) not in visited:
                heapq.heappush(heap, (manhattan_distance(neighbor) + cost + 1, cost + 1, neighbor))

    return None


# Example usage
steps = solve_puzzle(initial_state)
if steps is not None:
    print(f"Number of steps required to solve the puzzle: {steps}")
else:
    print("No solution found.")
