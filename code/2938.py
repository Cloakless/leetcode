class Solution:
    def minimumSteps(self, s: str) -> int:
        pos = 0
        tot = 0
        for i, c in enumerate(s):
            if c == '0':
                tot += i - pos
                pos += 1
        return tot
