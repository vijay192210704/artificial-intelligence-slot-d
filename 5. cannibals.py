from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def __eq__(self, other):
        return (self.missionaries, self.cannibals, self.boat) == (other.missionaries, other.cannibals, other.boat)

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def is_valid_state(state):
    """
    Check if the state is valid.
    """
    if state.missionaries < 0 or state.missionaries > 3:
        return False
    if state.cannibals < 0 or state.cannibals > 3:
        return False
    if state.missionaries > 0 and state.missionaries < state.cannibals:
        return False
    if state.missionaries < 3 and (3 - state.missionaries) < (3 - state.cannibals):
        return False
    return True

def generate_next_states(current_state):
    """
    Generate possible next states from the current state.
    """
    next_states = []
    if current_state.boat == 'left':
        next_states.extend([
            State(current_state.missionaries - 1, current_state.cannibals, 'right'),
            State(current_state.missionaries, current_state.cannibals - 1, 'right'),
            State(current_state.missionaries - 1, current_state.cannibals - 1, 'right'),
            State(current_state.missionaries - 2, current_state.cannibals, 'right'),
            State(current_state.missionaries, current_state.cannibals - 2, 'right')
        ])
    else:
        next_states.extend([
            State(current_state.missionaries + 1, current_state.cannibals, 'left'),
            State(current_state.missionaries, current_state.cannibals + 1, 'left'),
            State(current_state.missionaries + 1, current_state.cannibals + 1, 'left'),
            State(current_state.missionaries + 2, current_state.cannibals, 'left'),
            State(current_state.missionaries, current_state.cannibals + 2, 'left')
        ])
    return [state for state in next_states if is_valid_state(state)]

def solve_missionaries_cannibals():
    """
    Solve the Missionaries and Cannibals problem using BFS.
    """
    initial_state = State(3, 3, 'left')
    goal_state = State(0, 0, 'right')

    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        if current_state not in visited:
            visited.add(current_state)
            next_states = generate_next_states(current_state)
            for next_state in next_states:
                queue.append((next_state, path + [current_state]))

    return None

def print_solution(path):
    """
    Print the solution path.
    """
    if path is None:
        print("No solution found.")
        return

    print("Solution path:")
    for state in path:
        print(state.missionaries, state.cannibals, state.boat)

# Solve the problem
solution_path = solve_missionaries_cannibals()
print_solution(solution_path)
