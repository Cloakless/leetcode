class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        best = 2
        i = 0
        num_same = 0
        last = None
        for j in range(n-1):
            if s[j] != s[j+1]:
                best = max(best, j + 1 - i + 1)
            else:
                if last is None:
                    last = j + 1
                    best = max(best, last + 1)
                else:
                    best = max(best, j + 1 - last)
                    i = last
                    last = j + 1
        return best
