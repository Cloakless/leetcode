class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        import functools
        tot = 0
        @lru_cache(maxsize=1000)
        def dp(num):
            if num < 0:
                return 0
            elif num == 0:
                return 1
            else:
                return dp(num-zero) + dp(num-one) % 1000000007
        for i in range(low, high+1):
            tot += dp(i)
        return tot % 1000000007
