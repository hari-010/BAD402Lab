from collections import deque

# Check if a state is valid
def is_valid(m, c):
    # Invalid if negative or exceeds total
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    # Missionaries eaten condition
    if (m > 0 and m < c):
        return False
    if (3 - m > 0 and (3 - m) < (3 - c)):
        return False
    return True

# BFS function
def missionaries_cannibals():
    start = (3, 3, 1)  # (M_left, C_left, Boat: 1=left, 0=right)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m, c, boat), path = queue.popleft()

        if (m, c, boat) in visited:
            continue

        visited.add((m, c, boat))
        path = path + [(m, c, boat)]

        # Goal check
        if (m, c, boat) == goal:
            return path

        # Possible moves (M, C)
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for dm, dc in moves:
            if boat == 1:  # Boat on left → move to right
                new_state = (m - dm, c - dc, 0)
            else:          # Boat on right → move to left
                new_state = (m + dm, c + dc, 1)

            if is_valid(new_state[0], new_state[1]):
                queue.append((new_state, path))

    return None


# Run program
solution = missionaries_cannibals()

if solution:
    print("Solution found:\n")
    for step in solution:
        print(step)
else:
    print("No solution exists")
