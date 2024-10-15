class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        l_covs = []
        k, i = 0, 1
        while k < ladders and i < n:
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(l_covs, diff)
                k += 1
            i += 1
        while bricks >= 0 and i < n:
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(l_covs, diff)
                cand = heapq.heappop(l_covs)
                bricks -= cand
                if bricks < 0:
                    return i - 1
            i += 1
        return n - 1
