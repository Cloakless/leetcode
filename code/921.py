class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        worst = 0
        for char in s:
            if char == '(':
                count += 1
            else:
                count -= 1
                worst = min(worst, count)

        return count - 2*worst
