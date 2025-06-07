class Solution:
    def clearStars(self, s: str) -> str:
        chars = []
        removed = set()
        for idx, c in enumerate(s):
            if c == '*':
                l, i = heappop(chars)
                removed.add(-1*i)
            else:
                heappush(chars, (c, -1*idx))
        ans = ''
        for idx, c in enumerate(s):
            if c != '*' and idx not in removed:
                ans += c
        return ans
