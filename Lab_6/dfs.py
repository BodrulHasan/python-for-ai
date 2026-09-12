graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dfs(start, goal):

    stack = [start]
    visited = []

    while stack:

        node = stack.pop()

        if node not in visited:

            visited.append(node)

            if node == goal:
                return visited

            for child in graph[node]:
                stack.append(child)

    return "NO PATH FOUND"


start = 'A'
goal = 'G'

print("DFS:", dfs(start, goal))