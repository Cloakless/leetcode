class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        options = []
        m, n = len(grid), len(grid[0])
        seen = set()
        seen.add((0,0))
        heappush(options, (0,0,0))
        while options:
            dist, x, y = heappop(options)
            neighs = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            for a, b in neighs:
                if (a,b) not in seen and a >= 0 and a < m and b >= 0 and b < n:
                    seen.add((a,b))
                    if a == m - 1 and b == n - 1:
                        return dist
                    if grid[a][b] == 0:
                        heappush(options, (dist, a, b))
                    else:
                        heappush(options, (dist + 1, a, b))
