class Graph:
    def __init__(self, N, edges):
        self.vertices = N
        self.graph = [[] for i in range(N)]
        for (src, dest) in edges:
            self.graph[src].append(dest)
            self.graph[dest].append(src)

    def printGraph(self):
        for r in self.graph:
            print(r)

    def DFS(self, start_node, visited):
        print(start_node, end=' ')
        visited[start_node] = True
        for i in self.graph[start_node]:
            if not visited[i]:
                self.DFS(i, visited)

    def BFS(self, graph, q, visited):
        if not q:
            return

        # pop front node from queue and print it
        v = q.pop(0)
        print(v, end=' ')

        # do for every edge (v -> u)
        for u in self.graph[v]:
            if not visited[u]:
                # mark it visited and push it into queue
                visited[u] = True
                q.append(u)

        self.BFS(graph, q, visited)

# Create the graph
edges = [
    (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    # vertex 0, 13 and 14 are single nodes
]

# Set number of vertices in the graph
N = 15

# create a graph from edges
G = Graph( N, edges)
#G.printGraph()
visited = [False] * N
q = []

"""
# Do BFS traversal from all unvisited nodes to
# cover all unconnected components of graph
for i in range(N):
    if not visited[i]:
        # mark source vertex as visited
        visited[i] = True
        # push source vertex into the queue
        q.append(i)
        # start BFS traversal from vertex i
        G.BFS(G,q, visited)
"""

# Do DFS traversal from all unvisited nodes to
# cover all unconnected components of graph
for i in range(N):
    if not visited[i]:
        # mark source vertex as visited
        visited[i] = True
        # start DFS traversal from vertex i
        G.DFS(i, visited)

print()
