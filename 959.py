class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        big_grid = [['' for _ in range(3*n)] for _ in range(3*n)]

        for row in range(n):
            for index in range(n):
                if grid[row][index] == ' ':
                    big_grid[3*row][3*index] = "1"
                    big_grid[3*row][3*index+1] = "1"
                    big_grid[3*row][3*index+2] = "1"
                    big_grid[3*row+1][3*index] = "1"
                    big_grid[3*row+1][3*index+1] = "1"
                    big_grid[3*row+1][3*index+2] = "1"
                    big_grid[3*row+2][3*index] = "1"
                    big_grid[3*row+2][3*index+1] = "1"
                    big_grid[3*row+2][3*index+2] = "1"
                elif grid[row][index] == '/':
                    big_grid[3*row][3*index] = "1"
                    big_grid[3*row][3*index+1] = "1"
                    big_grid[3*row][3*index+2] = "0"
                    big_grid[3*row+1][3*index] = "1"
                    big_grid[3*row+1][3*index+1] = "0"
                    big_grid[3*row+1][3*index+2] = "1"
                    big_grid[3*row+2][3*index] = "0"
                    big_grid[3*row+2][3*index+1] = "1"
                    big_grid[3*row+2][3*index+2] = "1"
                elif grid[row][index] == '\\':
                    big_grid[3*row][3*index] = "0"
                    big_grid[3*row][3*index+1] = "1"
                    big_grid[3*row][3*index+2] = "1"
                    big_grid[3*row+1][3*index] = "1"
                    big_grid[3*row+1][3*index+1] = "0"
                    big_grid[3*row+1][3*index+2] = "1"
                    big_grid[3*row+2][3*index] = "1"
                    big_grid[3*row+2][3*index+1] = "1"
                    big_grid[3*row+2][3*index+2] = "0"

        def numIslands(grid: List[List[str]]) -> int:
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
                            if grid[p][q] == '1' and (point_x-p)*(point_y-q) == 0 and (point_x != p or point_y != q):
                                if (p,q) not in checked:
                                    new.add((p,q))
                return checked

            num_islands = 0
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == '1':
                        num_islands += 1
                        island = complete_island(x,y)
                        # Wipe everything in this island
                        for point in island:
                            grid[point[0]][point[1]] = '0'
            return num_islands

        return numIslands(big_grid)
