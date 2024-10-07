class Solution:

    @lru_cache(maxsize=10000)     
    def rotatedDigits(self, n: int) -> int:
        def is_good(n):
            n = str(n)
            n = set(n)
            if '3' in n or '4' in n or '7' in n:
                return False
            if n.issubset({'0', '1', '8'}):
                return False
            return True
        if n == 1:
            return 0
        return self.rotatedDigits(n-1) + int(is_good(n))
