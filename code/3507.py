class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        decreasing = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                decreasing = True
                break
        while decreasing:
            # print(nums)
            decreasing = False
            if len(nums) == 1:
                return ans
            min_sum = nums[0] + nums[1]
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    decreasing = True
                min_sum = min(min_sum, nums[i] + nums[i-1])
            combined = False
            new_nums = []
            i = 0
            while i < len(nums):
                if decreasing and not combined and (nums[i] + nums[i + 1] == min_sum):
                    combined = True
                    new_nums.append(nums[i] + nums[i+1])
                    i += 1
                    ans += 1
                else:
                    new_nums.append(nums[i])
                i += 1
            nums = new_nums
        return ans
