def building_graph(matrix):
    graph = {}

    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns):
            current_node = (i, j)

            if current_node not in graph:
                graph[current_node] = []
            if i + 1 != rows:
                graph[current_node].append((i + 1, j))

                if j + 1 < len(matrix[i + 1]):
                    graph[current_node].append((i + 1, j + 1))

    return graph


def topological_sort(graph, experience):
    def dfs(node, distance):
        visited.add(node)
        if graph.get(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, distance +
                        experience[neighbor[0]][neighbor[1]])

        stack.append((node, distance))

    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            dfs(node, experience[node[0]][node[1]])

    return stack[::-1]


def max_experience(levels, experience):
    graph = building_graph(experience)
    top = topological_sort(graph, experience)
    result = -1
    for coord, exp in top:
        if exp > result:
            result = exp
    return result


with open("career.in", "r") as file:
    levels = int(file.readline().strip())
    experience = [list(map(int, file.readline().split()))
                  for _ in range(levels)]

result = max_experience(levels, experience)

with open("career.out", "w") as outfile:
    outfile.write(str(result))
