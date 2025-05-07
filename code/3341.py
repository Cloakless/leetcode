class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        t = -1
        m, n = len(moveTime), len(moveTime[0])
        options = [(0, 0, 0)]
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        seen = set()
        moveTime[0][0] = 0

        while True:
            t = max(t+1, options[0][0])
            news = set()
            while options and options[0][0] == t:
                _, x, y = heappop(options)
                if x == m-1 and y == n-1:
                    return t
                if (x,y) not in seen:
                    seen.add((x, y))
                    for opt in dirs:
                        dx, dy = opt
                        nx, ny = x + dx, y + dy
                        if 0 <= nx and nx < m and 0 <= ny and ny < n:
                            if (nx, ny) not in seen:
                                news.add((nx, ny))
            for new in news:
                nx, ny = new
                heappush(options, (max(moveTime[nx][ny] + 1, t+1), nx, ny))
