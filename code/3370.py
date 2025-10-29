class Solution:
    def smallestNumber(self, n: int) -> int:
        base = 1
        while base <= n:
            base *= 2
        return base - 1
