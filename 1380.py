class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        lucky = []
        row_mins = [100000 for _ in range(m)]
        col_maxs = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                row_mins[i] = min(row_mins[i], val)
                col_maxs[j] = max(col_maxs[j], val)
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                if row_mins[i] == val and col_maxs[j] == val:
                    lucky.append(val)
        return lucky
