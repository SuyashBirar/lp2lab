# A* Algorithm for 4-Queens Problem

import heapq

N = 4

# Function to calculate heuristic
def heuristic(state):

    h = 0

    for i in range(len(state)):
        for j in range(i + 1, len(state)):

            # Check column conflicts
            if state[i] == state[j]:
                h += 1

            # Check diagonal conflicts
            if abs(state[i] - state[j]) == abs(i - j):
                h += 1

    return h


# Function to generate next states
def generate_states(state):

    states = []

    row = len(state)

    for col in range(N):

        new_state = state + [col]
        states.append(new_state)

    return states


# A* Search Algorithm
def a_star():

    # Priority Queue
    pq = []

    # Initial empty state
    heapq.heappush(pq, (0, []))

    while pq:

        f, state = heapq.heappop(pq)

        # Goal state
        if len(state) == N and heuristic(state) == 0:
            return state

        # Generate child states
        for next_state in generate_states(state):

            # Path cost
            g = len(next_state)

            # Heuristic cost
            h = heuristic(next_state)

            # Total cost
            f = g + h

            heapq.heappush(pq, (f, next_state))


# Driver code
solution = a_star()

print("Solution for 4-Queens Problem:")

for row in range(N):

    for col in range(N):

        if solution[row] == col:
            print("Q", end=" ")

        else:
            print(".", end=" ")

    print()