class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        best = 0
        last = nums[-1]
        for num in nums:
            best = max(best, abs(num-last))
            last = num
        return best
