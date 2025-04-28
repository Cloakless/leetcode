class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        acc = 0
        left = 0
        for right in range(n):
            acc += nums[right]
            while left <= right and (acc * (right - left + 1)) >= k:
                left += 1
                acc -= nums[left-1]
            ans += right - left + 1
        return ans
