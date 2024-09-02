class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        neighs = {}
        for edge in edges:
            x = edge[0]
            y = edge[1]
            if x not in neighs:
                neighs[x] = [y]
            else:
                neighs[x].append(y)
            if y not in neighs:
                neighs[y] = [x]
            else:
                neighs[y].append(x)
        cache = {}
        def sum_dist(node, parent):
            if (node,parent) in cache:
                return cache[(node, parent)]
            tot = 0
            children = 1 # Including yourself
            for neighbour in neighs[node]:
                if neighbour != parent:
                    neigh_tot, neigh_children = sum_dist(neighbour, node)
                    children += neigh_children
                    tot += neigh_tot + neigh_children
            cache[(node, parent)] = (tot, children)

            # If we are a leaf then other leaves attached to same point must have same value
            if len(neighs[node]) == 1:
                for sibling in neighs[neighs[node][0]]:
                    if len(neighs[sibling]) == 1:
                        cache[(sibling, parent)] = (tot, children)
            return (tot, children)
        return [sum_dist(i, n)[0] for i in range(n)]
