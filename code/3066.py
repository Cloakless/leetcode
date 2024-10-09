class Solution:
    import heapq
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ops = 0
        while True:
            x = heapq.heappop(nums)
            if x >= k:
                return ops
            else:
                ops += 1
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
