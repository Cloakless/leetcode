class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        ans = []
        zero_count = 0
        for num in nums:
            if num > 0:
                ans.append(num)
            else:
                zero_count += 1
        ans = ans + [0] * zero_count
        return ans
