from collections import deque

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def pour(current, capacity, other):
    """
    Pour water from one jug to another.
    """
    if current == 0:
        return 0, other
    elif current + other <= capacity:
        return 0, current + other
    else:
        return current - (capacity - other), capacity

def solve_water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque([State(0, 0)])
    visited.add(State(0, 0))
    solution_steps = []

    while queue:
        current_state = queue.popleft()

        if current_state.jug1 == target or current_state.jug2 == target:
            solution_steps.append((current_state.jug1, current_state.jug2))
            return solution_steps

        # Pour water from jug1 to jug2
        next_state = State(*pour(current_state.jug1, capacity2, current_state.jug2))
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
            solution_steps.append((current_state.jug1, current_state.jug2))

        # Pour water from jug2 to jug1
        next_state = State(*pour(current_state.jug2, capacity1, current_state.jug1))
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
            solution_steps.append((current_state.jug1, current_state.jug2))

        # Fill jug1
        next_state = State(capacity1, current_state.jug2)
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
            solution_steps.append((current_state.jug1, current_state.jug2))

        # Fill jug2
        next_state = State(current_state.jug1, capacity2)
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
            solution_steps.append((current_state.jug1, current_state.jug2))

        # Empty jug1
        next_state = State(0, current_state.jug2)
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
            solution_steps.append((current_state.jug1, current_state.jug2))

        # Empty jug2
        next_state = State(current_state.jug1, 0)
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)
            solution_steps.append((current_state.jug1, current_state.jug2))

    return None

# Example usage
capacity1 = 4
capacity2 = 3
target = 2

solution_steps = solve_water_jug(capacity1, capacity2, target)
if solution_steps:
    print("Solution steps:")
    for step in solution_steps:
        print(step)
else:
    print("No solution found.")
