class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        partials = []
        tot = 0
        n = len(nums)
        for i in range(n):
            tot += nums[i]
            tot %= p
            partials.append(tot)
        target = partials[-1]
        if target == 0:
            return 0
        best = n
        recents = {0:-1}
        for j in range(n):
            if nums[j] == target:
                return 1
            diff = (partials[j] - target) % p
            if diff in recents:
                best = min(best, j - recents[diff])
            recents[partials[j] % p] = j
        if best == n:
            return -1
        return best
