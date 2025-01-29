class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = [i for i in range(n+1)]
        def find_rep(k):
            a = k
            while dsu[k] != k:
                k = dsu[k]
            dsu[a] = k # Short-circuit
            return k

        for edge in edges:
            a, b = edge
            x, y = find_rep(a), find_rep(b)
            if x == y:
                return [a, b]
            dsu[x] = y
