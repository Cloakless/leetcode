class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        ans = 0
        r = 0
        counter = {}
        n = len(nums)
        for l in range(n):
            if l > 0:
                counter[nums[l-1]] -= 1
                if counter[nums[l-1]] == 0:
                    counter.pop(nums[l-1])
            while r < n and len(counter) < k:
                if nums[r] not in counter:
                    counter[nums[r]] = 0
                counter[nums[r]] += 1
                r += 1
            if len(counter) == k:
                ans += n - r + 1
        return ans
        
