N = 8

# Print solution
def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print("\n")

# Check if safe to place queen
def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

# Solve using backtracking
def solve(board, row):
    if row == N:
        print("Solution:\n")
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve(board, row + 1):
                return True

            board[row][col] = 0  # Backtrack

    return False


# Main
board = [[0]*N for _ in range(N)]

if not solve(board, 0):
    print("No solution exists")
