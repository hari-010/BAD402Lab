from collections import deque

def water_jug_bfs(x, y, z):
    visited = set()
    queue = deque([(0, 0)])  # Initial state: both jugs empty

    while queue:
        a, b = queue.popleft()

        # If target is reached
        if a == z or b == z:
            print("Target reached:", (a, b))
            return True

        if (a, b) in visited:
            continue

        visited.add((a, b))

        # Possible operations:
        next_states = [
            (x, b),       # Fill jug X
            (a, y),       # Fill jug Y
            (0, b),       # Empty jug X
            (a, 0),       # Empty jug Y
            # Pour X → Y
            (a - min(a, y - b), b + min(a, y - b)),
            # Pour Y → X
            (a + min(b, x - a), b - min(b, x - a))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("Target not possible")
    return False


# Example usage
x = 4  # Capacity of Jug X
y = 3  # Capacity of Jug Y
z = 2  # Target

water_jug_bfs(x, y, z)
