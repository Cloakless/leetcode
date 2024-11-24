class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        tot = 0
        neg_count = 0
        smallest = abs(matrix[0][0])
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                if val < 0:
                    neg_count += 1
                    abs_val = -1 * val
                else:
                    abs_val = val
                tot += abs_val
                if abs_val < smallest:
                    smallest = abs_val
        if neg_count % 2 == 0:
            return tot
        else:
            return tot - 2*smallest
