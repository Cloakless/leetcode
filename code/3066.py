class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_heap = []
        for num in nums:
            heappush(num_heap, num)
        ops = 0
        while len(num_heap) > 1 and num_heap[0] < k:
            x = heappop(num_heap)
            y = heappop(num_heap)
            heappush(num_heap, min(x,y)*2 + max(x,y))
            ops += 1
        return ops
