class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totSum = sum(nums)
        if totSum < target:
            return 0
        dp = [[0 for _ in range(-totSum, totSum + 1)] for _ in range(len(nums))]
        dp[0][nums[0]+totSum] += 1
        dp[0][-nums[0]+totSum] += 1
        for i in range(1, len(nums)):
            for j in range(-totSum, totSum + 1):
                if dp[i-1][j+totSum] > 0:
                    dp[i][j+totSum+nums[i]] += dp[i-1][j+totSum]
                    dp[i][j+totSum-nums[i]] += dp[i-1][j+totSum]
        return dp[len(nums)-1][target+totSum]
