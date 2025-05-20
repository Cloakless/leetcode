class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        changes = [0]*n
        for query in queries:
            l, r = query
            changes[l] += 1
            if r < n - 1:
                changes[r+1] -= 1
        acc = 0
        for i in range(n):
            acc += changes[i]
            if nums[i] > acc:
                return False
        return True
