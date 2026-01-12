class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        x, y = points[0]
        for i in range(1, len(points)):
            newx, newy = points[i]
            ans += max(abs(newx - x), abs(newy - y))
            x, y = newx, newy
        return ans
