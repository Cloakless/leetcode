class Solution:
    from collections import defaultdict
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        partials = defaultdict(int) 
        tot, ans = 0, 0
        partials[0] += 1
        for i in range(len(nums)):
            tot += nums[i]
            tot %= k
            partials[tot] += 1
        for thing in partials:
            n = partials[thing]
            ans += n*(n-1)//2
        return ans
