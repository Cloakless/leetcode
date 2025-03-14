class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canGiveN(n):
            given = 0
            for pile in candies:
                given += pile // n
            return given >= k
        lower = 0
        upper = sum(candies)
        while lower + 1 < upper:
            mid = (lower + upper) // 2
            if canGiveN(mid):
                lower = mid
            else:
                upper = mid
        if canGiveN(upper):
            return upper
        else:
            return lower
