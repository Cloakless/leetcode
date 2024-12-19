class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        num_chunks = 0
        last_chunk = -1
        highest = -1
        for i in range(len(arr)):
            highest = max(arr[i], highest)
            if highest == i:
                num_chunks += 1
        return num_chunks
