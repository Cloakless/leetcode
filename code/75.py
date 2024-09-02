class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cols = {0:0, 1:0, 2:0}
        for num in nums:
            if num == 0:
                cols[0] += 1
            elif num == 1:
                cols[1] += 1
            else:
                cols[2] += 1
        reds, whites, blues = cols[0], cols[1], cols[2]
        for i in range(reds):
            nums[i] = 0
        for j in range(reds, reds+whites):
            nums[j] = 1
        for k in range(reds+whites, reds+whites+blues):
            nums[k] = 2
