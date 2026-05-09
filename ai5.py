# Greedy Algorithm Applications
# 1. Selection Sort
# 2. Minimum Spanning Tree using Prim's Algorithm

# -----------------------------
# PART 1 : Selection Sort
# -----------------------------

def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Driver code for Selection Sort
arr = [64, 25, 12, 22, 11]

print("Original Array:")
print(arr)

sorted_arr = selection_sort(arr)

print("\nSorted Array using Selection Sort:")
print(sorted_arr)


# -----------------------------
# PART 2 : Minimum Spanning Tree
# Prim's Algorithm
# -----------------------------

INF = 9999999

# Number of vertices
V = 4

# Graph using adjacency matrix
graph = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 3],
    [0, 5, 3, 0]
]

selected = [False] * V

# Start from first vertex
selected[0] = True

edge_count = 0

print("\nMinimum Spanning Tree using Prim's Algorithm:")
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