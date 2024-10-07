class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        starts = events
        n = len(events)
        starts.sort(key=lambda x: -1*x[0])
        best = 0
        start_vals = []
        for start in starts:
            best = max(best, start[2])
            start_vals.append([start[0], best])
        start_vals.sort(key=lambda x: x[0])
        events.sort(key=lambda x: x[0])
        max_val = 0
        for i in range(len(events)):
            event = events[i]
            target = event[1] + 1
            if start_vals[-1][0] < target:
                continue
            lower, upper = 0, n
            while lower + 1 < upper:
                mid = (lower + upper) // 2
                if start_vals[mid][0] > target:
                    upper = mid
                else:
                    lower = mid
            if start_vals[lower][0] < target:
                next_one = lower+1
            else:
                next_one = lower
            best_of_rest = start_vals[next_one][1]
            best = max(best, event[2]+best_of_rest)
        return best
