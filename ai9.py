# Constraint Satisfaction Problem (CSP)
# 1. N-Queens Problem using Backtracking and Branch & Bound
# 2. Graph Coloring Problem using Backtracking

# ---------------------------------------------------
# PART 1 : N-Queens Problem
# ---------------------------------------------------

N = 4

# Create chessboard
board = [[0 for _ in range(N)] for _ in range(N)]

# Arrays for Branch and Bound
columns = [False] * N
diag1 = [False] * (2 * N)
diag2 = [False] * (2 * N)


# Function to print board
def print_board(board):

    for row in board:

        for cell in row:

            if cell == 1:
                print("Q", end=" ")

            else:
                print(".", end=" ")

        print()


# Function to solve N-Queens
def solve_nqueen(row):

    # All queens placed
    if row == N:
        return True

    for col in range(N):

        # Check constraints
        if (not columns[col] and
            not diag1[row + col] and
            not diag2[row - col + N]):

            # Place queen
            board[row][col] = 1

            columns[col] = True
            diag1[row + col] = True
            diag2[row - col + N] = True

            # Recursive call
            if solve_nqueen(row + 1):
                return True

            # Backtracking
            board[row][col] = 0

            columns[col] = False
            diag1[row + col] = False
            diag2[row - col + N] = False

    return False


print("N-Queens Problem Solution:\n")

if solve_nqueen(0):
    print_board(board)
else:
    print("No Solution Exists")


# ---------------------------------------------------
# PART 2 : Graph Coloring Problem
# ---------------------------------------------------

# Number of vertices
V = 4

# Number of colors
m = 3

# Graph represented using adjacency matrix
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

# Store colors assigned to vertices
colors = [0] * V


# Check if color can be assigned
def is_safe(vertex, color):

    for i in range(V):

        if graph[vertex][i] == 1 and colors[i] == color:
            return False

    return True


# Graph coloring using backtracking
def graph_coloring(vertex):

    # All vertices colored
    if vertex == V:
        return True

    for color in range(1, m + 1):

        if is_safe(vertex, color):

            colors[vertex] = color

            # Recursive call
            if graph_coloring(vertex + 1):
                return True

            # Backtracking
            colors[vertex] = 0

    return False


print("\nGraph Coloring Solution:\n")

if graph_coloring(0):

    for vertex in range(V):
        print("Vertex", vertex, "--> Color", colors[vertex])

else:
    print("No Solution Exists")