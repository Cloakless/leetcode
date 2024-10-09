class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1]-x[0])

        def overlaps(a, b):
            return b[0] <= a[0] and b[1] >= a[1]

        ans = [intervals[-1]]
        for interval in reversed(intervals[:n-1]):
            if not any([overlaps(interval, bigger_one) for bigger_one in ans]):
                ans.append(interval)
        return len(ans)
