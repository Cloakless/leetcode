class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return min(matrix[0])
        for i in range(1,n):
            for j in range(n):
                matrix[i][j] += min(matrix[i-1][max(0,j-1):min(n,j+2)])
        return min(matrix[n-1])
