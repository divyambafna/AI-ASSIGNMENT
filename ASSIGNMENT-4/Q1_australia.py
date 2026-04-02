states = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']

def is_valid(state, color, solution):
    for neighbor in neighbors[state]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

def solve(solution, states):
    if len(solution) == len(states):
        return solution

    state = states[len(solution)]

    for color in colors:
        if is_valid(state, color, solution):
            solution[state] = color
            result = solve(solution, states)
            if result:
                return result
            del solution[state]

    return None

solution = solve({}, states)

for state in solution:
    print(state, solution[state])
