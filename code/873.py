class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        best = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                streak = 2
                x = arr[i]
                y = arr[j]
                while x + y in nums:
                    streak += 1
                    best = max(best, streak)
                    x, y = y, x + y
        return best
