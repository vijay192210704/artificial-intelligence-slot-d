def is_valid_assignment(assignment, equation):
    """
    Check if the current assignment of letters to digits is valid.
    """
    expression = ''.join(str(assignment.get(letter, letter)) for letter in equation)
    if expression[0] == '0':
        return False  # Leading zeros are not allowed
    return eval(expression.replace('==', '-')) == 0

def solve_cryptarithmetic(equation):
    """
    Solve the Cryptarithmetic problem using brute-force approach.
    """
    letters = set(letter for letter in equation if letter.isalpha())
    letters = sorted(list(letters))
    digits = range(10)

    for perm in generate_permutations(digits, len(letters)):
        assignment = dict(zip(letters, perm))
        print("Trying assignment:", assignment)  # Debug statement
        if is_valid_assignment(assignment, equation):
            print("Valid assignment found:", assignment)  # Debug statement
            return assignment
    return None

def generate_permutations(elements, length):
    """
    Generate all permutations of given elements with the specified length.
    """
    if length == 0:
        yield []
        return

    for element in elements:
        for permutation in generate_permutations(elements, length - 1):
            if element not in permutation:
                yield [element] + permutation

# Example usage
equation = "SEND + MORE == MONEY"
solution = solve_cryptarithmetic(equation)

if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
