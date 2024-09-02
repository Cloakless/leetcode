class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if nums[0] >= n:
            return n
        for i in range(1,n):
            if (n-i) <= nums[i] and (n-i) > nums[i-1]:
                return (n-i)
        return -1
