import heapq

# A* algorithm
def astar(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    f_cost = {node: float('inf') for node in graph}
    f_cost[start] = heuristic[start]

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current]:
            temp_g = g_cost[current] + cost

            if temp_g < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = temp_g
                f_cost[neighbor] = temp_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))

    return None


# Example graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values (estimated distance to goal F)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

# Run A*
path = astar(graph, 'A', 'F', heuristic)

print("Shortest Path:", path)
