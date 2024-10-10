class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            if nums[1] >= nums[0]:
                return 1
            else:
                return 0
        bases = [0] * n
        lowest = nums[0]
        for i in range(n):
            lowest = min(lowest, nums[i])
            bases[i] = lowest

        best = 0
        # For each endpoint find the earliest ramp start-point with binary search
        for j in reversed(range(1,n)):
            lower = 0
            upper = j - 1
            if nums[0] <= nums[j]:
                if j > best:
                    best = j
            elif nums[j] < bases[j-1]:
                continue
            else:
                while lower + 1 < upper:
                    mid = (upper + lower) // 2
                    if bases[mid] <= nums[j]:
                        upper = mid
                    else:
                        lower = mid
                if j - lower - 1 > best:
                    best = j - lower - 1
        return best
