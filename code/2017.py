class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        rights, lefts = [0]*n, [0]*n
        l_acc, r_acc = 0, 0
        for i in range(1, n):
            lefts[i] = lefts[i-1] + grid[1][i-1]
            rights[n-i-1] = rights[n-i] + grid[0][n-i]
        best = 1000000000000
        for i in range(n):
            best = min(best, max(lefts[i], rights[i]))
        return best
