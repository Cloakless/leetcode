class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)//2):
            if nums[2*i] != nums[2*i+1]:
                return False
        return True
