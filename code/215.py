class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        my_heap = []
        for num in nums:
            heapq.heappush(my_heap, -1*num)
        for i in range(k-1):
            heappop(my_heap)
        return -1*heappop(my_heap)
