class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        counter = defaultdict(int)
        tot = 0
        r = -1
        for l in range(n):
            while tot < k and r + 1 < n:
                r += 1
                tot += counter[nums[r]]
                counter[nums[r]] += 1
            if tot >= k:
                ans += n - r
            counter[nums[l]] -= 1
            tot -= counter[nums[l]]
        return ans
        
