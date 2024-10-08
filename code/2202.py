class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k % 2 == 1 and n == 1:
            return -1
        if k == 1:
            return nums[1]
        best = 0
        for i in range(n):
            if i == k or i < k - 1:
                best = max(best, nums[i])
        return best
