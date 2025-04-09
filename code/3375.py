class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = set()
        for num in nums:
            if num > k:
                ops.add(num)
            elif num < k:
                return -1
        return len(ops)
