class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m*n):
            ans[i//n][i%n] = original[i]
        return ans
