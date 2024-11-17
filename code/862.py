class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        shortest = n + 1
        acc = 0
        prefix_sums = []
        for i, num in enumerate(nums):
            acc += num
            if acc >= k and i + 1 < shortest:
                shortest = i + 1
            while prefix_sums and (acc - prefix_sums[0][0] >= k):
                cand = heappop(prefix_sums)[1]
                if i - cand < shortest:
                    shortest = i - cand
            heappush(prefix_sums, (acc, i))

        return -1 if (shortest == n + 1) else shortest
