class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        curr = (1 - nums[0]) % 2
        evens, odds, alts = 0, 0, 0
        for num in nums:
            num %= 2
            if num == 0:
                evens += 1
            else:
                odds += 1
            if num != curr:
                alts += 1
                curr = 1 - curr
        return max(evens, odds, alts)
