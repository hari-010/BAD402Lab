# AO* Algorithm Implementation

graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],  # A is AND-OR node
    'B': [[('E', 1)], [('F', 1)]],
    'C': [[('G', 1)]],
    'D': [[('H', 1)]],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

# Initial heuristic values
H = {
    'A': 10,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0
}

# To store optimal solution graph
solution = {}

# AO* function
def ao_star(node):
    if not graph[node]:  # leaf node
        return H[node]

    min_cost = float('inf')
    best_path = None

    # Explore all possible paths (AND/OR combinations)
    for path in graph[node]:
        cost = 0
        for (child, weight) in path:
            cost += weight + ao_star(child)

        if cost < min_cost:
            min_cost = cost
            best_path = path

    H[node] = min_cost
    solution[node] = best_path

    return H[node]


# Run AO*
ao_star('A')

# Print solution
print("Optimal Cost:", H['A'])
print("\nSolution Graph:")
for node in solution:
    print(node, "->", solution[node])
