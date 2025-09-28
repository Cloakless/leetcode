class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        n = len(nums)
        for i in range(n-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
