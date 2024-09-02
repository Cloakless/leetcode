class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0 for b in range(n)] for a in range(m)]
        for i in range(m):
            for j in range(n):
                cand = min(rowSum[i], colSum[j])
                matrix[i][j] = cand
                rowSum[i] -= cand
                colSum[j] -= cand
        return matrix
 
