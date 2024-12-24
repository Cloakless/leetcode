class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter(edgeset):
            neighbours = defaultdict(set)
            for x, y in edgeset:
                neighbours[x].add(y)
                neighbours[y].add(x)

            furthest_node = -1
            furthest_dist = -1

            def dfs(node, parent, dist):
                nonlocal furthest_node
                nonlocal furthest_dist
                best = -1
                if dist > furthest_dist:
                    furthest_dist = dist
                    furthest_node = node
                for neighbour in neighbours[node]:
                    if neighbour != parent:
                        best = max(best, dfs(neighbour, node, dist + 1))
                return best + 1

            dfs(0, -1, 0)

            furthest_dist = -1

            dfs(furthest_node, -1, 0)
            return furthest_dist

        a = diameter(edges1)
        b = diameter(edges2)
        return max(a, b, (a+1)//2 + (b+1)//2 + 1)
