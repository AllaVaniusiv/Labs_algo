from collections import deque

def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            vertex = int(parts[0])
            neighbors = [int(x) for x in parts[1:]]
            graph[vertex] = neighbors
    return graph

def find_root(graph):
    def bfs(graph, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            visited.add(vertex)
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)
        return visited

    for vertex in graph:
        if not any(vertex in bfs(graph, v) for v in graph if v != vertex):
            return vertex
    return -1


input_file = "input.txt"
output_file = "output.txt"

graph = read_graph_from_file(input_file)
root = find_root(graph)

with open(output_file, 'w') as file:
    file.write(str(root))
