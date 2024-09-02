class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0

        def is_magic(x,y):
            if set([grid[x][y], grid[x][y+1], grid[x][y+2], grid[x+1][y], grid[x+1][y+1], grid[x+1][y+2], grid[x+2][y], grid[x+2][y+1], grid[x+2][y+2]]) != {1,2,3,4,5,6,7,8,9}:
                return False
            row1 = grid[x][y] + grid[x][y+1] + grid[x][y+2]
            row2 = grid[x+1][y] + grid[x+1][y+1] + grid[x+1][y+2]
            row3 = grid[x+2][y] + grid[x+2][y+1] + grid[x+2][y+2]
            col1 = grid[x][y] + grid[x+1][y] + grid[x+2][y]
            col2 = grid[x][y+1] + grid[x+1][y+1] + grid[x+2][y+1]
            col3 = grid[x][y+2] + grid[x+1][y+2] + grid[x+2][y+2]
            dig1 = grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2]
            dig2 = grid[x+2][y] + grid[x+1][y+1] + grid[x][y+2]
            return len(set([row1, row2, row3, col1, col2, col3, dig1, dig2])) == 1
   
        tot = 0
        for a in range(rows - 2):
            for b in range(cols - 2):
                if is_magic(a,b):
                    tot += 1
        return tot
       
