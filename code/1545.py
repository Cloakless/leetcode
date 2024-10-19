class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            return bin((2**len(s) - 1) - int(s, 2))[2:]
        s = ["0"] * n
        for i in range(1, n):
            s[i] = s[i-1] + "1" + invert(s[i-1])[::-1]

        return s[n-1][k-1]
