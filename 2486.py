class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        m = len(s)
        j = 0
        n = len(t)
        while i < m:
            if t[j] == s[i]:
                j += 1
                if j >= n:
                    break
            i += 1
        return len(t) - j
