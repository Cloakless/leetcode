class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def cost(a,b):
            return abs(ord(a)-ord(b))
        costs = [cost(s[i],t[i]) for i in range(len(s))]
        l = 0
        r = 0
        n = len(s)
        if sum(costs) < maxCost:
            return n
        tot = 0
        best = min(costs)
        if best > maxCost:
            return 0
        best = 0
        curr_cost = 0
        while r < n:
            if curr_cost + costs[r] <= maxCost:
                curr_cost += costs[r]
                r += 1
                tot += 1
            else:
                curr_cost -= costs[l]
                l += 1 
                tot -= 1
            best = max(best, tot)
        return best
