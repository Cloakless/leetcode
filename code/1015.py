class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1
        counter = 1
        remainders = set()
        while n % k != 0 and n % k not in remainders:
            remainders.add(n%k)
            n *= 10
            n += 1
            counter += 1
        if n % k == 0:
            return counter
        return -1
