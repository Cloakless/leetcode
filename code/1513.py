class Solution:
    def numSub(self, s: str) -> int:
        groups = s.split('0')
        ans = 0
        for group in groups:
            n = len(group)
            ans += (n**2 + n) // 2
            ans %= 10**9 + 7
        return ans
