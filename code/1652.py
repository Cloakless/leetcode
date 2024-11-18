class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = n * [0]
        if k == 0:
            return ans
        if k < 0:
            sign = -1
            k *= -1
        else:
            sign = 1
        for i, elem in enumerate(code):
            for j in range(k):
                ans[i] += code[(i + sign*(1+j)) % n]
        return ans
