def find_root_vertex(graph):
    visited = [False] * len(graph)

    for i in range(len(graph)):
        if not visited[i]:
            queue = [i]
            visited[i] = True

            while queue:
                current_vertex = queue.pop(0)

                for neighbor in graph[current_vertex]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True
            return i
    return -1


with open("../input.txt", "r") as file:
    graph = [list(map(int, line.strip().split())) for line in file]

root_vertex = find_root_vertex(graph)

with open("../output.txt", "w") as file:
    file.write(str(root_vertex))