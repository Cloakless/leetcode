class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        while True:
            if nums[1] == -1:
                return nums[0]
            for i in range(n):
                if i+1 == n or nums[i+1] == -1:
                    nums[i] = -1
                    break
                else:
                    nums[i] = (nums[i] + nums[i+1]) % 10
