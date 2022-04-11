class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            # if the location is already a key in the dictionary
            if start in self.graph_dict:
                # we will just add the second value of it to the list
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict:", self.graph_dict)

    # the logic here is we use recursion
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        # the simplest case would be start == end
        if start == end:
            return [path]

        # corner cases: start point is the destination
        if start not in self.graph_dict:
            return []

        # normal cases:
        paths = []
        for node in self.graph_dict[start]:
            # if we have not visited that node yet => the node is not in the path
            if node not in path:
                # need to add the path in => append the start
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                #sometime sp is returned as None
                if sp:
                    # if there is no shortest path => take whatever path we have as answer or the current path is shorter than the length of the path
                    # we have seen so far
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path



if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "Dubai"

    print(f"Shortest paths between {start} and {end}: ", route_graph.get_shortest_path(start, end))
