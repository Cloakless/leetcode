class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def max_gold(x,y,visited):
            tot = grid[x][y]
            cvisited = visited + ((x,y),)
            a,b,c,d = 0,0,0,0
            if x > 0 and grid[x-1][y] != 0 and (x-1,y) not in cvisited:
                a = max_gold(x-1,y,cvisited)
            if x < m-1 and grid[x+1][y] != 0 and (x+1,y) not in cvisited:
                b = max_gold(x+1,y,cvisited)
            if y > 0 and grid[x][y-1] != 0 and (x,y-1) not in cvisited:
                c = max_gold(x,y-1,cvisited)
            if y < n-1 and grid[x][y+1] != 0 and (x,y+1) not in cvisited:
                d = max_gold(x,y+1,cvisited)
            tot += max(a,b,c,d)
            return tot
        best_gold = 0
        for i in range(m):
            for j in range(n):
                best_gold = max(best_gold, max_gold(i,j,()))
        return best_gold
