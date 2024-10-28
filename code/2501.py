class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        best = -1
        num_set = set(nums)
        for num in num_set:
            run = 1
            k = num
            while k**2 in num_set:
                run += 1
                k = k**2
            if run > 1 and run > best:
                best = run
        return best
