class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def land_around(a,b):
            tot = 0
            for i in range(max(a-1, 0), min(a+2, m)):
                for j in range(max(b-1, 0), min(b+2, n)):
                    if grid[i][j] == 1 and (a-i)*(b-j) == 0 and (a != i or b != j):
                        tot += 1
            return tot
        border = 0    
        for a in range(m):
            for b in range(n):
                if grid[a][b] == 1:
                    border += 4 - land_around(a,b)
        return border
        
