class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = [[] for i in range(n)]
        for edge in edges:
            parents[edge[1]].append(edge[0])
        ancestors = []

        def trace(node, seen):
            seen.add(node)
            for parent in parents[node]:
                if parent not in seen:
                    trace(parent, seen)

        for k in range(n):
            upwards, seen = [], set()
            trace(k, seen)
            for node in range(n):
                if node == k:
                    pass
                elif node in seen:
                    upwards.append(node)
            upwards.sort()
            ancestors.append(upwards)
        return ancestors
        
