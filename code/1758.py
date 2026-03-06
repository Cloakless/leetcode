class Solution:
    def minOperations(self, s: str) -> int:
        best = len(s)
        acc = 0
        curr = 1
        for c in s:
            curr = 1 - curr
            acc += int(curr != int(c))
        best = min(best, acc)
        acc = 0
        curr = 0
        for c in s:
            curr = 1 - curr
            acc += int(curr != int(c))
        best = min(best, acc)
        return best
