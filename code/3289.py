class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
        return ans
