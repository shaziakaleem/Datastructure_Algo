graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E','C']),
         'C': set(['A', 'F','B']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#using bfs
def cycle(graph,start):
    queue = [start]
    visited =[]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.extend(vertex)
            for v in graph[vertex]:
                if v in queue:
                    return "Cycle detected"
                else:
                    queue.append(v)
    return "No Cycle"

print(cycle(graph,'A'))
