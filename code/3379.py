class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i, num in enumerate(nums):
            if num > 0:
                transform = (i + num) % n
            elif num < 0:
                transform = (i + num) % n
            else:
                transform = i
            ans[i] = nums[transform]
        return ans
