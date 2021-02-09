"""
Input:
The first line of the input contains an integer 'T' denoting the number of test cases.
Then 'T' testcases follow. Each testcase consists of two lines.
Description of testcases are as follows:
The First line of each testcase contains two integers 'N' and 'M' which denotes
the no of vertices and no of edges respectively.
The Second line of each test case contains 'M'
space separated pairs u and v denoting that there is a bidirectional  edge from u to v .

Output:
The method should return 1 if there is a cycle else it should return 0.
3
2 1
0 1
4 3
0 1 1 2 2 3
5 4
0 1 2 3 3 4 4 2

Output:
0
0
1

DFS:
    Condition: 1. if node is visited and node is not parent
        then its a back-edge and cycle exist
"""

class Graph:
    def __init__(self, edges, N):
        self.graph = [[] for _ in range(N)]
        for (src, dest) in edges:
            self.graph[src].append(dest)
            self.graph[dest].append(src)


def check_cycle(g, v, visited, parent):

    visited[v] = True

    for neighbour in g.graph[v]:
        if not visited[neighbour]:
            if check_cycle(g, neighbour, visited, v):
                return True
        elif neighbour != parent: # we found a back-edge (cycle)
            return True

    return False

def isCyclic(g,n):
    visited = [False] * n
    parent = -1
    for i in range(n):
        if not visited[i]:
            if(check_cycle(g, i, visited, parent)):
                return 1
    return 0

if __name__ == '__main__':
    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11), (11, 12)
        # edge (11->12) introduces a cycle in the graph
    ]
    N = 13
    graph = Graph(edges, N)

    # Do DFS traversal from first vertex
    if isCyclic(graph, N):
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain any cycle")
