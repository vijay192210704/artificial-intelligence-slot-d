import heapq

class Node:
    def __init__(self, row, col, g_cost=float('inf'), h_cost=0, parent=None):
        self.row = row
        self.col = col
        self.g_cost = g_cost  # Cost from start node to current node
        self.h_cost = h_cost  # Heuristic cost (estimated cost from current node to goal node)
        self.parent = parent  # Parent node

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __lt__(self, other):
        # Comparison method for priority queue ordering
        return (self.g_cost + self.h_cost) < (other.g_cost + other.h_cost)

    def __hash__(self):
        # Override hash method to make Node objects hashable
        return hash((self.row, self.col))

def heuristic(node, goal):
    # Euclidean distance heuristic
    return ((node.row - goal.row) ** 2 + (node.col - goal.col) ** 2) ** 0.5

def astar(grid, start, goal):
    open_set = [start]  # Priority queue (open set of nodes to be evaluated)
    closed_set = set()  # Set of nodes already evaluated

    while open_set:
        current_node = heapq.heappop(open_set)  # Get node with lowest f_cost
        closed_set.add(current_node)

        if current_node == goal:
            # Reconstruct path
            path = []
            while current_node:
                path.append((current_node.row, current_node.col))
                current_node = current_node.parent
            return path[::-1]  # Reverse path to start from the start node

        for neighbor_row, neighbor_col in [(current_node.row - 1, current_node.col),
                                           (current_node.row + 1, current_node.col),
                                           (current_node.row, current_node.col - 1),
                                           (current_node.row, current_node.col + 1)]:
            if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]) and grid[neighbor_row][neighbor_col] != 1:
                neighbor_node = Node(neighbor_row, neighbor_col)
                if neighbor_node in closed_set:
                    continue

                g_cost = current_node.g_cost + 1  # Cost of moving to neighbor is always 1 in a grid
                h_cost = heuristic(neighbor_node, goal)
                f_cost = g_cost + h_cost

                if neighbor_node not in open_set or f_cost < (neighbor_node.g_cost + neighbor_node.h_cost):
                    neighbor_node.g_cost = g_cost
                    neighbor_node.h_cost = h_cost
                    neighbor_node.parent = current_node

                    if neighbor_node not in open_set:
                        heapq.heappush(open_set, neighbor_node)

    return None  # No path found

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_node = Node(0, 0)
goal_node = Node(4, 4)
path = astar(grid, start_node, goal_node)

if path:
    print("Path found:", path)
else:
    print("No path found.")
