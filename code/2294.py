class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        base = nums[0]
        for num in nums:
            if num - base > k:
                ans += 1
                base = num
        return ans
