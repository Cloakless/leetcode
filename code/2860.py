class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if nums[0] > 0:
            ans = 1
        else:
            ans = 0
        if nums[-1] < n:
            ans += 1
        for i in range(n-1):
            # Select up to i
            if (i+1) > nums[i]:
                if ((i+1) < nums[i+1]):
                    ans += 1
        return ans
