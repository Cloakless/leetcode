class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        n = endPos - startPos
        
        @cache
        def dfs(n, k):
            if n == k:
                return 1
            if n > k:
                return 0
            if k == 0:
                return n == 0
            return (dfs(n-1,k-1) + dfs(n+1, k-1)) % (10**9+7)

        return dfs(n, k)
