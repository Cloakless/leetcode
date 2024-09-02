class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        output = [[0 for i in range(n-2)] for j in range(n-2)]
        for i in range(1,n-1):
            for j in range(1,n-1):
                peak = 0
                for a in range(-1,2):
                    for b in range(-1,2):
                        peak = max(peak, grid[i+a][j+b])
                output[i-1][j-1] = peak
        return output
