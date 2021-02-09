class graph:
    def __init__(self,g_dict=None):
        if g_dict is None:
            g_dict = {}
        self.g_dict = g_dict

    def get_vertices(self):
        # return self.g_dict.keys() ---> dict_keys(['a', 'b', 'c', 'd', 'e'])
        # to return ---> ['a', 'b', 'c', 'd', 'e']
        return list(self.g_dict.keys())

    def get_edges(self):
        edges = []
        for v1 in self.g_dict:
            for v2 in self.g_dict[v1]:
                if {v1,v2} not in edges:
                    edges.append({v1,v2})
        return edges

    def add_vertex(self, data):
        if data not in list(self.g_dict.keys()):
            self.g_dict[data] = []
        

    def add_edge(self,edge):  
        edges = set(edge)
        v1,v2 = tuple(edges)
        if v1  in self.g_dict:
            self.g_dict[v1].append(v2)
        else:
            self.g_dict[v1] = [v2]

graph_i = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }

obj = graph(graph_i)
obj.add_vertex("ee")
print((obj.get_vertices()))
obj.add_edge({"a","rr"})
print((obj.get_edges()))