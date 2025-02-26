class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        best, worst, acc = 0, 0, 0
        for num in nums:
            acc += num
            best = max(best, acc)
            worst = min(worst, acc)
        return best - worst
