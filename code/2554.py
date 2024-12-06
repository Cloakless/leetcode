class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bset = set(banned)
        tot, count = 0, 0
        for i in range(1, n+1):
            if tot + i > maxSum:
                return count
            if i not in bset:
                tot += i
                count += 1
        return count
