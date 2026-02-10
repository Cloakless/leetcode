class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        best, n = 0, len(nums)
        for i in range(n):
            if n - i >= best:
                odds, evens = set(), set()
                for j in range(i,n):
                    if nums[j] % 2 == 0:
                        evens.add(nums[j])
                    else:
                        odds.add(nums[j])
                    if len(odds) == len(evens):
                        best = max(best, j - i + 1)
        return best
