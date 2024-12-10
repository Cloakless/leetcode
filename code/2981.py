class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        def count_subs(sub):
            tot = 0
            m = len(sub)
            for i in range(n-m+1):
                if s[i:i+m] == sub:
                    tot += 1
            return tot
        best = ''
        for o in range(26):
            for l in range(1, n):
                letter = chr(o+97)
                if count_subs(letter*l) >= 3 and l > len(best):
                    best = letter*l
        return -1 if best == '' else len(best)
