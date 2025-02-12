class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = defaultdict(list)
        def dsum(n):
            s = list(str(n))
            ans = 0
            for c in s:
                ans += int(c)
            return ans
        for num in nums:
            digit_sum[dsum(num)].append(num)
        best = -1
        for option in digit_sum:
            digit_sum[option].sort()
            if len(digit_sum[option]) > 1:
                best = max(best, digit_sum[option][-1] + digit_sum[option][-2])
        return best
