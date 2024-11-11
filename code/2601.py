class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = [2,3]
        for i in range(5, 1001, 2):
            is_prime = True
            for prime in primes:
                if i % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        
        def largest_prime(k):
            # Returns the largest prime at most k
            if k < 2:
                return 0
            lower = 0
            upper = len(primes) - 1
            while lower + 1 < upper:
                mid = (lower + upper) // 2
                if primes[mid] > k:
                    upper = mid
                else:
                    lower = mid
            if primes[upper] <= k:
                return primes[upper]
            else:
                return primes[lower]
            
        initial_sub = largest_prime(nums[0] - 1)
        nums[0] -= initial_sub
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
            subtract_amount = largest_prime(nums[i] - nums[i-1] - 1)
            nums[i] -= subtract_amount
        return True
