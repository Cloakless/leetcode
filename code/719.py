class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def num_dist(d):
            left = 0
            right = 0
            pairs = 0
            while left < n:
                while right < n - 1 and nums[right + 1] - nums[left] <= d:
                    right += 1       
                pairs += right - left
                left += 1
                if right < left:
                    right = left
            return pairs
                
        upper = nums[-1] - nums[0]
        lower = 0
        while upper > lower + 1:
            mid = (upper + lower) // 2
            cand = num_dist(mid)
            if cand < k:
                lower = mid
            else:
                upper = mid
        if num_dist(lower) >= k:
            return lower
        return upper
