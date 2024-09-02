class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        laps = time // (n-1)
        remainder = time % (n-1)
        if laps % 2 == 0:
            return remainder + 1
        else:
            return n - remainder
