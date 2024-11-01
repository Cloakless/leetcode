class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        if len(s) < 3:
            return s
        ans += s[:2]
        for i in range(2, len(s)):
            if s[i] != s[i-1] or s[i] != s[i-2]:
                ans += s[i]
        return ans
