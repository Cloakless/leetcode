class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def flip(row):
            row = list(map(lambda x: 1-x, row))
            return row
        def col_sum(y):
            tot = 0
            for a in range(m):
                tot += grid[a][y]
            return tot

        for i in range(m):
            if grid[i][0] == 0:
                grid[i] = flip(grid[i])
        
        binsum = 0
        for j in range(n):
            col = col_sum(j)
            binsum += max(col, m-col)*2**(n-j-1)
        return binsum
