class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        count = sum(nums)
        acc = 0
        for i in range(len(nums)-1):
            count -= nums[i]
            acc += nums[i]
            if acc >= count:
                ans += 1
        return ans
