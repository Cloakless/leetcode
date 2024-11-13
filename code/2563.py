class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        ans = 0
        if n == 1:
            return 0
        nums.sort()

        def count_pairs(bound):
            tot = 0
            l = 0
            r = n-1
            while nums[l] + nums[r] > bound and r >= l:
                r -= 1
            while l < r:
                tot += r - l
                l += 1
                while nums[l] + nums[r] > bound and r >= l:
                    r -= 1
            return tot

        return count_pairs(upper) - count_pairs(lower - 1)      
