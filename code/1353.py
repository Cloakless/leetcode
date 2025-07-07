class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        end_day = 0
        for event in events:
            end_day = max(end_day, event[1])
        ends = []
        ans, j = 0, 0
        for i in range(end_day + 1):
            while j < n and events[j][0] <= i:
                heappush(ends, events[j][1])
                j += 1
            while ends and ends[0] < i:
                _ = heappop(ends)
            if ends:
                _ = heappop(ends)
                ans += 1
        return ans
