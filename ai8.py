# Greedy Algorithm Applications
# 1. Kruskal's Minimum Spanning Tree Algorithm
# 2. Dijkstra's Shortest Path Algorithm

# ---------------------------------------------------
# PART 1 : Kruskal's Algorithm
# ---------------------------------------------------

# Number of vertices
V = 5

# Graph edges: (weight, vertex1, vertex2)
edges = [
    (2, 0, 1),
    (3, 1, 2),
    (5, 1, 4),
    (6, 0, 3),
    (7, 2, 4),
    (8, 1, 3),
    (9, 3, 4)
]

# Sort edges by weight
edges.sort()

parent = []
rank = []

# Create sets
for node in range(V):
    parent.append(node)
    rank.append(0)


# Find function
def find(node):

    if parent[node] != node:
        parent[node] = find(parent[node])

    return parent[node]


# Union function
def union(u, v):

    root_u = find(u)
    root_v = find(v)

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v

    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u

    else:
        parent[root_v] = root_u
        rank[root_u] += 1


print("Kruskal's Minimum Spanning Tree:")
print("Edge : Weight")

mst_cost = 0
edge_used = 0

for weight, u, v in edges:

    # Check cycle
    if find(u) != find(v):

        union(u, v)

        print(u, "-", v, ":", weight)

        mst_cost += weight
        edge_used += 1

        if edge_used == V - 1:
            break

print("Total MST Cost =", mst_cost)


# ---------------------------------------------------
# PART 2 : Dijkstra's Algorithm
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
print("\nDijkstra's Shortest Path:")

shortest_paths = dijkstra(graph, 'A')

for node, distance in shortest_paths.items():
    print(f"A -> {node} = {distance}")