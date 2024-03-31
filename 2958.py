class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 1
        l = 0
        r = 0
        best = 0
        cts = {num: 0 for num in nums}
        cts[nums[0]] += 1
        while True:
            # try add right
            if r == n - 1:
                return best
            if cts[nums[r+1]] < k:
                r += 1
                cts[nums[r]] += 1
                if (r - l + 1) > best:
                    best = r - l + 1
            # unsuccessful -> remove left
            else:
                cts[nums[l]] -= 1
                l += 1
        return best
