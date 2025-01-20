class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        locations = {}
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                locations[mat[i][j]] = (i,j)
        rows, cols = [0] * m, [0] * n
        for idx in range(m*n):
            x, y = locations[arr[idx]]
            rows[x] += 1
            cols[y] += 1
            if rows[x] == n or cols[y] == m:
                return idx
