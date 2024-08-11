class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # Code from No. 200
        def numIslands(grid: List[List[int]]) -> int:
            m, n = len(grid), len(grid[0])
            bid = [[grid[i][j] for j in range(n)] for i in range(m)]

            def complete_island(i,j):
                checked = set()
                new = set()
                new.add((i,j))
                while bool(new):
                    point = new.pop()
                    checked.add(point)
                    point_x, point_y = point[0], point[1]
                    for p in range(max(point_x-1, 0), min(point_x+2, m)):
                        for q in range(max(point_y-1, 0), min(point_y+2, n)):
                            if bid[p][q] == 1 and (point_x-p)*(point_y-q) == 0 and (point_x != p or point_y != q):
                                if (p,q) not in checked:
                                    new.add((p,q))
                return checked

            num_islands = 0
            for x in range(m):
                for y in range(n):
                    if bid[x][y] == 1:
                        num_islands += 1
                        island = complete_island(x,y)
                        # Wipe everything in this island
                        for point in island:
                            bid[point[0]][point[1]] = 0
            return num_islands

        # Is the island already disconnected
        if numIslands(grid) != 1:
            return 0

        # Else is there a single point we can turn to water to disconnect
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    pass
                else:
                    grid[i][j] = 0
                    if numIslands(grid) != 1:
                        return 1
                    grid[i][j] = 1

        # Else, there will be a corner with only two neighbours
        return 2
