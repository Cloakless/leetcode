class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        tot = 0
        if n == 1:
            return tot
        for i in range(1,n):
            if nums[i] < nums[i-1] + 1:
                diff = nums[i-1] + 1 - nums[i]
                nums[i] += diff
                tot += diff
        return tot
