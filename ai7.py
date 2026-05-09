# Greedy Algorithm Applications
# 1. Prim's Minimum Spanning Tree Algorithm
# 2. Kruskal's Minimum Spanning Tree Algorithm

# ---------------------------------------------------
# PART 1 : Prim's Algorithm
# ---------------------------------------------------

INF = 9999999

# Number of vertices
V = 5

# Graph represented using adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [False] * V

# Start from first vertex
selected[0] = True

edge_count = 0

print("Prim's Minimum Spanning Tree:")
print("Edge : Weight")

while edge_count < V - 1:

    minimum = INF
    x = 0
    y = 0

    for i in range(V):

        if selected[i]:

            for j in range(V):

                if (not selected[j]) and graph[i][j]:

                    if minimum > graph[i][j]:

                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", graph[x][y])

    selected[y] = True
    edge_count += 1


# ---------------------------------------------------
# PART 2 : Kruskal's Algorithm
# ---------------------------------------------------

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


print("\nKruskal's Minimum Spanning Tree:")
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

print("\nTotal MST Cost =", mst_cost)