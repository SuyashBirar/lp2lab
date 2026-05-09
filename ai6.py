# Greedy Algorithm Applications
# 1. Single Source Shortest Path (Dijkstra's Algorithm)
# 2. Job Scheduling Problem

# ---------------------------------------------------
# PART 1 : Single Source Shortest Path
# Dijkstra's Algorithm
# ---------------------------------------------------

import heapq

# Graph represented using adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Dijkstra Algorithm
def dijkstra(graph, start):

    # Store shortest distances
    distances = {node: float('inf') for node in graph}

    distances[start] = 0

    # Priority Queue
    pq = [(0, start)]

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:

            distance = current_distance + weight

            # Update shorter path
            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(pq, (distance, neighbor))

    return distances


# Driver code
print("Single Source Shortest Path using Dijkstra Algorithm:")

shortest_paths = dijkstra(graph, 'A')

for node, distance in shortest_paths.items():
    print(f"A -> {node} = {distance}")


# ---------------------------------------------------
# PART 2 : Job Scheduling Problem
# ---------------------------------------------------

# Job format:
# (Job ID, Deadline, Profit)

jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

# Sort jobs by profit in descending order
jobs.sort(key=lambda x: x[2], reverse=True)

# Find maximum deadline
max_deadline = max(job[1] for job in jobs)

# Create slots
slots = [False] * max_deadline

# Store selected jobs
job_sequence = []

total_profit = 0

# Job Scheduling Algorithm
for job in jobs:

    job_id, deadline, profit = job

    # Find free slot before deadline
    for i in range(deadline - 1, -1, -1):

        if not slots[i]:

            slots[i] = True

            job_sequence.append(job_id)

            total_profit += profit

            break


# Display Result
print("\nJob Scheduling Problem:")

print("Selected Jobs:", job_sequence)

print("Total Profit:", total_profit)