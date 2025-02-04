class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        acc = nums[0]
        best = acc
        n = len(nums)
        if n == 1:
            return acc
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                acc += nums[i]
                best = max(best, acc)
            else:
                acc = nums[i]
        return best
