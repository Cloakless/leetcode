class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        tot = 0
        for num in nums:
            if num != k - num:
                pairs = min(counter[num], counter[k-num])
            else:
                pairs = counter[num] // 2
            counter[num] -= pairs
            counter[k-num] -= pairs
            tot += pairs
        return tot
