class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tot = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                tot += 1
                nums[i] = 1
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return tot
