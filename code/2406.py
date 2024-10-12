class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            heappush(events, (start, -1))
            heappush(events, (end, 1))

        # Run through events
        tot = 0
        best = 0
        while events:
            time, direction = heappop(events)
            tot += -1*direction
            if tot > best:
                best = tot
        return best
