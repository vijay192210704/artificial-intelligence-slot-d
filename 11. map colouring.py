def is_valid_assignment(region, color, assignment):
    """
    Check if the current assignment of color to region is valid.
    """
    for neighbor in assignment.get(region, []):
        if assignment.get(neighbor) == color:
            return False
    return True

def map_coloring(countries, colors):
    """
    Solve the Map Coloring problem using backtracking.
    """
    def backtrack(assignment):
        if len(assignment) == len(countries):
            return assignment
        region = None
        for country in countries:
            if country not in assignment:
                region = country
                break
        for color in colors:
            if is_valid_assignment(region, color, assignment):
                assignment[region] = color
                result = backtrack(assignment)
                if result is not None:
                    return result
                del assignment[region]
        return None

    return backtrack({})

# Example usage:
countries = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW']
}

colors = ['red', 'green', 'blue']

color_assignment = map_coloring(countries, colors)
if color_assignment is not None:
    print("Map coloring solution:")
    for country, color in color_assignment.items():
        print(f"{country}: {color}")
else:
    print("No solution found.")
