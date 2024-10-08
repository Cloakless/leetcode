class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n = len(graph)
        def find_paths(x, route):
            nr = route + (x,)
            if x == (n-1):
                paths.append(list(nr))
            else:
                for node in graph[x]:
                    find_paths(node, nr)
        find_paths(0, ())
        return paths
