class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        tot = 0
        while i < len(s) - 1:
            if s[i] != s[i+1]:
                tot += 1
            i += 2
        return tot
