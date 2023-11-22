def build_graph(levels):
    graph = {}
    for i in range(levels):
        for j in range(i + 1):
            if i < levels - 1:
                if (i, j) not in graph:
                    graph[(i, j)] = []
                graph[(i, j)].extend([(i + 1, j), (i + 1, j + 1)])
    return graph

def max_experience(graph, levels, experience):
    max_exp = 0
    stack = [((0, 0), 0)]

    while stack:
        node, current_exp = stack.pop()
        i, j = node
        current_exp += experience[i][j]
        max_exp = max(max_exp, current_exp)

        for neighbor in graph.get(node, []):
            stack.append((neighbor, current_exp))

    return max_exp


def read_input(file_path="career.in"):
    with open(file_path, "r") as file:
        levels = int(file.readline())
        experience = [list(map(int, file.readline().split())) for _ in range(levels)]
    return levels, experience

def write_output(result, file_path="career.out"):
    with open(file_path, "w") as file:
        file.write(str(result))

if __name__ == "__main__":
    levels, experience = read_input()
    graph = build_graph(levels)
    result = max_experience(graph, levels, experience)
    write_output(result)
