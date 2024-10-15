class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9+7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

        for a in range(1, n+1):
            dp[a][0] = dp[a-1][0] + a-1
        
        
        for j in range(1, k):
            acc = 0
            for i in range(j+2, n+1):
                acc += dp[i-1][j-1]
                dp[i][j] = dp[i-1][j] + acc
        
        return dp[n][k-1] % MOD
