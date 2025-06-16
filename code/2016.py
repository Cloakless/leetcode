class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        best = -1
        top = nums[-1]
        for i in reversed(range(len(nums)-1)):
            if top > nums[i]:
                best = max(best, top - nums[i])
            top = max(top, nums[i])
        return best
