class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def catch_fish(x,y):
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            lake = set()
            border = set()
            border.add((x,y))
            ans = 0
            while border:
                new_border = set()
                while border:
                    (a,b) = border.pop()
                    ans += grid[a][b]
                    grid[a][b] = 0
                    for opt in dirs:
                        dx, dy = opt
                        na, nb = a + dx, b + dy
                        if 0 <= na < m and 0 <= nb < n and grid[na][nb] != 0:
                            new_border.add((na,nb))
                border = new_border
            return ans

        tot = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    tot = max(tot, catch_fish(i,j))

        return tot
