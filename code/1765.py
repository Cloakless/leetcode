class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        opts = [(0,1),(1,0),(-1,0),(0,-1)]

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n

        height = [[0 for _ in range(n)] for _ in range(m)]
        visited = set()
        border = set()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    border.add((i,j))
        while border:
            new_border = set()
            while border:
                x, y = border.pop()
                for opt in opts:
                    dx, dy = opt
                    nx, ny = x + dx, y + dy
                    if is_valid(nx,ny) and (nx, ny) not in border and (nx, ny) not in visited:
                        new_border.add((nx,ny))
                        height[nx][ny] = height[x][y] + 1
                visited.add((x,y))
            border = new_border
        return height
