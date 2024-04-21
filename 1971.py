class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        neighbours = {}
        for edge in edges:
            x = edge[0]
            y = edge[1]
            if x not in neighbours:
                neighbours[x] = [y] 
            else:
                neighbours[x].append(y)
            if y not in neighbours:
                neighbours[y] = [x]
            else:
                neighbours[y].append(x)

        reachable = set()
        not_checked = {source}
        changing = True
        while bool(not_checked):
            next_item = not_checked.pop()
            for neighbour in neighbours[next_item]:
                if neighbour not in reachable:
                    not_checked.add(neighbour)
            reachable.add(next_item)

        return destination in reachable
