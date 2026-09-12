from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(start, goal):

    queue = deque([start])
    visited = []

    while queue:

        node = queue.popleft()

        if node not in visited:

            visited.append(node)

            if node == goal:
                return visited

            for child in graph[node]:
                queue.append(child)

    return "NO PATH FOUND"


start = 'A'
goal = 'G'

print("BFS:", bfs(start, goal))