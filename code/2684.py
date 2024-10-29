class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = 0
        valid_rows = set()
        for i in range(m):
            valid_rows.add(i)
        for col in range(1, n):
            new_rows = set()
            for a in range(m):
                is_valid = False
                for x in range(max(0, a-1), min(m, a+2)):
                    if x in valid_rows and grid[a][col] > grid[x][col-1]:
                        is_valid = True
                if is_valid:
                    new_rows.add(a)
            if len(new_rows) > 0:
                moves += 1
            else:
                break
            valid_rows = new_rows
        return moves
