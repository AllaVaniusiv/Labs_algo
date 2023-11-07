from collections import deque

def find_root_vertex(graph):
    def bfs(start_vertex):
        visited = set()
        queue = deque([start_vertex])
        while queue:
            vertex = queue.popleft() 
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return visited

    roots = []
    for vertex in graph:
        if len(bfs(vertex)) == len(graph):
            roots.append(vertex)

    if not roots:
        return -1
    else:
        return roots[0]

graph = {}
with open("input.txt", "r") as file:
    for line in file:
        u, v = map(int, line.strip().split())
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]

root_vertex = find_root_vertex(graph)


with open("output.txt", "w") as file:
    file.write(str(root_vertex))