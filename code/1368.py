class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        opts = [(0,1), (0,-1), (1, 0), (-1, 0)]
        neighs = set()
        m, n = len(grid), len(grid[0])

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n
        
        best = [[m*n for _ in range(n)] for _ in range(m)]
        best[0][0] = 0

        dq = deque([(0,0)])

        while dq:
            r, c = dq.popleft()
            for i in range(4):
                dx, dy = opts[i]
                opt = i + 1
                new_x, new_y = r + dx, c + dy
                cost = 0 if grid[r][c] == opt else 1
                if is_valid(new_x, new_y) and best[r][c] + cost < best[new_x][new_y]:
                    best[new_x][new_y] = best[r][c] + cost
                    if cost == 1:
                        dq.append((new_x, new_y))
                    else:
                        dq.appendleft((new_x, new_y))
        return best[m-1][n-1]
