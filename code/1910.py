class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = [None] * len(s)
        n = len(part)
        i = -1
        for char in s:
            i += 1
            ans[i] = char
            while (i > n - 2) and (''.join(ans[i-n+1:i+1]) == part):
                i -= n
        return ''.join(ans[:i+1])
