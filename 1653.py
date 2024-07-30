class Solution:
    def minimumDeletions(self, s: str) -> int:
        bs = 0
        dels = 0
        for c in s:
            if c == 'a':
                dels = min(dels + 1, bs)
            else:
                bs += 1
        return dels
