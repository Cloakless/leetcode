class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        l = 0
        n, best = len(nums), 1
        nums.sort()
        for r in range(n):
            while nums[l] * k < nums[r]:
                l += 1
            best = max(best, r-l+1)
        return n - best
