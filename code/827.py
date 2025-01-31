class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        sizes = defaultdict(int)
        group = 1
        n = len(grid)
        opts = [(0,1),(1,0),(-1,0),(0,-1)]

        def fill_island(x,y):
            nonlocal group
            group += 1
            border = set()
            size = 1
            grid[x][y] = group
            border.add((x,y))
            
            while border:
                a,b = border.pop()
                for opt in opts:
                    da, db = opt
                    na, nb = a + da, b + db
                    if 0 <= na < n and 0 <= nb < n and grid[na][nb] == 1:
                        border.add((na,nb))
                        size += 1
                        grid[na][nb] = group
            sizes[group] = size

        num_zeros = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    fill_island(i,j)
                elif grid[i][j] == 0:
                    num_zeros += 1
        if num_zeros == 0:
            return n*n
        elif num_zeros == n*n:
            return 1

        best = 0
        for a in range(n):
            for b in range(n):
                if grid[a][b] == 0:
                    combination = 1
                    added = set()
                    for opt in opts:
                        da, db = opt
                        na, nb = a + da, b + db
                        if 0 <= na < n and 0 <= nb < n and grid[na][nb] != 0 and grid[na][nb] not in added:
                            added.add(grid[na][nb])
                            combination += sizes[grid[na][nb]]
                    best = max(best, combination)
        return best
