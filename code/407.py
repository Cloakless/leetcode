class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n

        processed = [[False for _ in range(n)] for _ in range(m)]
        boundary = []
        for i in range(m):
            heappush(boundary, (heightMap[i][0], i, 0))
            heappush(boundary, (heightMap[i][n-1], i, n-1))
            processed[i][0], processed[i][n-1] = True, True
        for i in range(n):
            heappush(boundary, (heightMap[0][i], 0, i))
            heappush(boundary, (heightMap[m-1][i], m-1, i))
            processed[0][i], processed[m-1][i] = True, True

        ans = 0
        while boundary:
            h, x, y = heappop(boundary)
            for direction in dirs:
                dx, dy = direction
                nx, ny = x + dx, y + dy
                if is_valid(nx,ny) and not processed[nx][ny]:
                    nh = heightMap[nx][ny]
                    if nh < h:
                        ans += (h - nh)
                    heappush(boundary, (max(h, nh), nx, ny))
                    processed[nx][ny] = True
        return ans
      
