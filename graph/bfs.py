class Graph:
    def __init__(self):
        self.vertex_size = 0
        self.g = {}
    
    def getNeighbour(self,vertex):
        return g[vertex]
    
    def getSize(self):
        return self.vertex_size
    
def bfs(graph,start):
    visited =[]
    queue =[start]
    
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex]-set(visited))

    return visited

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(bfs(graph, 'A'))