class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best = max(nums)
        ans, streak = 0, 0
        for num in nums:
            if num == best:
                streak += 1
            else:
                streak = 0

            ans = max(ans, streak)
        return ans
