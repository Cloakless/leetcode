class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        prev = nums[0] - k - 1
        for num in nums:
            curr = min(max(num-k, prev+1), num+k)
            if curr > prev:
                ans += 1
                prev = curr
        return ans
