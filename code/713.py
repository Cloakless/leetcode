class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        tot = 0
        p = 1
        n = len(nums)
        for elem in nums:
            p *= elem
        if p < k:
            return int(n*(n+1)/2)
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                if prod < k:
                    tot += 1
                else:
                    break
        return tot
