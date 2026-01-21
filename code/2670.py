class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(-len(set(nums[i+1:])) + len(set(nums[:i+1])))
        return ans
