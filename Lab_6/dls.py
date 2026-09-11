def dls(graph, node, goal, limit, path=None):

    if path is None:
        path = [node]

    # Goal found
    if node == goal:
        return path

    # Limit শেষ
    if limit == 0:
        return None

    for neighbour in graph[node]:

        if neighbour not in path:

            result = dls(
                graph,
                neighbour,
                goal,
                limit - 1,
                path + [neighbour]
            )

            if result is not None:
                return result

    return None


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'

result = dls(graph, start, goal, 2)

print("Result:", result)