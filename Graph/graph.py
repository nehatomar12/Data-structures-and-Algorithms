def add_vertex(v):
    global graph
    if v in graph:
        return("Vetex {} already exist!".format(v))
    graph[v] = []


def add_edge(v1, v2, e):
    global graph
    if v1 in graph:
        graph[v1].append((v2, e))
    else:
        graph[v1] = [(v2, e)]


def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex, "->", edges[0], " edge weight: ", edges[1])


def bfs(graph, start_node):
    # Use queue
    # visit adjecent first
    queue = [start_node]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.append(node)
            for neighbour in graph[node]:
                queue.append(neighbour)


def dfs(graph, node, visted):
    # Use stack
    # pick nope and visit it till depth
    if node not in visted:
        print(node, end=" ")
        visted.append(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visted)


def dfs_iter(graph, start_node):
    # Use stack
    # pick nope and visit it till depth
    visited = []
    stack = [start_node]
    while stack:
        print(stack)
        node = stack.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            for neighbour in graph[node]:
                stack.insert(0, neighbour)


if __name__ == "__main__":
    """
    graph = {}
    add_vertex(1)
    add_vertex(2)
    add_vertex(3)
    add_vertex(4)
    # Add the edges between the vertices by specifying
    # the from and to vertex along with the edge weights.
    add_edge(1, 2, 1)
    add_edge(1, 3, 1)
    add_edge(2, 3, 3)
    add_edge(3, 4, 4)
    add_edge(4, 1, 5)
    print_graph()
    """

    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 4],
        3: [0],
        4: [2]
    }

    #bfs(graph, start_node=0)
    dfs(graph, 0, visted=[])
    print()
    print()
    print()
    dfs_iter(graph, start_node=0)
