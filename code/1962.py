class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = list(map(lambda x: -1*x, piles))
        heapq.heapify(piles)
        for i in range(k):
            best = heapq.heappop(piles)
            if best % 2 == 0:
                best //= 2
            else:
                best -= 1
                best //= 2
            heapq.heappush(piles, best)
        return -1 * sum(piles)
