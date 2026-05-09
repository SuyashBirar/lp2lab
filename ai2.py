# Breadth First Search using Queue

from collections import deque

# Create an undirected graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS function
def bfs(graph, start):

    visited = set()          # To store visited nodes
    queue = deque([start])   # Create queue

    visited.add(start)

    while queue:

        # Remove front element
        node = queue.popleft()

        print(node, end=" ")

        # Visit adjacent nodes
        for neighbour in graph[node]:

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Driver code
print("Breadth First Search Traversal:")

bfs(graph, 'A')