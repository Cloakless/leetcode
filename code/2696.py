class Solution:
    def minLength(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        ind = 0
        s = list(s)
        while ind < n - 1:
            if (s[ind] == 'A' and s[ind+1] == 'B') or (s[ind] == 'C' and s[ind+1] == 'D'):
                s.pop(ind+1)
                s.pop(ind)
                n -= 2
                if ind > 0:
                    ind -= 1
            else:
                ind += 1
        return n
