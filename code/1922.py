class Solution:
    def countGoodNumbers(self, n: int) -> int:
        tot = pow(20, n//2, 10**9 + 7)
        if n % 2 != 0:
            tot *= 5
        return tot % (10**9 + 7)
