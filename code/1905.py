class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        grid = grid2

        # Solution from problem 200
        m = len(grid)
        n = len(grid[0])

        def complete_island(i,j):
            checked = set()
            new = set()
            new.add((i,j))
            while bool(new):
                point = new.pop()
                checked.add(point)
                point_x = point[0]
                point_y = point[1]
                for p in range(max(point_x-1, 0), min(point_x+2, m)):
                    for q in range(max(point_y-1, 0), min(point_y+2, n)):
                        if grid[p][q] == 1 and (point_x-p)*(point_y-q) == 0 and (point_x != p or point_y != q):
                            if (p,q) not in checked:
                                new.add((p,q))
            return checked

        num_subislands = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    island = complete_island(x,y)
                    # Wipe everything in this island
                    is_subisland = True
                    for point in island:
                        if grid1[point[0]][point[1]] == 0:
                            is_subisland = False
                        grid[point[0]][point[1]] = 0
                    if is_subisland:
                        num_subislands += 1
        return num_subislands
