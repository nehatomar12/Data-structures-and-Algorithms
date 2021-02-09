# https://www.geeksforgeeks.org/topological-sorting/

class Graph:
    def __init__(self, N, edges):
        self.graph = [[] for _ in range(N)]
        self.vertices = N

        for (src, dest) in edges:
            self.graph[src].append(dest)

def topologicalSortUtil(g, node, visited, stack):

    visited[node] = True

    for i in g.graph[node]:
        if not visited[i]:
            topologicalSortUtil(g, i, visited, stack)

    stack.append(node)

def topologicalSort(g, N):
    visited =  [False] * N
    stack = []
    for i in range(N):
        if not visited[i]:
            topologicalSortUtil(g, i, visited, stack)

    print((stack[::-1]))

N=6
edges =[(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]
g = Graph(N, edges)
print((g.graph))
topologicalSort(g, N)