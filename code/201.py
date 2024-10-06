class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        bit = 1
        while bit <= left:
            if left&bit != 0:
                if right&bit != 0 and right - left < bit:
                    ans += bit
            bit *= 2
        return ans
