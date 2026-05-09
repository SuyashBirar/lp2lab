# Depth First Search using recursion

# Create graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Set to store visited vertices
visited = set()

# Recursive DFS function
def dfs(visited, graph, node):
    
    # Check if node is not visited
    if node not in visited:
        
        print(node, end=" ")
        
        # Mark node as visited
        visited.add(node)
        
        # Visit all adjacent vertices
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver code
print("Depth First Search Traversal:")

dfs(visited, graph, 'A')