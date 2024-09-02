class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        best = -1
        neg = set()
        i = 0
        while i < n and nums[i] < 0:
            neg.add(nums[i]*-1)
            i += 1
        while i < n:
            if nums[i] in neg:
                best = nums[i]
            i += 1
        return best
