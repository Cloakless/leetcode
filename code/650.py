class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        primes = [2,3,5,7,11,13,17,19,23,29,31]
        tot = 0
        for prime in primes:
            while n % prime == 0 and n != 1:
                n /= prime
                tot += prime
        if n != 1:
            tot += int(n)
        return tot 
