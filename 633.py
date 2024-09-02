class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def is_square(n):
            return int((n+0.5)**0.5)**2 == n
        for i in range(int((c/2)**0.5)+1):
            if is_square(c-i**2):
                return True
        return False
