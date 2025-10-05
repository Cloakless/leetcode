class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        def is_valid(x,y):
            return 0 <= x and x < m and 0 <= y and y < n


        def resolve(ocean):
            dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            unseen = ocean
            seen = set()
            while unseen:
                x, y = unseen.pop()
                seen.add((x, y))
                for (dx, dy) in dirs:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny) and (nx, ny) not in seen and heights[nx][ny] >= heights[x][y]:
                        unseen.add((nx, ny))
            return seen
        
        atlantic = set()
        pacific = set()
        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n-1))

        for j in range(n):
            pacific.add((0, j))
            atlantic.add((m-1, j))

        atlantic = resolve(atlantic)
        pacific = resolve(pacific)
        ans = []
        for (x, y) in atlantic:
            if (x, y) in pacific:
                ans.append([x,y])
        return ans
