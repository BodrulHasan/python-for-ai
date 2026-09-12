graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dls(node, goal, limit):

    if node == goal:
        return [node]

    if limit == 0:
        return None

    for child in graph[node]:

        result = dls(child, goal, limit - 1)

        if result is not None:
            return [node] + result

    return None


start = 'A'
goal = 'G'
limit = 2

result = dls(start, goal, limit)

if result:
    print("DLS:", " -> ".join(result))
else:
    print("NO PATH FOUND")