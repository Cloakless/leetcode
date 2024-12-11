class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = (0,0)
        while r < n and nums[r] - nums[l] <= 2*k:
            r += 1
        best = r - l
        while r < n:
            best = max(best, r - l)
            l += 1
            while l <= r and r < n and nums[r] - nums[l] <= 2*k:
                r += 1
            best = max(best, r - l)
        return best
