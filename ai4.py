# A* Algorithm for 8-Puzzle Problem

import heapq

# Goal State
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Initial State
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Function to calculate heuristic
def heuristic(state):

    count = 0

    for i in range(3):
        for j in range(3):

            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count


# Find blank position
def find_blank(state):

    for i in range(3):
        for j in range(3):

            if state[i][j] == 0:
                return i, j


# Generate next states
def generate_states(state):

    states = []

    x, y = find_blank(state)

    # Possible moves
    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in moves:

        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            # Deep copy
            new_state = [row[:] for row in state]

            # Swap blank tile
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            states.append(new_state)

    return states


# Convert state to tuple
def to_tuple(state):
    return tuple(tuple(row) for row in state)


# A* Search
def a_star(start):

    pq = []

    visited = set()

    # Initial cost
    h = heuristic(start)

    heapq.heappush(pq, (h, 0, start))

    while pq:

        f, g, current = heapq.heappop(pq)

        # Goal check
        if current == goal:
            return current

        visited.add(to_tuple(current))

        # Generate child states
        for next_state in generate_states(current):

            if to_tuple(next_state) not in visited:

                g_new = g + 1
                h_new = heuristic(next_state)

                f_new = g_new + h_new

                heapq.heappush(
                    pq,
                    (f_new, g_new, next_state)
                )

    return None


# Driver code
solution = a_star(start)

print("Solution State:")

for row in solution:
    print(row)