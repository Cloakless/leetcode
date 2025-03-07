class Solution:
    primes = [2,3,5,7,11]
    for num in range(13, 1000001, 2):
        is_prime = True
        for prime in primes:
            if prime > num**0.5:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = Solution.primes
        if left > primes[-1]:
            return [-1, -1]
        l, r = 0, 0
        while primes[l] < left:
            l += 1
        while r < len(primes) - 1 and primes[r+1] <= right:
            r += 1
        best = 100000000
        if r - l < 1:
            return [-1, -1]
        for i in range(l, r):
            if primes[i+1] - primes[i] < best:
                best_l = primes[i]
                best_r = primes[i+1]
                best = primes[i+1] - primes[i]
        return [best_l, best_r]
