class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxX = 0
        minX = m-1
        maxY = 0
        minY = n-1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxX = max(maxX, i)
                    minX = min(minX, i)
                    maxY = max(maxY, j)
                    minY = min(minY, j)
        return ((maxX + 1) - minX) * ((maxY + 1) - minY) 
