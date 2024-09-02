class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        tot = 0
        partials = set([0])
        for i in range(len(nums)-1):
            if (tot + nums[i] + nums[i+1]) % k in partials:
                return True
            tot += nums[i]
            tot = tot % k
            partials.add(tot)
        return False
