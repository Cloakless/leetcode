class Solution:
    def scoreOfString(self, s: str) -> int:
        tot = 0
        for i in range(1,len(s)):
            tot += abs(ord(s[i]) - ord(s[i-1]))
        return tot

