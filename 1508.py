class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(n):
            tot = 0
            j = i
            while j < n:
                tot += nums[j]
                sums.append(tot)
                j += 1
        sums.sort()
        return sum(sums[left-1:right]) % (10**9 + 7)
