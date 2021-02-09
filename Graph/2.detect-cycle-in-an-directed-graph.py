# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

class Graph:
    def __init__(self, edges, N):
        self.graph = [[] for _ in range(N)]
        for (src, dest) in edges:
            self.graph[src].append(dest)

def check_cycle(g, v, visited, recStack):
    visited[v] = True
    recStack[v] = True
    for neighbour in g.graph[v]:
        if not visited[neighbour]:
            if check_cycle(g, neighbour, visited, recStack):
                return True
        elif recStack[neighbour]: # we found a back-edge (cycle)
            return True

    # The node needs to be poped from
    # recursion stack before function ends
    recStack[v] = False
    return False

def isCyclic(g,n):
    visited = [False] * n
    recStack = [False] * n
    for i in range(n):
        if not visited[i]:
            if(check_cycle(g, i, visited, recStack)):
                return 1
    return 0

if __name__ == '__main__':
    edges = [
        (0, 1), (0, 2), (1, 2),(2, 0),(2, 3),(3, 3)
    ]
    N = 13
    graph = Graph(edges, N)
    print((graph.graph))
    # Do DFS traversal from first vertex
    if isCyclic(graph, N):
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain any cycle")
