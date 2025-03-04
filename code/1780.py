class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        diff = 1
        while 3*diff <= n:
            diff *= 3

        while diff:
            if n >= diff:
                n -= diff
            diff //= 3
        return n == 0
