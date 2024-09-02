class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for a in range(n):
            dp[0][a] = points[0][a]
        best_left = [0 for _ in range(n)]
        best_right = [0 for _ in range(n)]
        for i in range(1, m):
            best_left[0] = dp[i-1][0]
            best_right[n-1] = dp[i-1][n-1]
            for j in range(1, n):
                best_left[j] = max(best_left[j-1] - 1, dp[i-1][j])
                best_right[n-1-j] = max(best_right[n-j] - 1, dp[i-1][n-j-1])
            for k in range(n):
                dp[i][k] = points[i][k] + max(best_left[k], best_right[k])
        return max([dp[m-1][x] for x in range(n)])
