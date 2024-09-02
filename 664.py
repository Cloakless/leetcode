class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        cache = {}
        def dp(i,j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i,j) in cache:
                return cache[(i,j)]
            best = 1 + dp(i+1, j)
            for k in range(i+1, j+1):
                if s[i] == s[k]:
                    cand = dp(i, k-1) + dp(k+1, j)
                    best = min(cand, best)
            cache[(i,j)] = best
            return best
        return dp(0, n-1)
