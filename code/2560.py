class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        if k == 1:
            return min(nums)

        def canRob(amount):
            i = 0
            num = 0
            while i < len(nums):
                if nums[i] <= amount:
                    num += 1
                    i += 1
                i += 1
            return num >= k

        lower = min(nums)
        upper = max(nums)
        while lower + 1 < upper:
            mid = (upper + lower) // 2
            if canRob(mid):
                upper = mid
            else:
                lower = mid

        if canRob(lower):
            return lower
        else:
            return upper
