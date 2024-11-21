class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        prison = [[0 for _ in range(n)] for _ in range(m)]
        # 0: unguarded, 1: guarded, 2: wall, 3: guard
        removed = 0
        for (i, j) in guards:
            prison[i][j] = 3
            removed += 1
        for (i, j) in walls:
            prison[i][j] = 2
            removed += 1
        # Then walk each direction
        # East
        for a in range(m):
            guarding = False
            for b in range(n):
                cell = prison[a][b]
                if cell == 2:
                    guarding = False
                elif cell == 3:
                    guarding = True
                elif cell == 0 and guarding == True:
                    prison[a][b] = 1
                    removed += 1
        # West
        for a in range(m):
            guarding = False
            for b in reversed(range(n)):
                cell = prison[a][b]
                if cell == 2:
                    guarding = False
                elif cell == 3:
                    guarding = True
                elif cell == 0 and guarding == True:
                    prison[a][b] = 1
                    removed += 1
        # South
        for b in range(n):
            guarding = False
            for a in range(m):
                cell = prison[a][b]
                if cell == 2:
                    guarding = False
                elif cell == 3:
                    guarding = True
                elif cell == 0 and guarding == True:
                    prison[a][b] = 1
                    removed += 1
        # North
        for b in range(n):
            guarding = False
            for a in reversed(range(m)):
                cell = prison[a][b]
                if cell == 2:
                    guarding = False
                elif cell == 3:
                    guarding = True
                elif cell == 0 and guarding == True:
                    prison[a][b] = 1
                    removed += 1
        return m*n - removed
