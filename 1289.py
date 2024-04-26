class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return min(grid[0])
        for i in range(1,n):
            for j in range(n):
                prev = [x for x in grid[i-1]]
                prev.pop(j)
                grid[i][j] += min(prev)
        return min(grid[n-1])
